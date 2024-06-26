from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from user_app.api.serializers import RegistrationSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logout_view(request):

    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            account = serializer.save()
            response_data = serializer.data
            response_data['id'] = account.id
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)


# @api_view(['GET'])
# def get_user_details(request, id):
#     try:
#         user = User.objects.get(pk=id)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     serializer = UserSerializer(user)
#     return Response(serializer.data)

# @api_view(['PUT', 'PATCH'])
# @permission_classes([IsAuthenticated])
# def update_user(request, id):
#     try:
#         user = User.objects.get(pk=id)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = UserSerializer(user, data=request.data)
#     else:  # PATCH
#         serializer = UserSerializer(user, data=request.data, partial=True)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# @permission_classes([IsAuthenticated])
# def delete_user(request, id):
#     try:
#         user = User.objects.get(pk=id)
#     except User.DoesNotExist:
#         return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)  

#     user.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        try:
            return self.retrieve(request, *args, **kwargs)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        self.partial = False
        try:
            return self.update(request, *args, **kwargs)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, *args, **kwargs):
        self.partial = True
        try:
            return self.update(request, *args, **kwargs)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            user = self.get_object()
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
