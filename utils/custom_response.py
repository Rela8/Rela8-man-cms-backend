# NOTE this file houses a function that gives Me a well formated Response So Now
# i can update response in one place
from rest_framework.response import Response
from rest_framework import status


def structure_responseDict(msg, status_code, success, data=None):
    "this just returns a structured dictionary which would be used across this app so we wont have to re-righting"

    return {
        "message": msg,
        "status_code": status_code,
        "data": data,
        "success": success
    }


def Success_response(msg, data=None, status_code=status.HTTP_200_OK):
    "anytime this function is called it returns this particular dictionary or error response"

    return Response(data={
        **structure_responseDict(msg, status_code, success=True, data=data)
    })


def Failure_response(msg, status_code=status.HTTP_400_BAD_REQUEST):
    "function for failed requests, default status code of 400"

    return Response(
        data={
            "error": {
                "message": msg,
                "status_code": status_code
            }
        },
        status=status_code
    )
