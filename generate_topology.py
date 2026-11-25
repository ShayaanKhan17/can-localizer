import json
import base64
from BYOK_FRC_CAN import get_api_key

def generate_topology_json(image_path, output_json_path="topology.json"):
    # Load API key from the keyring
    user_key = get_api_key()

    if not user_key:
        print("Error: No API key found.")
        print("Please run your temporary test block in BYOK_FRC_CAN.py to save one.") #placeholder
        return None

    try:
        from openai import OpenAI
    except ModuleNotFoundError:
        print("Error: The OpenAI package is not installed. Run: python -m pip install openai")
        return None

    client = OpenAI(
        api_key=user_key,
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    )

    print(f"Reading schematic: {image_path}...")
    try:
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: Could not find the image file '{image_path}'.")
        return None

    print("Parsing the schematic. This may take 5-10 seconds...")
    
    # 3. Send the image to the AI
    try:
        response = client.chat.completions.create(
            model="gemini-2.5-flash", 
            response_format={ "type": "json_object" },
            messages=[
                {
                    "role": "system",
                    "content": """You are an expert FRC electrical engineer. 
                    Analyze the provided wiring diagram and extract the CAN bus daisy chain topology.
                    Output a JSON object with a single key called 'devices'.
                    'devices' should be an array of objects.
                    Each object must have 'id', 'name', 'type', and 'bus' (default 'rio').
                    Order them based on the physical daisy chain from the roboRIO."""
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Extract the CAN topology from this schematic."},
                        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}}
                    ]
                }
            ]
        )

        # 4. Save output
        parsed_json = json.loads(response.choices[0].message.content)
        
        with open(output_json_path, "w") as f:
            json.dump(parsed_json, f, indent=4)
            
        print(f"Success: Topology saved to {output_json_path}")
        return parsed_json
        
    except Exception as e:
        print(f"AI Error: {e}")
        return None

# --- Test it out ---
if __name__ == "__main__":
    # 1. Save a real wiring diagram image to your folder.
    # 2. Change the filename below to match your image.
    # generate_topology_json("my_robot_schematic.jpg")
    print("Script loaded. Uncomment the line above to test with an image.")