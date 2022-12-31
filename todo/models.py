from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

# FLAW 2 Fix: delete these functinos and rely on Django's existing
# password manaagement functinality

    def set_password(self, raw_password):
        self.password = raw_password
        self._password = raw_password

    def check_password(self, entered_password):
        return entered_password == self.password

    class Meta:
        db_table = "auth_user"

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)