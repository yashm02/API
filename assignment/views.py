from rest_framework import generics
from .models import Work, Artist
from .serializers import WorkSerializer, ArtistSerializer

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
