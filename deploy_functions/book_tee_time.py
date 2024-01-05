"""BOOKS TEE TIME FOR NEWLY AVAILABLE TIME"""
from datetime import datetime
import json
import requests

from config import PRIVATE_HEADERS, PRIVATE_PAYLOAD

def generate_payload(date_time):#(data, optimal_date_time):
    """RETURNS FULL PAYLOAD FOR THE OPTIMAL TIME FOUND"""
    # initial_payload = [entry for entry in data if entry.get("time") == optimal_date_time]

    dt_object = datetime.strptime(date_time, "%Y-%m-%d %H:%M")
    formatted_date = dt_object.strftime("%d%H%M")

    my_payload = PRIVATE_PAYLOAD
    my_payload["time"] = date_time
    my_payload["start_front"] = int("202311"+formatted_date)


    # my_payload = {
    #     "time": date_time,
    #     "start_front": int("202311"+formatted_date),
    #     "course_id": 19671,
    #     "course_name": "Mangrove Bay",
    #     "schedule_id": 2149,
    #     "teesheet_id": 2149,
    #     "schedule_name": "Mangrove Bay",
    #     "require_credit_card": False,
    #     "teesheet_holes": 18,
    #     "teesheet_side_id": 3416,
    #     "teesheet_side_name": " ",
    #     "teesheet_side_order": 1,
    #     "reround_teesheet_side_id": 3417,
    #     "reround_teesheet_side_name": " ",
    #     "available_spots": 4,
    #     "available_spots_9": 0,
    #     "available_spots_18": 4,
    #     "maximum_players_per_booking": "4",
    #     "minimum_players": "2",
    #     "allowed_group_sizes": [
    #         "2",
    #         "3",
    #         "4"
    #     ],
    #     "holes": "18",
    #     "has_special": False,
    #     "special_id": False,
    #     "special_discount_percentage": 0,
    #     "group_id": False,
    #     "booking_class_id": 12239,
    #     "booking_fee_required": False,
    #     "booking_fee_price": False,
    #     "booking_fee_per_person": False,
    #     "foreup_trade_discount_rate": 0,
    #     "trade_min_players": 8,
    #     "trade_available_players": 0,
    #     "green_fee_tax_rate": False,
    #     "green_fee_tax": 0,
    #     "green_fee_tax_9": 0,
    #     "green_fee_tax_18": 0,
    #     "guest_green_fee_tax_rate": False,
    #     "guest_green_fee_tax": 0,
    #     "guest_green_fee_tax_9": 0,
    #     "guest_green_fee_tax_18": 0,
    #     "cart_fee_tax_rate": False,
    #     "cart_fee_tax": 0,
    #     "cart_fee_tax_9": 0,
    #     "cart_fee_tax_18": 0,
    #     "guest_cart_fee_tax_rate": False,
    #     "guest_cart_fee_tax": 0,
    #     "guest_cart_fee_tax_9": 0,
    #     "guest_cart_fee_tax_18": 0,
    #     "foreup_discount": False,
    #     "pay_online": "no",
    #     "green_fee": 35.5,
    #     "green_fee_9": 0,
    #     "green_fee_18": 35.5,
    #     "guest_green_fee": 35.5,
    #     "guest_green_fee_9": 0,
    #     "guest_green_fee_18": 35.5,
    #     "cart_fee": 0,
    #     "cart_fee_9": 0,
    #     "cart_fee_18": 0,
    #     "guest_cart_fee": 0,
    #     "guest_cart_fee_9": 0,
    #     "guest_cart_fee_18": 0,
    #     "rate_type": "riding",
    #     "special_was_price": None, #THIS IS WHERE IT ENDS
    #     "players": "4",
    #     "carts": True,
    #     "promo_code": "",
    #     "promo_discount": 0,
    #     "player_list": True,
    #     "duration": 1,
    #     "notes": [],
    #     "customer_message": "",
    #     "total": 142,
    #     "purchased": False,
    #     "pay_players": "4",
    #     "pay_carts": True,
    #     "pay_total": 142,
    #     "pay_subtotal": 142,
    #     "paid_player_count": 0,
    #     "discount_percent": 0,
    #     "discount": 0,
    #     "details": "",
    #     "pending_reservation_id": "TTID_1208141544a7gz5",
    #     "allow_mobile_checkin": 0,
    #     "foreup_trade_discount_information": [],
    #     "airQuotesCart": [
    #         {
    #         "type": "item",
    #         "description": "Green Fee",
    #         "price": 35.5,
    #         "quantity": 4,
    #         "subtotal": 142
    #         }
    #     ],
    #     "preTaxSubtotal": 142,
    #     "estimatedTax": 0,
    #     "subtotal": 142,
    #     "available_duration": None,
    #     "increment_amount": None,
    #     "availableHoles": "18",
    #     "blockReservationDueToExistingReservation": False
    # }

    return my_payload


def book_tee_time(payload):
    """BOOKS TEE TIME"""

    url = "https://foreupsoftware.com/index.php/api/booking/users/reservations"
    # Convert JSON dictionary to a string
    json_payload = json.dumps(payload)
    # print(json_payload)

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
