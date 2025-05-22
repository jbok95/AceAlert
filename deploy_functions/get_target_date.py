"""RETURNS DATE OF THE NEWLY RELEASED TEE TIME IN CORRECT FORMAT"""

def get_target_date_payload(target_date):
    """RETURNS DATE OF THE NEWLY RELEASED TEE TIME IN CORRECT FORMAT FOR THE PAYLOAD"""
    try:
        payload_date = target_date[6:] + "-" + target_date[:2] + "-" + target_date[3:5]
        return payload_date

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
