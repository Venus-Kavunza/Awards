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

class UserProfileTest(TestCase):
    def setUp(self):
        self.user = User(username='venus', email='venus@gmail.com', password='newpassword')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()

class RatingsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='venus', email="venus@gmail.com")
        self.post = Posts.objects.create(title='Django', photo='img.png', description='first project test',
                                        user=self.user, url="http://django.com")
        self.rating = Ratings.objects.create(design=9, usability=10, content=5, user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Ratings))
    def test_save_ratings(self):
        self.rating.save_rating()
        rating = Ratings.objects.all()
        self.assertTrue(len(rating) > 0)        

    