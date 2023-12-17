import datetime
import time
import pytz

def wait_until(target, timeout_minutes):
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
