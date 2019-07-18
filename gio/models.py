from django.db import models
from geoposition.fields import GeopositionField
from simple_history.models import HistoricalRecords
from django.conf import settings

User = settings.AUTH_USER_MODEL

class PointOfInterest(models.Model):
    name = models.CharField(max_length=100)
    position = GeopositionField()


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    changed_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    history = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    history = HistoricalRecords()