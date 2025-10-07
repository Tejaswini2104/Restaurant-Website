from django.db import models

# Create your models here.

class ItemList(models.Model):
    Category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.Category_name

class Items(models.Model):
    item_name = models.CharField(max_length=50)
    description = models.TextField(blank=False)
    price = models.IntegerField()
    category = models.ForeignKey(ItemList,related_name="name",on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Items/',blank=True)
    
    def __str__(self):
        return self.item_name


class AboutUs(models.Model):
    description = models.TextField(blank=False)
    
    def __str__(self):
        return self.description



class Feedback(models.Model):
    user_name = models.CharField(max_length=255)
    description = models.TextField(blank=False)
    rating = models.IntegerField()
    image = models.ImageField(upload_to='feedback_images/', null=True, blank=True)  # Save inside /media/feedback_images/
    
    def __str__(self):
        return self.user_name
    


class BookTable(models.Model):
    user_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    email = models.EmailField()
    total_person = models.IntegerField()
    booking_date = models.DateField()
    
    def __str__(self):
        return self.user_name
