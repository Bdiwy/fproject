from django.db import models

# Create your models here.
class prod(models.Model):
    name=models.CharField(max_length=50)
    comment=models.TextField()
    price= models.DecimalField(max_digits=5,decimal_places=2)
    act=models.BooleanField(default=True)
    img=models.ImageField(upload_to='photo/%y/%m/%d')

    def __str__(self):
        return self.name



    class  Meta:
        db_table = ''
        managed = True
        verbose_name = 'prod'
        verbose_name_plural = 'prod'
        ordering=['price']



# Create your models here.