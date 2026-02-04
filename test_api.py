#!/usr/bin/env python3
"""
Test script for Octofit Tracker API endpoints
"""
import os
import json
try:
    import urllib.request
    from urllib.error import URLError
except ImportError:
    print("urllib not available")
    exit(1)

# Determine base URL
codespace_name = os.environ.get('CODESPACE_NAME', '')
if codespace_name:
    base_url = f"https://{codespace_name}-8000.app.github.dev"
    print(f"Testing API with Codespace URL: {base_url}")
else:
    base_url = "http://localhost:8000"
    print(f"Testing API with localhost: {base_url}")

# Test endpoints
endpoints = [
    ('API Root', '/api/'),
    ('Users', '/api/users/'),
    ('Teams', '/api/teams/'),
    ('Activities', '/api/activities/'),
    ('Leaderboard', '/api/leaderboard/'),
    ('Workouts', '/api/workouts/'),
]

print("\n" + "="*60)
for name, endpoint in endpoints:
    try:
        url = base_url + endpoint
        print(f"\nTesting {name}: {url}")
        print("-" * 60)
        
        with urllib.request.urlopen(url, timeout=5) as response:
            data = response.read().decode('utf-8')
            json_data = json.loads(data)
            print(json.dumps(json_data, indent=2))
            print(f"✓ {name} endpoint working!")
            
    except URLError as e:
        print(f"✗ Failed to fetch {name}: {e}")
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON response for {name}: {e}")
        print(f"Response: {data[:200]}")
    except Exception as e:
        print(f"✗ Error testing {name}: {e}")

print("\n" + "="*60)
print("API testing completed!")
print("="*60)
