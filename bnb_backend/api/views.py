from random import randrange
from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import AuctionsSerializer, CommentsSerializer, BidsSerializer
from .models import Auctions, Comments, Bids


# /index shows a random quote
def index(request):
    context = {'quote': 'Hello World'}
    return render(request, 'api/index.html', context)


class AuctionsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Auctions to be viewed or edited.
    """
    queryset = Auctions.objects.all()
    serializer_class = AuctionsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CommentsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Comments to be viewed or edited.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [permissions.IsAuthenticated]


class BidsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Bids to be viewed or edited.
    """
    queryset = Bids.objects.all()
    serializer_class = BidsSerializer
    permission_classes = [permissions.IsAuthenticated]
