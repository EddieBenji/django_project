import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # important to add always this method. (kind of similar "to_string", from java)
    def __str__(self):
        return self.question_text

    # this method helps to know if the publication date of a question was yesterday.
    def was_published_recently(self):
        today = timezone.now()
        yesterday = today - datetime.timedelta(days=1)
        return yesterday <= self.pub_date <= today

    was_published_recently.admin_order_field = "pub_date"
    was_published_recently.boolean = True
    was_published_recently.short_description = "Published recently?"


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  # set the default value of votes to 0.

    def __str__(self):
        return self.choice_text
