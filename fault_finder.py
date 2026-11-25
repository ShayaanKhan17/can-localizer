expected_ids = [1, 2, 3, 4, 5, 6]

observed_ids = [1, 2, 3] #hardcoded to test

print("\nChecking for missing device IDs...")

last_seen_device = None
fault_found = False

for expected_id in expected_ids:
    if expected_id in observed_ids:
        last_seen_device = expected_id
    else:
        fault_found = True

        if last_seen_device is None:
            print("Likely fault between the roboRIO and the first device (ID " + str(expected_id) + ").")
        else:
            print("Likely fault between device ID " + str(last_seen_device) + " and device ID " + str(expected_id) + ".")

            break

if not fault_found:
    print("No issues were found)")
