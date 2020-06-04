from django.db import models

'''
django model field
        - Html widget
        - validation
        - db size
        - 
'''

# Create your models here.
JOB_TYPE = (
    ('FULL TIME', 'FULL TIME'),
    ('PART TIME', 'PART TIME'),
)


class Job(models.Model):
    title = models.CharField(max_length=100)  # column
    # Location
    job_type = models.CharField(max_length=100, choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    def __str__(self):
        return self.title
