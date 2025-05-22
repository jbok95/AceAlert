"""BOOKS TEE TIME FOR NEWLY AVAILABLE TIME"""
from datetime import datetime
import json
import requests

from config import PRIVATE_HEADERS, PRIVATE_PAYLOAD

def generate_payload(date_time, num_golfers):
    """RETURNS FULL PAYLOAD FOR THE OPTIMAL TIME FOUND"""

    dt_object = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    formatted_date = dt_object.strftime("%d%H%M")

    my_payload = PRIVATE_PAYLOAD

    # Update payload for target date and time
    my_payload["time"] = date_time
    my_payload["start_front"] = int("202311"+formatted_date)

    # Update payload for number of golfers
    update_int_golfers = ['available_spots', 'available_spots_18']
    for field in update_int_golfers:
        my_payload[field] = num_golfers

    update_str_golfers = ['players', 'pay_players']
    for field in update_str_golfers:
        my_payload[field] = str(num_golfers)

    return my_payload


def book_tee_time(payload):
    """BOOKS TEE TIME"""

    url = "https://foreupsoftware.com/index.php/api/booking/users/reservations"
    # Convert JSON dictionary to a string
    json_payload = json.dumps(payload)

    # Set Headers for POST request
    headers = PRIVATE_HEADERS

    # Make POST request
    try:
        timeout = 5
        response = requests.post(url, data=json_payload, headers=headers, timeout=timeout)

        # Check the response status
        if response.status_code == 200:
            print("POST request successful")
            print("Response:")
            print(response.text)
            return response.status_code
        else:
            print(f"POST request failed with status code {response.status_code}")
            print("Response:")
            print(response.text)
            return response.status_code

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
