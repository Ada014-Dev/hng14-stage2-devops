#!/bin/bash
set -e

docker compose up -d --build

echo "Waiting for services..."
sleep 30

JOB_ID=$(curl -s -X POST http://localhost:3000/submit | jq -r '.job_id')
echo "Job ID: $JOB_ID"

for i in {1..10}; do
STATUS=$(curl -s http://localhost:3000/status/$JOB_ID | jq -r '.status')
echo "Status: $STATUS"
if [ "$STATUS" = "completed" ]; then
echo "Job completed successfully"
docker compose down
exit 0
fi
sleep 5
done

echo "Job did not complete in time"
docker compose down
exit 1
