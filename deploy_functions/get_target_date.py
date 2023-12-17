"""RETURNS DATE OF THE NEWLY RELEASED TEE TIME IN CORRECT FORMAT"""
from datetime import datetime, timedelta
import pytz

def get_target_date_url():
    """RETURNS DATE OF THE NEWLY RELEASED TEE TIME IN CORRECT FORMAT FOR THE URL"""
    try:
        # Get the current date
        my_tz = pytz.timezone('US/Eastern')
        today = datetime.now(my_tz)

        # Get the target date (one week from today)
        target_date = today + timedelta(days=7)

        # Format the date as 'mm-dd-yyyy'
        formatted_date = target_date.strftime('%m-%d-%Y')

        return formatted_date

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_target_date_payload():
    """RETURNS DATE OF THE NEWLY RELEASED TEE TIME IN CORRECT FORMAT FOR THE PAYLOAD"""
    try:
        # Get the current date
        today = datetime.today()

        # Get the target date (one week from today)
        target_date = today + timedelta(days=7)

        # Format the date as 'mm-dd-yyyy'
        formatted_date = target_date.strftime('%Y-%m-%d')

        return formatted_date

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
