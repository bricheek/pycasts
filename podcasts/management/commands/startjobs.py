from django.core.management.base import BaseCommand
import feedparser
from dateutil import parser
from time import pytz
import ssl
from podcasts.models import Episode

class Command(BaseCommand):
    def handle(self, *args, **options):
        ssl._create_default_https_context=ssl._create_unverified_context
        #rss_feed = feedparser.parse("https://dataskeptic.libsyn.com/rss")
        d = feedparser.parse("https://realpython.com/podcasts/rpp/feed")
        podcast_title = d.feed.title
        podcast_image = d.feed.image['href']

        for entry in d.entries:
            if not Episode.objects.filter(guid='guid').exists():
                episode = Episode(
                    title='title',
                    description='description',
                    pub_date=timezone.now(),
                    #pub_date=parser.parse('published', fuzzy = True),
                    #pub_date="2020-08-10 10:10:10.000111 EST",
                    image=podcast_image,
                    podcast_name=podcast_title,
                    guid='guid',
                    )
                episode.save()
               
