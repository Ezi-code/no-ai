from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
	"""users model."""

	id = models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=True)
	username = models.CharField(max_length=50, null=False)
	email = models.EmailField(max_length=50, null=False, unique=True)

	USERNAME_FIELD = "email"
	EMAIL_FIELD = "email"
	REQUIRED_FIELDS = ["username"]
