#!/bin/bash

# Test script for Octofit Tracker API endpoints
# Get the Codespace URL or use localhost

if [ -n "$CODESPACE_NAME" ]; then
    BASE_URL="https://${CODESPACE_NAME}-8000.app.github.dev"
    echo "Testing API with Codespace URL: $BASE_URL"
else
    BASE_URL="http://localhost:8000"
    echo "Testing API with localhost: $BASE_URL"
fi

echo -e "\n========================================="
echo "Testing API Root"
echo "========================================="
curl -s "${BASE_URL}/api/" | python3 -m json.tool || echo "Failed to fetch API root"

echo -e "\n========================================="
echo "Testing Users Endpoint"
echo "========================================="
curl -s "${BASE_URL}/api/users/" | python3 -m json.tool || echo "Failed to fetch users"

echo -e "\n========================================="
echo "Testing Teams Endpoint"
echo "========================================="
curl -s "${BASE_URL}/api/teams/" | python3 -m json.tool || echo "Failed to fetch teams"

echo -e "\n========================================="
echo "Testing Activities Endpoint"
echo "========================================="
curl -s "${BASE_URL}/api/activities/" | python3 -m json.tool || echo "Failed to fetch activities"

echo -e "\n========================================="
echo "Testing Leaderboard Endpoint"
echo "========================================="
curl -s "${BASE_URL}/api/leaderboard/" | python3 -m json.tool || echo "Failed to fetch leaderboard"

echo -e "\n========================================="
echo "Testing Workouts Endpoint"
echo "========================================="
curl -s "${BASE_URL}/api/workouts/" | python3 -m json.tool || echo "Failed to fetch workouts"

echo -e "\n========================================="
echo "All API tests completed!"
echo "========================================="
