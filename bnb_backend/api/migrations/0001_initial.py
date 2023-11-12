# Generated by Django 3.2.8 on 2021-10-12 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auctions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_uuid', models.CharField(max_length=64)),
                ('auction_start', models.DateTimeField()),
                ('auction_end', models.DateTimeField()),
                ('auction_reserve', models.IntegerField(max_length=32)),
                ('auction_bids', models.IntegerField(max_length=2)),
                ('auction_comments', models.IntegerField(max_length=2)),
                ('auction_watchers', models.IntegerField(max_length=2)),
                ('auction_seller', models.IntegerField(max_length=2)),
                ('auction_seller_notes', models.TextField()),
                ('auction_bidder_comments', models.IntegerField(max_length=2)),
                ('auction_views', models.IntegerField(max_length=4)),
                ('bike_year', models.IntegerField(max_length=4)),
                ('bike_model', models.CharField(max_length=32)),
                ('bike_make', models.CharField(max_length=32)),
                ('bike_type', models.CharField(max_length=32)),
                ('bike_location', models.IntegerField(max_length=2)),
                ('bike_serial', models.CharField(max_length=64)),
                ('bike_description', models.TextField()),
                ('bike_highlights', models.TextField()),
                ('bike_modifications', models.TextField()),
                ('bike_known_flaws', models.TextField()),
                ('bike_seller_history', models.TextField()),
                ('bike_service_history', models.TextField()),
                ('bike_video_url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Bids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.IntegerField(max_length=2)),
                ('user_id', models.IntegerField(max_length=2)),
                ('bid_amount', models.IntegerField(max_length=32)),
                ('bid_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auction_id', models.IntegerField(max_length=2)),
                ('comment_id', models.IntegerField(max_length=2)),
                ('comment_from_seller', models.BooleanField(default=False)),
                ('comment_is_bid', models.BooleanField(default=False)),
                ('comment_votes', models.IntegerField(max_length=4)),
                ('flagged_comment', models.BooleanField(default=False)),
                ('comment_datetime', models.DateTimeField(auto_now=True)),
                ('comment_text', models.TextField()),
            ],
        ),
    ]
