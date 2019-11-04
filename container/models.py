from django.db import models

# Create your models here.


class MarkupKey(models.Model):
    markup_key = models.CharField(max_length=255, null=True, blank=True)
    is_used = models.BooleanField(default=False)

    def __str__(self):
        return '{}'.format(self.markup_key)