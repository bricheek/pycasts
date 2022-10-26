from time import timezone
from django.test import TestCase

from django.utils import timezone
from.models import Episode

class PodcastsTests(TestCase):
    def setUp(self):
        self.episode = Episode.objects.create(
            title="My Awesome Podcast Episode",
            description="Look mom, I made it!",
            pub_date=timezone.now(),
            link="https://myawesomeshow.com",
            podcast_name="My Python Podcast",
            guid="de194720-7b4c-49e2-a05f-432436d3fetr"
        )
        self.episode.save()
    
    def test_episode_content(self):
        self.assertEqual(self.episode.description, "Look mom, I made it!")
        self.assertEqual(self.episode.link, "https://myawesomeshow.com")
        self.assertEqual(self.episode.guid, "de194720-7b4c-49e2-a05f-432436d3fetr")

    def test_episode_str_representation(self):
        self.assertEqual(str(self.episode), "My Python Podcast: My Awesome Podcast Episode")

    def test_homepage_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "homepage.html")

    def test_homepage_list_contents(self):
        response = self.client.get("/")
        print(response.content)
        self.assertContains(response, "My Awesome Podcast Episode")
