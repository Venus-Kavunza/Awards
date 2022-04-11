from django.test import TestCase
from .models import Posts, Ratings
from django.contrib.auth.models import User

# Create your tests here.
class PostsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='venus', email="venus@gmail.com")
        self.post = Posts.objects.create(title='Django', photo='img.png', description='first project test',
                                        user=self.user, url="http://django.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))
    def test_save_post(self):
        self.post.save_post()
        post = Posts.objects.all()
        self.assertTrue(len(post) > 0)        
        
    def test_search_post(self):
        self.post.save()
        post = Posts.search_project('Django')
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Posts.all_posts()
        self.assertTrue(len(posts) > 0)

    def test_delete_post(self):
        self.post.delete_post()
        post = Posts.search_project('Django')
        self.assertTrue(len(post) < 1)