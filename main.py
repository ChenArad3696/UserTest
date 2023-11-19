import requests

base_url = "http://127.0.0.1:5000"

test_data = {
    "user_id": 1,
    "problem_description": "My device is making weird noises",
    "device_serial_number": "51-B-125447-DC",
    "indicator_light1": "on",
    "indicator_light2": "on",
    "indicator_light3": "off"
}


def submit_form(data):
    url = f"{base_url}/api/submit_form"
    response = requests.post(url, json=data)
    return response.json()


# Test the API
if __name__ == "__main__":
    submission_response = submit_form(test_data)
    print("Submission Response:", submission_response)
