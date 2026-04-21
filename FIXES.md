File: api/main.py
Line: 8
Bug: Redis connected to localhost instead of Docker service name
Fix: Replaced with redis_url from environment variable using Redis.from_url()

File: api/main.py
Line: 9
Bug: Duplicate Redis connection statements merged on one line (invalid syntax)
Fix: Removed duplicate `r = redis.Redis(host="localhost", port=6379)`

File: api/main.py
Line: 14
Bug: Queue name was "job" (singular), worker reads from "jobs" (plural)
Fix: Changed r.lpush("job", job_id) to r.lpush("jobs", job_id)

File: api/main.py
Bug: Missing /health endpoint for Docker healthcheck
Fix: Added GET /health endpoint returning {"status": "ok"}

File: worker/worker.py
Line: 5
Bug: Redis connected to localhost instead of Docker service name
Fix: Replaced with redis_url from environment variable using Redis.from_url()

File: worker/worker.py
Bug: No graceful shutdown handling
Fix: Added SIGTERM and SIGINT signal handlers so worker exits cleanly

File: worker/worker.py
Bug: Queue name was "job" (singular), mismatched with API
Fix: Changed brpop("job") to brpop("jobs")

File: frontend/app.js
Line: 6
Bug: API_URL hardcoded as localhost, breaks inside Docker
Fix: Changed to process.env.API_URL || "http://api:8000"

File: frontend/app.js
Line: 13
Bug: req.body not passed to API when submitting job
Fix: Changed axios.post(`${API_URL}/jobs`) to axios.post(`${API_URL}/jobs`, req.body)

File: frontend/app.js
Bug: Missing /health endpoint for Docker healthcheck
Fix: Added GET /health endpoint returning {"status": "ok"}

File: api/requirements.txt
Bug: No version numbers pinned
Fix: Pinned fastapi==0.104.1, uvicorn==0.24.0, redis==5.0.1

File: worker/requirements.txt
Bug: No version numbers pinned
Fix: Pinned redis==5.0.1
