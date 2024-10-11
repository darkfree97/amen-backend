from adrf.viewsets import ModelViewSet

from .models import Publication
from .serializers import PublicationSerializer


class PublicationViewSet(ModelViewSet):
    serializer_class = PublicationSerializer
    queryset = Publication.objects.order_by('-date')
