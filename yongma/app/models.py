from django.db import models

# Create your models here.


class New(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Press(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=10)
    link = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    category = models.CharField(max_length=10)
    client_name = models.CharField(max_length=50)
    client_email = models.CharField(max_length=50)
    client_number = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    category = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.title
