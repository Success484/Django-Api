from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=10)

class Product(models.Model):
    RATING_CHOICE= (
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')
    )
    name=models.CharField(max_length=20)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products')
    category= models.ForeignKey(Category, on_delete=models.CASCADE)
    prod_date= models.DateField(auto_now_add=True)  # date the product was added to the database
    exp_date= models.DateField(blank=True, null=True)   # when the product will expire
    ratings= models.CharField(max_length=5, choices=RATING_CHOICE)             
    dis_price= models.DecimalField(max_digits=5,decimal_places=2) 


    def _str_(self):
        return self.name