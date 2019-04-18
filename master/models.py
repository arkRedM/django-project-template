from django.db import models


class MasterKeyValueData(models.Model):
    key = models.CharField(max_length=255)
    value = models.TextField()
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.key
