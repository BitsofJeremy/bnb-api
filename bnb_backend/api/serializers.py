from rest_framework import serializers
from .models import Auctions, Comments, Bids


class AuctionsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Auctions
        # fields = '__all__'
        fields = ['auction_uuid']


class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comments
        # fields = '__all__'
        fields = ['comment_text']


class BidsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bids
        # fields = '__all__'
        fields = ['bid_amount']
