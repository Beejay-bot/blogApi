from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
# Create your views here.
from .serializers import RegisterUserSerializer

class CustomUserCreate(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        req_serializer = RegisterUserSerializer(data=request.data)
        if req_serializer.is_valid():
            newuser = req_serializer.save()
            if newuser:
                return Response(status=status.HTTP_201_CREATED)
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


