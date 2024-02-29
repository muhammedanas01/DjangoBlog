from django.db import models
from ckeditor.fields import RichTextField 


class Blog(models.Model):
    name = models.CharField(max_length = 100, default ="")
    title = models.CharField(max_length = 100 )
    id = models.AutoField(primary_key=True)
    short_desc = models.CharField(max_length = 200)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to="blogimages", null=False, blank=True)
    created_at = models.TimeField(auto_now_add = True)


    def __str__(self) -> str:
        return self.name
    
class Comment(models.Model):
    name = models.CharField(max_length=100, default ="")
    blogparent = models.ForeignKey(Blog,on_delete=models.CASCADE)
    Comment = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    cid = models.IntegerField(null = True)

    def __str__(self) -> str:
        return self.name
    
class Reply(models.Model):
    name = models.CharField(max_length = 100, default = "")
    commentparent = models.ForeignKey(Comment, on_delete = models.CASCADE)
    reply = models.TextField()
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name
