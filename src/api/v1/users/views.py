from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def user_hello(request):
    result = {"user": "Hello world"}
    return Response(result)
