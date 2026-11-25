import requests

ROBOT_URL = "http://172.22.11.2:1250/?action=getdevices"

print(f"Testing connection to {ROBOT_URL}...")

try:
    response = requests.get(ROBOT_URL, timeout=5)
    response.raise_for_status()  # if bad response
    print("\n--- RAW RESPONSE ---")
    print(response.text)
    print("--- END ---\n")
    print("Response Received")
except requests.exceptions.ConnectionError:
    print("Error: Could not reach the robot")  # DNR DNR DNR
    print("Check that you are connected to the robot's WiFi or USB, and that the robot is powered on.")
except requests.exceptions.Timeout:
    print("Error: The robot took long to respond")
except requests.exceptions.HTTPError as e:
    print(f"Error: the robot returned an HTTP error: {e}")
