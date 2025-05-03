from rest_framework.views import APIView
from users.serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework import status

class CreateCustomUserView(APIView):
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
