from django.db import models
from datetime import datetime, date

TASK_STATUS = (
  ('complete', 'complete'),
  ('uncomplete', 'uncomplete')
)

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    status = models.CharField(max_length=255, choices=TASK_STATUS, default='uncomplete')
    public_date = models.DateField(default=date.today)

    def __str__(self):
        return self.title + " <object id:" + str(self.id) + ">"