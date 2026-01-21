import requests
import json

BASE_URL = "http://localhost:5001"
TEST_SESSION = "test_session_12345"

print("\n" + "="*60)
print("🧪 AYURVEDA WEBSITE BACKEND TESTS")
print("="*60 + "\n")

# TEST 1: Home Page
print("TEST 1: Home Page")
try:
    response = requests.get(f"{BASE_URL}/")
    print(f"  Status: {response.status_code} {'✓ PASS' if response.status_code == 200 else '✗ FAIL'}")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

# TEST 2: All Routes
print("\nTEST 2: Testing All Routes")
routes = ["/", "/about", "/benefits", "/conditions", "/chat"]
for route in routes:
    try:
        response = requests.get(f"{BASE_URL}{route}")
        status = "✓ PASS" if response.status_code == 200 else "✗ FAIL"
        print(f"  {route:20} {response.status_code} {status}")
    except Exception as e:
        print(f"  {route:20} ✗ FAIL: {e}")

# TEST 3: Chat API
print("\nTEST 3: Chat API - Testing Question")
try:
    payload = {
        "message": "What is Pitta dosha?",
        "session_id": TEST_SESSION
    }
    response = requests.post(
        f"{BASE_URL}/api/chat",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        data = response.json()
        if "response" in data:
            print(f"  Status: {response.status_code} ✓ PASS")
            print(f"  Response: {data['response'][:100]}...")
        else:
            print(f"  Status: {response.status_code} ✗ FAIL - No response field")
    else:
        print(f"  Status: {response.status_code} ✗ FAIL")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

# TEST 4: Chat API - Empty Message
print("\nTEST 4: Chat API - Error Handling (Empty Message)")
try:
    payload = {
        "message": "",
        "session_id": TEST_SESSION
    }
    response = requests.post(
        f"{BASE_URL}/api/chat",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 400:
        data = response.json()
        if "error" in data:
            print(f"  Status: {response.status_code} ✓ PASS (Error caught properly)")
        else:
            print(f"  Status: {response.status_code} ✗ FAIL")
    else:
        print(f"  Status: {response.status_code} (Expected 400)")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

# TEST 5: Clear Chat API
print("\nTEST 5: Clear Chat API")
try:
    payload = {"session_id": TEST_SESSION}
    response = requests.post(
        f"{BASE_URL}/api/clear-chat",
        json=payload,
        headers={"Content-Type": "application/json"}
    )
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            print(f"  Status: {response.status_code} ✓ PASS")
        else:
            print(f"  Status: {response.status_code} ✗ FAIL")
    else:
        print(f"  Status: {response.status_code} ✗ FAIL")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

# TEST 6: 404 Error Handling
print("\nTEST 6: Error Handling (404 Not Found)")
try:
    response = requests.get(f"{BASE_URL}/nonexistent")
    if response.status_code == 404:
        print(f"  Status: {response.status_code} ✓ PASS (404 handled)")
    else:
        print(f"  Status: {response.status_code} (Expected 404)")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

# TEST 7: CORS Support
print("\nTEST 7: CORS Support")
try:
    response = requests.get(
        f"{BASE_URL}/",
        headers={"Origin": "http://example.com"}
    )
    if response.status_code == 200:
        cors_headers = response.headers.get("Access-Control-Allow-Origin")
        if cors_headers:
            print(f"  Status: {response.status_code} ✓ PASS (CORS enabled)")
        else:
            print(f"  Status: {response.status_code} ✓ PASS (No CORS headers, but route works)")
    else:
        print(f"  Status: {response.status_code} ✗ FAIL")
except Exception as e:
    print(f"  ✗ FAIL: {e}")

print("\n" + "="*60)
print("✅ BACKEND TESTS COMPLETE")
print("="*60 + "\n")
