from django.db import models


class Tasks(models.Model):
    """
    This table is used to store the tasks that need to be done.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=255, default="Pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, null=False)

    def __str__(self):
        return self.title
