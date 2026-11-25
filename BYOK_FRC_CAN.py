import keyring

SERVICE_NAME = "BYOK_FRC_CAN"


def save_api_key(user_key):
    keyring.set_password(SERVICE_NAME, "api_key", user_key)
    print("API key saved successfully.")


def get_api_key():
    return keyring.get_password(SERVICE_NAME, "api_key")


def has_api_key():
    key = get_api_key()
    if key is None:
        return False
    return True


key = get_api_key()
if key is None:
    print("Please enter your API key in the settings menu.")