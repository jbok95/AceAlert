"""STRIPS AND CONVERTS A LIST OF TIMEs FROM FORMAT MM-DD-YYYY HH-MM TO HH-MM"""
from datetime import datetime

def convert_times(time_items):
    """STRIPS AND CONVERTS A LIST OF TIMES FROM FORMAT MM-DD-YYYY HH-MM TO HH-MM"""
    try:
        # Parse and format each time in the list
        formatted_times = [datetime.strptime(time_str, '%Y-%m-%d %H:%M').
                           strftime('%H:%M') for time_str in time_items]

        return formatted_times

    except ValueError as value_err:
        print(f"ValueError: {value_err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
