from django.db import models

# Create your models here.
class ConsoleUser(models.Model):
    first_name= models.CharField(max_length=256)
    last_name=models.CharField(max_length=256)
    email=models.CharField(max_length=256, default='', db_index=True, unique=True)
    created_on= models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)


    def get_user_name(self):
        return self.first_name + ' ' + self.last_name
    def __unicode__(self):
        return u'{}-{}'.format(self.email, self.get_user_name())
    def to_json(self):
        return {
            'id': self.id,
            'name': self.get_user_name(),
            'email': self.email
        }

