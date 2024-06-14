from django.db import models
from userauths.models import User, Profile, user_directory_path
from django.utils.text import slugify
from django.utils.safestring import mark_safe

from shortuuid.django_fields import ShortUUIDField
import shortuuid
# Create your models here.


VISIBILITY = (
    ("Only Me", "Only Me"),
    ("Everyone" , "Everyone"),
)

FRIEND_REQUEST = (
    ("pending", "pending"),
    ("accept","accept"),
    ("reject", "reject"),
)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 500, blank = True, null = True)
    image = models.ImageField(upload_to=user_directory_path, blank = True, null = True)
    video = models.FileField(upload_to=user_directory_path, blank = True, null = True)
    visibility = models.CharField(max_length=100, choices = VISIBILITY, default = "Everyone")
    pid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    likes = models.ManyToManyField(User, blank=True, related_name = "likes")
    active = models.BooleanField(default = True)
    slug = models.SlugField(unique= True)
    views = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:2]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + '-' + uniqueid
        super(Post, self).save(*args, **kwargs)


    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))
    

    def post_comments(self):
        comments = Comment.objects.filter(post = self, active = True).order_by("-id")
        return comments
    

class Gallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to = "gallery", null = True, blank = True)
    active = models.BooleanField(default = True)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return str(self.post)
    
    class Meta:
        verbose_name_plural = 'Gallery'

    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))
    




class FriendRequest(models.Model):
    fid = ShortUUIDField(length = 7, max_length = 25, alphabet = "abcdefghijklmnopqrstuvwxyz")
    sender = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "sender")
    receiver = models.ForeignKey(User, on_delete = models.CASCADE, related_name= "receiver")
    status = models.CharField(max_length = 100, default= "pending", choices = FRIEND_REQUEST)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.sender)
    
    class Meta: 
        verbose_name_plural = 'Friend Request'





class Friend(models.Model):
    fid = ShortUUIDField(length = 7, max_length = 25, alphabet = "abcdefghijklmnopqrstuvwxyz")
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name = "user")
    friend = models.ForeignKey(User, on_delete = models.CASCADE, related_name= "friend")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user)
    
    class Meta: 
        verbose_name_plural = 'Friend'



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "comment_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length = 1000)
    active = models.BooleanField(default = True)
    date = models.DateTimeField(auto_now_add= True)
    likes = models.ManyToManyField(User, blank = True, related_name= "comment_likes")
    cid = ShortUUIDField(length = 7, max_length= 25, alphabet = "abcdefghijklmnopqrstuvwxyz")

    def __str__(self):
        return str(self.post)
    
    class Meta: 
        verbose_name_plural = 'Comment'

    def comment_replies(self):
        comment_replies = ReplyComment.objects.filter(comment = self, active = True)
        return comment_replies



class ReplyComment(models.Model):
    user = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "reply_user")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reply = models.CharField(max_length = 1000)
    active = models.BooleanField(default = True)
    date = models.DateTimeField(auto_now_add= True)
    cid = ShortUUIDField(length = 7, max_length= 25, alphabet = "abcdefghijklmnopqrstuvwxyz")

    def __str__(self):
        return str(self.comment)
    
    class Meta: 
        verbose_name_plural = 'Reply Comment'



class Group(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "group_user")
    members =models.ManyToManyField(User,  related_name = "group_members")
    image = models.ImageField(upload_to=user_directory_path, blank = True, null = True)
    name  = models.CharField(max_length = 500, blank = True, null = True)
    description  = models.TextField(max_length = 500, blank = True, null = True)
    
    video = models.FileField(upload_to=user_directory_path, blank = True, null = True)
    visibility = models.CharField(max_length=100, choices = VISIBILITY, default = "Everyone")
    gid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    active = models.BooleanField(default = True)
    slug = models.SlugField(unique= True)
    views = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.name:
            return self.name 
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:2]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + '-' + uniqueid
        super(Group, self).save(*args, **kwargs)


    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))




class GroupPost(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 500, blank = True, null = True)
    image = models.ImageField(upload_to=user_directory_path, blank = True, null = True)
    video = models.FileField(upload_to=user_directory_path, blank = True, null = True)
    visibility = models.CharField(max_length=100, choices = VISIBILITY, default = "Everyone")
    pid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    likes = models.ManyToManyField(User, blank=True, related_name = "group_post_likes")
    active = models.BooleanField(default = True)
    slug = models.SlugField(unique= True)
    views = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:2]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + '-' + uniqueid
        super(GroupPost, self).save(*args, **kwargs)


    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))
    




class Page(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "page_user")
    members =models.ManyToManyField(User, related_name = "page_members")
    image = models.ImageField(upload_to=user_directory_path, blank = True, null = True)
    name  = models.CharField(max_length = 500, blank = True, null = True)
    description  = models.TextField(max_length = 500, blank = True, null = True)
    
    video = models.FileField(upload_to=user_directory_path, blank = True, null = True)
    visibility = models.CharField(max_length=100, choices = VISIBILITY, default = "Everyone")
    pid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    active = models.BooleanField(default = True)
    slug = models.SlugField(unique= True)
    views = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.name:
            return self.name 
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:2]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + '-' + uniqueid
        super(Page, self).save(*args, **kwargs)


    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))






class PagePost(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 500, blank = True, null = True)
    image = models.ImageField(upload_to=user_directory_path, blank = True, null = True)
    video = models.FileField(upload_to=user_directory_path, blank = True, null = True)
    visibility = models.CharField(max_length=100, choices = VISIBILITY, default = "Everyone")
    pid = ShortUUIDField(length = 7, max_length=25, alphabet = 'abcdefghijklmnopqrstuvwxyz')
    likes = models.ManyToManyField(User, blank=True, related_name = "page_post_likes")
    active = models.BooleanField(default = True)
    slug = models.SlugField(unique= True)
    views = models.PositiveIntegerField(default = 0)
    date = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.user.username
        
    def save(self, *args, **kwargs):
        uuid_key = shortuuid.uuid()
        uniqueid = uuid_key[:2]
        if self.slug == "" or self.slug == None:
            self.slug = slugify(self.title) + '-' + uniqueid
        super(PagePost, self).save(*args, **kwargs)


    def thumbnail(self):
        return mark_safe('<img src ="/media/%s" width = "50" height = "50" object-fit:"cover" style = "border-radius: 5px;" /> '  % (self.image))
    


    