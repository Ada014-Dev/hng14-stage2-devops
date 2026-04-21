# HNG14 Stage 2 DevOps - Containerized Microservices

## Prerequisites
- Docker
- Docker Compose
- Git

## Services
- **Frontend** (Node.js) - Job submission UI on port 3000
- **API** (Python/FastAPI) - Job creation and status on port 8000
- **Worker** (Python) - Processes jobs from Redis queue
- **Redis** - Shared message queue

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Ada014-Dev/hng14-stage2-devops
cd hng14-stage2-devops

### 2. Copy the example env file
cp .env.example .env

### 3. Build and start all services
docker compose up --build

### 4. Verify all services are healthy
docker compose ps

## Successful Startup
You should see all 4 services running:
- redis - healthy
- api - healthy
- worker - running
- frontend - healthy

Visit http://localhost:3000 to access the frontend.

## Submitting a Job
1. Open http://localhost:3000 in your browser
2. Click Submit Job
3. Copy the job ID returned
4. Check status at http://localhost:3000/status/job_id

## Tearing Down
docker compose down

## Bugs Fixed
See FIXES.md for a full list of all bugs found and fixed.

