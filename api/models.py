import hashlib
from datetime import datetime

from django.db import models


# Create your models here.
class Room(models.Model):
    host = models.CharField(max_length=50, unique=True)
    guest_can_pause = models.BooleanField(null=False, default=False)
    votes_to_skip = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=255, unique=True, default="")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = self.get_code()

    def get_code(self):
        return f'{hashlib.md5(self.host.encode("utf-8")).hexdigest()}_{datetime.utcnow().timestamp()}'
