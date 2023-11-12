from django.db import models


class Auctions(models.Model):
    # ## Auctions ##
    auction_uuid = models.CharField(max_length=64)
    # auction_start = models.DateTimeField()
    # # Should be +7 days after auction_start date
    # auction_end = models.DateTimeField()
    # auction_reserve = models.IntegerField(default=0)
    # # fk to bids table ???
    # auction_bids = models.IntegerField(default=0)
    # # fk to comments table ???
    # auction_comments = models.IntegerField(default=0)
    # # fk to auction_watch table ???
    # auction_watchers = models.IntegerField(default=0)
    # # fk to user.username
    # auction_seller = models.IntegerField(default=0)
    # auction_seller_notes = models.TextField(default="No Notes Yet.")
    # # fk to comments table ???
    # auction_bidder_comments = models.IntegerField(default=0)
    # auction_views = models.IntegerField(default=0)
    #
    # # ## BIKE ##
    # # example: 2021
    # bike_year = models.IntegerField(default=1999)
    # # example: SB150
    # bike_model = models.CharField(max_length=32, default=None)
    # # example: Yeti
    # bike_make = models.CharField(max_length=32, default=None)
    #
    # BIKE_TYPES = (
    #     ('Road', 'road'),
    #     ('Cyclocross', 'cx'),
    #     ('Time Trial', 'tt'),
    #     ('MTB Cross Country', 'mtb_xc'),
    #     ('MTB Down Country', 'mtb_dc'),
    #     ('MTB Trail', 'mtb_trail'),
    #     ('MTB Enduro', 'mtb_enduro'),
    #     ('MTB Downhill', 'mtb_dh'),
    #     ('eBike', 'ebike'),
    # )
    # bike_type = models.CharField(max_length=64, choices=BIKE_TYPES)
    # # fk to user.location
    # bike_location = models.IntegerField(default=0)
    # bike_serial = models.CharField(max_length=64, default=000)
    #
    # bike_description = models.TextField(default="bike_description")
    # bike_highlights = models.TextField(default="bike_highlights")
    # bike_modifications = models.TextField(default="bike_modifications")
    # bike_known_flaws = models.TextField(default="bike_known_flaws")
    # bike_seller_history = models.TextField(default="bike_seller_history")
    # bike_service_history = models.TextField(default="bike_service_history")
    # bike_video_url = models.TextField(default="bike_video_url")

    def __str__(self):
        return self.auction_uuid


class Comments(models.Model):
    # auction_id = models.IntegerField()
    # comment_id = models.IntegerField()
    # comment_from_seller = models.BooleanField(default=False)
    # comment_is_bid = models.BooleanField(default=False)
    # comment_votes = models.IntegerField()
    # flagged_comment = models.BooleanField(default=False)
    # comment_datetime = models.DateTimeField(auto_now=True)
    comment_text = models.TextField()

    def __str__(self):
        return self.comment_text


class Bids(models.Model):
    # auction_id = models.IntegerField()
    # user_id = models.IntegerField()
    bid_amount = models.CharField(max_length=64)
    # bid_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.bid_amount
