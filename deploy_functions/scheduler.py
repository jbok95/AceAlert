"""
Waits until the specified time that tee times become available
"""
import datetime
import time
import pytz

def wait_until(target, timeout_minutes):
    """
    Waits until specified time to start the program

    Parameters:
    - target (str): target time for when tee times are released in form hh:mm:ss
    - timeout_minutes (int): maximum amount of time to wait before ending function
    - sheet_title (str): name of targeted sheet
    """

    # Set the timezone to Eastern Time
    et_timezone = pytz.timezone('US/Eastern')
    target_hr = int(target[:2])
    target_min = int(target[3:5])
    target_sec = int(target[6:])

    # Get the current time in Eastern Time
    now_et = datetime.datetime.now(et_timezone)

    # Set the desired time
    desired_time = now_et.replace(hour=target_hr, minute=target_min,
                                   second=target_sec, microsecond=0)

    # Calculate the time difference
    time_difference = (desired_time - now_et).total_seconds()

    if time_difference > timeout_minutes * 60:
        print("Timeout reached")
        return
    else:
        # Pause the script until specified time
        print(f"Waiting until {desired_time}. Current time: {now_et}")
        time.sleep(time_difference)
        return
