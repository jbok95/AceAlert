"""RETURNS FILTERED TIMES FROM A LIST THAT ARE LESS THAN A SPECIFIED TIME"""
import math
from datetime import datetime

def filter_times(time_list, latest_time):
    """RETURNS FILTERED TIMES FROM A LIST THAT ARE LESS THAN A SPECIFIED TIME"""
    try:
        # Convert each time string to a datetime object
        times_as_datetime = [datetime.strptime(time_str, '%H:%M') for time_str in time_list]

        # Filter times that are earlier than latest_time
        filtered_times = [time.strftime('%H:%M') for time in times_as_datetime
                          if time.time() <= datetime.strptime(latest_time, '%H:%M').time()]

        return filtered_times

    except ValueError as value_err:
        print(f"ValueError: {value_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def best_time(filtered_times):
    """RETURNS THE MIDDLE OF THE AVAILABLE TEE TIMES LIST"""

    try:
        best_tee_time_location = math.floor(max(len(filtered_times)/2,0))
        best_tee_time = filtered_times[best_tee_time_location]
        return best_tee_time

    except ValueError as value_err:
        print(f"ValueError: {value_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
