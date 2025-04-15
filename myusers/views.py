from django.shortcuts import get_object_or_404
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsersViewset(APIView):
    def get(self, request, id=None):
        if id:
            user = models.Users.objects.get(id=int(id))
            serializer = serializers.UsersSerializer(user)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        users = models.Users.objects.all()
        serializer = serializers.UsersSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = serializers.UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        if id is None:
            return Response({"status": "error", "message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(models.Users, id=int(id))
        serializer = serializers.UsersSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "error", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is None:
            return Response({"status": "error", "message": "User ID is required."}, status=status.HTTP_400_BAD_REQUEST)
        user = get_object_or_404(models.Users, id=int(id))
        user.delete()
        return Response({"status": "success", "data": "User Deleted"})