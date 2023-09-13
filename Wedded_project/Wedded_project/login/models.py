from django.db import models

# Create your models here.
class Login(models.Model):
    login_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    type = models.CharField(max_length=45)
    u_id = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'login'



