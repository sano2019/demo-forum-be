from django.db import models
from core.models import User

class Category(models.Model):
    title = models.CharField(max_length=200, unique="true")
    country = models.CharField(max_length=200, unique="true")


class Post(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    country = models.ForeignKey(Category, on_delete=models.CASCADE),
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=1200)
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField('date created')
    updated_at = models.DateTimeField('date updated')

    # def increment_views():

    # def get_latest_response_date():

    # def get_responses():

    # def count_responses():

    # def get_latest_response_date():