from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from shortuuid.django_fields import ShortUUIDField
from django.db.models.signals import post_save
from django.utils.text import slugify
import shortuuid

# Create your models here.

GENDER = (
    ("male", "Male"),
    ("female", "Female")
)

RELATIONSHIP = (
    ("single", "Single"),
    ("married", "Married")
)


def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, ext),
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class User(AbstractUser):
    full_name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length=200)
    gender = models.CharField(max_length=100, choices = GENDER)

    otp = models.CharField(max_length=10, null = True, blank = True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    



class Profile(models.Model):
    pid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cover_image = models. ImageField(upload_to = user_directory_path, blank= True, null = True,default = "cover.jpg")
    image = models.ImageField(upload_to = user_directory_path, blank= True, null = True, default = "default.png")
    full_name = models.CharField(max_length=200, null= True, blank = True)
    phone = models.CharField(max_length=200, null = True, blank = True)
    gender = models.CharField(max_length=100, choices = GENDER, default = "male")
    relationship = models.CharField(max_length=100, choices=RELATIONSHIP, default = "single")
    bio = models.CharField(max_length=200, null = True, blank = True)
    about_me = models.TextField(null = True, blank = True)
    country = models.CharField(max_length=200, null = True, blank = True)
    state = models.CharField(max_length=200, null = True, blank = True)
    city = models.CharField(max_length=200, null = True, blank = True)
    address = models.CharField(max_length=200, null = True, blank = True)
    working_at = models.CharField(max_length=200, null = True, blank = True)
    instagram = models.CharField(max_length=200, null = True, blank = True)
    whatsapp = models.CharField(max_length=200, null = True, blank = True)
    verified = models.BooleanField(default = False)
    followers =models.ManyToManyField(User, null = True, blank = True, related_name = "followers")
    following =models.ManyToManyField(User, null = True, blank = True, related_name = "following")
    friends =models.ManyToManyField(User, null = True, blank = True, related_name = "friends")
    blocked = models.ManyToManyField(User, null = True, blank = True, related_name = "blocked")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique = True, null = True, blank = True)

    def __str__(self):
        return self.user.username
    
    def save(self, *args, **kwargs):
        if self.slug == "" or self.slug == None:
            uuid_key = shortuuid.uuid()
            uniqueid = uuid_key[:2]
            self.slug = slugify(self.full_name)+ '-'+ str(uniqueid.lower())
        super(Profile, self).save(*args, **kwargs)




def create_user_profile(sender, instance, created, **Kwargs):
    if created:
        Profile.objects.create(user = instance)


def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(create_user_profile, sender = User)
post_save.connect(save_user_profile, sender = User)










