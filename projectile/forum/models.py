from django.db import models
from core.models import User, Country


class Category(models.Model):
    title = models.CharField(max_length=200, unique="true")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Post(models.Model):
    parent = models.ForeignKey('self', on_delete=models.CASCADE),
    category = models.ForeignKey(Category, on_delete=models.CASCADE),
    country = models.ForeignKey(User, on_delete=models.SET_NULL),
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField()
    view_count = models.IntegerField(default=0)
    created_at = models.DateTimeField('date created', auto_now_add=True)
    updated_at = models.DateTimeField('date updated', auto_now=True)

    def increment_views(self):
        self.view_count = self.view_count + 1
        self.save(update_fields=['view_count',])

    def get_latest_response_date():
        return self.get_responses().last().created_at
    
    def get_responses(self):
        return Post.objects.filter(
            parent__id=self.id
        )

    def count_responses(self):
        return self.get_responses().count()

## get_latest_response_date was listed twice in the requirements with different descriptions.