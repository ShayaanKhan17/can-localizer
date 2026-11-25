import json

fake_robot_response = """
[

    {"model":"Talon FX","id":1,"name":"FrontLeftDrive"},
    {"model":"Talon FX","id":2,"name":"FrontLeftSteer"},
    {"model":"Talon FX","id":3,"name":"FrontRightDrive"}

]
"""
print("Fake robot response:")
print(fake_robot_response)

devices = json.loads(fake_robot_response)
print("\nParsed devices:")
for device in devices:
    print(f"Device ID: {device['id']}, Name: {device['name']}, Model: {device['model']}")


