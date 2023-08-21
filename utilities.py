import os
import math
import tempfile
from datetime import datetime, timezone
import pytz

CLIENT_ID = "173067898019-9clcusn9ljf933e597k1aorar5jirlor.apps.googleusercontent.com"
CLIENT_SECRET = "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"
REDIRECT_URI = "https://linkpay.to/login/callback"

MAX_DEPTH = 3
# Function to convert bytes to a human-readable format


def get_user_profile(service):
    profile = service.people().get(resourceName="people/me",
                                   personFields="names,emailAddresses").execute()
    user_name = profile["names"][0]["displayName"]
    user_email = profile["emailAddresses"][0]["value"]
    return user_name, user_email


def convert_size(size_bytes):
    if size_bytes == "N/A" or size_bytes is None:
        return "N/A"

    try:
        size_bytes = int(size_bytes)
    except ValueError:
        return "N/A"

    if size_bytes == 0:
        return "0B"

    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"
