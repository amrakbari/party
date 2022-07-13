import hashlib

from django.db import models


# Create your models here.
class Room(models.Model):
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def code(self):
        return f'{hashlib.md5(self.host).hexdigest()}_{self.created_at}'
