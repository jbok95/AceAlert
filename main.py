from deploy_functions.book_tee_time import book_tee_time, generate_payload
from deploy_functions.get_target_date import get_target_date_url, get_target_date_payload
from deploy_functions.get_time_items import get_time_items
from deploy_functions.convert_times import convert_times
from deploy_functions.filter_times import filter_times, best_time
from deploy_functions.scheduler import wait_until

def tee_time_booker(request):
    """FINDS THE BEST AVAILABLE TEE TIME AT MANGROVE BAY 
    ONE WEEK OUT AND BOOKS THAT TEE TIME FOR ME"""

    target_start = "06:00:00" #must be in format hh:mm:ss
    timeout_minutes = 5
    # wait_until(target_start, timeout_minutes)

    # Pulls specified times from Cloud Scheduler
    request_json = request.get_json()
    #check if this works
    tgt_time = request_json.get('tgt_time', '08:37')
    max_time = request_json.get('max_time', '10:00')

    # Tries to book the target tee time first
    first_try = get_target_date_payload() + " "+tgt_time #08:37
    my_payload = generate_payload(first_try)
    my_success = book_tee_time(my_payload)

    if my_success != 200:

        # Returns the date in correct format for one week from the day
        url_target_date = get_target_date_url()

        # Pulls all times currently available in format mm-dd-yyyy hh:mm from the URL
        num_players = 4
        booking_class = 12239
        schedule_id = 2149

        time_items, full_data = get_time_items(url_target_date, num_players, booking_class, schedule_id)

        # Formats times to hh:mm
        formatted_times = convert_times(time_items)

        if formatted_times:
            print(formatted_times)
        else:
            print("No times to convert.")

        # Filters list of times to only times within target range
        # max_time = '10:00'
        filtered_times = filter_times(formatted_times, max_time)

        if filtered_times:
            print(f"Times earlier than {max_time}: {filtered_times}")

            # FINDS BEST AVAILABLE TEE TIME FROM THE FILTERED LIST
            optimal_time = best_time(filtered_times)
            print(optimal_time)

            # IF TEE TIME IS AVAILABLE, THEN BOOKS THE TEE TIME
            payload_date_time = get_target_date_payload() + " " + optimal_time
            #my_payload = generate_payload(full_data, payload_date_time)
            my_payload = generate_payload(payload_date_time)
            book_tee_time(my_payload)
        else:
            print(f"No times found earlier than {max_time}.")

    return "Success!"

# if __name__ == "__main__":
#     request = {
#         "tgt_time": "07:45",
#         "max_time": "09:30"
#         }
#     tee_time_booker(request)
