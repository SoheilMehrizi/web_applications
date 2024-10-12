from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import Profile

#getting user model

User = get_user_model()

class Post(models.Model):
    """
    This is a class to define Post table structure for blog app 
    """
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    category = models.ForeignKey("category", on_delete=models.SET_NULL, null=True, default=None)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    def get_snippet(self):
        """
        Returns a Brief summery of posts content field , # this field is readonly
        """
        return self.content[0:5]
    
    def get_absolute_api_url(self):
        return reverse('blog:api-v5:post-detail', kwargs={'pk': self.pk})

class category(models.Model):
    """
    this is a class to define categories of posts for blog app.
    """
    name = models.CharField(max_length = 25)
    
    def __str__(self):
        return self.name
    

