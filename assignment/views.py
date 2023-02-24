from rest_framework import generics
from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

class WorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        work_type = self.request.query_params.get('work_type', None)
        if work_type is not None:
            queryset = queryset.filter(work_type=work_type)
        return queryset

class ArtistList(generics.ListAPIView):
    serializer_class = ArtistSerializer
    queryset = Artist.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        artist_name = self.request.query_params.get('artist', None)
        if artist_name is not None:
            queryset = queryset.filter(name__icontains=artist_name)
        return queryset

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Both username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        User.objects.create_user(username=username, password=password)
        return Response({'success': 'User created successfully'}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
