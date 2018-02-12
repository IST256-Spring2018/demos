import datetime
import math
import requests
import json


def get_steps():
    accesstoken = input("Please enter you access token")
    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"
    today = datetime.date.today()
    today_ms = math.ceil(datetime.datetime(today.year, today.month, today.day).timestamp() * 1000)
    now_ms = math.ceil(datetime.datetime.today().timestamp() * 1000)

    params = {
    "aggregateBy": [
    {
    "dataTypeName": "com.google.step_count.delta",
    "dataSourceId": "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"
    }
    ],
    "endTimeMillis": str(now_ms),
    "startTimeMillis": str(today_ms),
    "bucketByTime": {
    "durationMillis": "86400000"
    }
    }

    headers = {
        "Authorization": "Bearer " + accesstoken,
        "Content-Type": "application/json; charset=UTF-8"
    }

    response = requests.post(url, data=json.dumps(params), headers=headers)
    data = response.json()

    steps = data["bucket"][0]["dataset"][0]["point"][0]["value"][0]["intVal"]

    return steps