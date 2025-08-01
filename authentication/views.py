from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserModelSerializer


class CreateUserView(APIView):
    def post(self, request):
        serializer = UserModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"ok": True}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
