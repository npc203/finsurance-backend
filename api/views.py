from django.shortcuts import render

from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from datetime import datetime, timezone
import requests


@api_view(["GET", "POST"])
def index(request):
    return Response(request.session.get("USER_ID", "Not found"), status=status.HTTP_200_OK)


@api_view(["GET"])
def callback(request):
    return Response("sussy baka", status=status.HTTP_200_OK)


@api_view(["POST"])
def auth(request):
    request.session["USER_ID"] = "sussy baka1"
    cur_date = datetime.now(timezone.utc).isoformat()
    cur_date = cur_date.rsplit(".", 1)
    cur_date = f"{cur_date[0]}.{cur_date[1][:3]}Z"

    url = "https://fiu-uat.setu.co/consents"

    headers = {
        "x-client-id": "e4a41785-973f-474c-ac13-0b149a8728aa",
        "x-client-secret": "da2bb980-b634-44a9-adf6-6df2991db3e7",
    }

    data = {
        "Detail": {
            "consentStart": cur_date,
            "consentExpiry": "2022-04-23T05:44:53.822Z",
            "Customer": {"id": "7092128101@onemoney"},
            "FIDataRange": {"from": "2021-04-01T00:00:00Z", "to": "2021-10-01T00:00:00Z"},
            "consentMode": "STORE",
            "consentTypes": ["TRANSACTIONS", "PROFILE", "SUMMARY"],
            "fetchType": "ONETIME",
            "Frequency": {"value": 30, "unit": "MONTH"},
            "DataLife": {"value": 1, "unit": "MONTH"},
            "DataConsumer": {"id": "setu-fiu-id"},
            "Purpose": {
                "Category": {"type": "string"},
                "code": "102",
            },
            "fiTypes": ["DEPOSIT"],
        },
        "redirectUrl": "http://localhost:3000",
    }

    # response = requests.post(url, headers=headers, json=data)

    # raw_data = response.json()
    # url = raw_data["url"]
    url = "balls"
    return Response(url, status=status.HTTP_200_OK)
