import redis
import time
import os
import signal

redis_url = os.getenv("REDIS_URL", "redis://redis:6379")
r = redis.Redis.from_url(redis_url)

running = True


def handle_shutdown(sig, frame):
    global running
    running = False


signal.signal(signal.SIGTERM, handle_shutdown)
signal.signal(signal.SIGINT, handle_shutdown)


def process_job(job_id):
    print(f"Processing job {job_id}")
    time.sleep(2)
    r.hset(f"job:{job_id}", "status", "completed")
    print(f"Done: {job_id}")


while running:
    job = r.brpop("jobs", timeout=5)
    if job:
        _, job_id = job
        process_job(job_id.decode())
