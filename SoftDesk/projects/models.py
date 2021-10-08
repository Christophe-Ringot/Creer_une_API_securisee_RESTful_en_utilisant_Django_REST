from django.conf import settings
from django.db import models

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=128)
    date = models.DateField()
    description = models.CharField(max_length=128)
    completed = models.BooleanField(default=None)

    TYPE_CHOICES = [
        ('Back', 'Back'), ('Front', 'Front'), ('iOS', 'iOS'),
        ('Android', 'Android')
    ]
    type = models.CharField(max_length=7, choices=TYPE_CHOICES)

    author_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                                       on_delete=models.CASCADE,
                                       blank=True, null=True)


class Contributor(models.Model):
    ALL = 'Al'
    READ = 'Rd'
    PERMISSION_CHOICES = [(ALL, 'All'), (READ, 'Read')]
    permission = models.CharField(
        max_length=2, choices=PERMISSION_CHOICES, default=READ
        )
    role = models.CharField(max_length=128)

    user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )
    project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE,
                                   blank=True, null=True)


class Issue(models.Model):

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    PRIORITY_CHOICES = [('Low', 'Low'), ('Middle', 'Middle'), ('High', 'High')]
    priority = models.CharField(
        max_length=6, choices=PRIORITY_CHOICES, default='Middle'
        )
    TAG_CHOICES = [('Bug', 'Bug'), ('Improve', 'Improve'), ('Task', 'Task')]
    tag = models.CharField(max_length=7, choices=TAG_CHOICES, default='Bug')
    STATUS_CHOICES = [
        ('Todo', 'Todo'), ('Inprogress', 'Inprogress'),
        ('Finished', 'Finished')
        ]
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='Todo'
        )

    project_id = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, blank=True, null=True
        )
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='user_id_author', blank=True, null=True
        )
    assignee_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='user_id_assignee', blank=True, null=True
        )


class Comment(models.Model):

    description = models.CharField(max_length=128)
    created_time = models.DateTimeField(auto_now_add=True)

    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        blank=True, null=True
        )
    issue_id = models.ForeignKey(
        to=Issue, on_delete=models.CASCADE, blank=True, null=True
        )
