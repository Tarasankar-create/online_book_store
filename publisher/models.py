from django.db import models

class Catagory(models.Model):
    c_id=models.AutoField(primary_key=True)
    c_name=models.CharField(max_length=40)
    def __str__(self):
        return self.c_name
    
class Add_Book(models.Model):
    c_name=models.ForeignKey(Catagory,on_delete=models.CASCADE)
    bookname=models.CharField(max_length=50)
    authorname=models.CharField(max_length=50)
    isbn=models.IntegerField(primary_key=True,max_length=50)
    price=models.FloatField()
    discount=models.IntegerField()
    bookdoc=models.ImageField(upload_to='Book_Image/')
    review = models.TextField(null=True, blank=True) 
    def __str__(self):
        return self.bookname