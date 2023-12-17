"""PULLS ALL 'TIME' ITEMS FROM THE URL'S JSON"""
import requests

def get_time_items(target_date, num_players, booking_class, schedule_id):
    """PULLS ALL 'TIME' ITEMS FROM THE URL'S JSON"""

    # Formats URL to be used
    base_url = "https://foreupsoftware.com/index.php/api/booking/times?time=all"
    url = (f"{base_url}&date={target_date}&holes=18&players={num_players}"+
            f"&booking_class={booking_class}"+
            f"&schedule_id={schedule_id}&schedule_ids%5B%5D={schedule_id}"+
            "&specials_only=0&api_key=no_limits")

    try:
        timeout = 5
        response = requests.get(url, timeout=timeout)

        # Check for successful response (status code 200)
        response.raise_for_status()

        # Parse JSON content
        data = response.json()

        # Filter items with the "time" tag
        time_items = [item['time'] for item in data if 'time' in item]

        return time_items, data

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.RequestException as err:
        print(f"Request Exception: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
