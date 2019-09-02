from django.test import TestCase
from .models import Image, Follow, Comments, Profile

# Create your tests here.
class ImageTestCase(TestCase):
    def setUp(self):
        self.image = Image(image_name="Drifting in kenya", image_caption="Test 2", uploaded_by="Daniel", comments="Embu was awesome")

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.image.save_image()
        self.image.delete_image()

class FollowTestCase(TestCase):
    def setUp(self)
        self.follower = Follow(user_id=1, following_id=5)

    def test_instance(self):
        self.assertTrue(isinstance(self.follower, Follow))

class CommentsTestCase(TestCase):
    def setUp(self):
        self.comment = Comments(comment="Likely....", image_id=2)

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comments))
    
class ProfileTestCase(TestCase):
    def setUp(self):
        self.profile = Profile(user_id=1, first_name="Dan", last_name="Njuguna", email="njugunadaniel364@gmail.com", phone="0791293150", bio="Young Wild n Free...")

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    

