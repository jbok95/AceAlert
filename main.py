"""Tee time booker that is compatible with Google Cloud"""

import json
from deploy_functions.book_tee_time import book_tee_time, generate_payload
from deploy_functions.get_target_date import get_target_date_payload
from deploy_functions.get_time_items import get_time_items
from deploy_functions.convert_times import convert_times
from deploy_functions.filter_times import filter_times, best_time

def ace_alert_scraper(request):
    """
    FINDS THE BEST AVAILABLE TEE TIME AT MANGROVE BAY 
    ONE WEEK OUT AND BOOKS THAT TEE TIME
    """

    # If request from local
    if isinstance(request, str):
        request_json = json.loads(request)

    # If request is from Google Cloud
    else:
        request_json = request.get_json()

    # Pulls specified times from Cloud Scheduler
    target_date = request_json.get('target_date')
    preferred_tee_time = request_json.get('preferred_tee_time')
    max_tee_time = request_json.get('max_tee_time')

    # Tries to book the target tee time first
    first_try = get_target_date_payload(target_date) + " "+preferred_tee_time
    my_payload = generate_payload(first_try)
    my_success = book_tee_time(my_payload)

    if my_success != 200:

        # Returns the date in correct format for one week from the day
        url_target_date = target_date

        # Pulls all times currently available in format mm-dd-yyyy hh:mm from the URL
        num_players = 4
        booking_class = 12239
        schedule_id = 2149

        time_items = get_time_items(url_target_date, num_players, booking_class, schedule_id)

        # Formats times to hh:mm
        formatted_times = convert_times(time_items)

        if formatted_times:
            print(formatted_times)
        else:
            print("No times to convert.")

        # Filters list of times to only times within target range
        filtered_times = filter_times(formatted_times, max_tee_time)

        if filtered_times:
            print(f"Times earlier than {max_tee_time}: {filtered_times}")

            # Finds best available tee time from filtered list
            optimal_time = best_time(filtered_times)
            print(optimal_time)

            # If tee time is available, then books tee time
            payload_date_time = get_target_date_payload(target_date) + " " + optimal_time
            my_payload = generate_payload(payload_date_time)
            book_tee_time(my_payload)
        else:
            print(f"No times found earlier than {max_tee_time}.")

    return "Success!"

if __name__ == "__main__":
    my_request = {
        "target_date": "02-18-2024",
        "preferred_tee_time": "8:37",
        "max_tee_time": "10:00"
        }
    json_request = json.dumps(my_request)
    ace_alert_scraper(json_request)
