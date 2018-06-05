from django.db import models

# Create your models here.
from django.db import models


class Question(models.Model):#has pub date and question text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):#choice is associated with a quetsion
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)#correlated to question
    def __str__(self):
        return self.choice_text
