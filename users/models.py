from django.db import models

class Users(models.Model):
    phone_number = models.CharField(max_length=100)
    name = models.CharField(max_length=100 ,null=True)
    gender = models.SmallIntegerField(null=True)
    IsPremium = models.BooleanField(default=False)
    IsBlocked = models.BooleanField(default=False)
    lastSeen = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tbl_user'
    def __str__(self):
        return self.phone_number
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
