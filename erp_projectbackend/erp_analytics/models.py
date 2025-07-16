

# This file intentionally left minimal.
# All individual models are organized in submodules.
# You can optionally define shared abstract base models here.

from django.db import models

# Optional: Shared abstract base class for timestamping
class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
