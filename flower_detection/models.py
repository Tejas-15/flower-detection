from django.db import models

# Create your models here.

class Info(models.Model):
    Flower_name = models.CharField(max_length=50) 
    Introduction = models.TextField()
    Etymology = models.TextField()
    Evolution = models.TextField()
    Species = models.TextField()
    Tax_domain = models.CharField(max_length=50)
    Tax_kingdom = models.CharField(max_length=50)
    Tax_phylum = models.CharField(max_length=50)
    Tax_order = models.CharField(max_length=50)
    Tax_family = models.CharField(max_length=50)
    Tax_genus = models.CharField(max_length=50)
    Ornamental_plants = models.TextField()
    Cut_flowers = models.TextField()
    Medicinal_uses = models.TextField()
    Health_benefit = models.TextField()
    Perfumes_food = models.TextField()
    Symbolizes = models.TextField()
    Season_to_grow = models.TextField()
#     Image_flower = models.ImageField(null=True, blank=True, upload_to")

    def __str__(self):
        return self.Flower_name

# class Upload_img(models.Model): 
#     Uploaded_image = models.ImageField() 