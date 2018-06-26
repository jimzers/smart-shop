from django.db import models


# Create your models here.

class Clothing(models.Model):
    clothing_name = models.CharField(max_length=250)
    store_name = models.CharField(max_length=600)
    clothing_type = models.CharField(max_length=600)
    clothing_price = models.IntegerField()
    clothing_style = models.CharField(max_length=600)
    clothing_gender = models.CharField(max_length=200)
    clothing_url = models.CharField(max_length=1000)
    clothing_image = models.CharField(max_length=1000)
    friendly = models.BooleanField(default=False)

    def __str__(self):
        return 'Clothing: ' + self.clothing_name

fle = "clothesdata.txt"
f = open(fle)
text = f.read()
with open(fle) as f:
    clothelist = [line.split() for line in f]

    for lst in clothelist:
        Clothing(clothing_name=lst[0], store_name=lst[1], clothing_type=lst[2], clothing_price=lst[3],
                 clothing_style=lst[4], clothing_gender=lst[5], clothing_url=lst[6], clothing_image=lst[7], friendly=lst[8])
