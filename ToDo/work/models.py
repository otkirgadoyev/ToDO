from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Todo(models.Model):
    COLORS=(
       ('blue','blue'),
       ('red','red'),
       ('yellow','yellow'),
       ('orange','orange'),
       ('pink','pink'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=500,blank=False,null=True)
    color=models.CharField(max_length=20,blank=False,choices=COLORS,null=True)
    is_completed = models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(default=datetime.now(), null=True, blank=True)

    def __str__(self):
        return self.name
