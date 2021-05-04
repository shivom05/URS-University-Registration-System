from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

payment_mode = (
    ('debit card',"debit card"),
    ('net banking',"net banking"),
    ('paypal',"paypal")
)
 
sheet = (
     ('Yes',"Yes"),
     ('No',"No")
)
body = (
    ('male',"Male"),
    ('female',"Female"),
    ('other',"Other")
)
clg = (
   ('Daulat Ram College',"Daulat Ram College"),
   ('Gargi College',"Gargi College"),
   ('Hindu College',"Hindu College"),
   ('Hans Raj College',"Hans Raj College"),
   ('Maharaja Agarsen College',"Maharaja Agarsen College"),
   ('Delhi College of Arts & Commerce',"Delhi College of Arts & Commerce")
)
crs = (
    ('B.Sc (Hons) Applied Life Science',"B.Sc (Hons) Applied Life Science"),
    ('B.Sc (Hons) Electronics',"B.Sc (Hons) Electronics"),
    ('B.Com (Hons) Corporate Laws',"B.Com (Hons) Corporate Laws"),
    ('B.Sc (Hons) Mathematics',"B.Sc (Hons) Mathematics"),
    ('B.A. (Hons) Economics',"B.A. (Hons) Economics"),
    ('B.A (Hons) Psychology',"B.A (Hons) Psychology")
)
class student(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    f_name = models.CharField(max_length=100,default="")
    f_lname = models.CharField(max_length=100,default="")
    email = models.EmailField(max_length=100,default="")
    age = models.IntegerField()
    number = models.BigIntegerField(default="8888888888")
    gender = models.CharField(max_length=10, choices=body,default="", )
    father= models.CharField(max_length=100,default="")
    l_father = models.CharField(max_length=100,default="")
    address =  models.CharField(max_length=100,default="")
    photo=models.ImageField(upload_to='pics')
    dob=models.DateField(blank=True, null=True)
    
    
class register(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    d_name = models.CharField(max_length=100,default="N/A",null=True)
    d_lname = models.CharField(max_length=100,default="N/A",null=True)
    mobile = models.BigIntegerField(blank=True, null=True)
    college =models.CharField(max_length=200,choices=clg,blank=True, null=True)
    degree = models.CharField(max_length=200,choices=crs,blank=True, null=True)
    rdate = models.DateField(blank=True, null=True)
    reg_no = models.IntegerField(default="1234")
    
     
class payment(models.Model):
     user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
     p_name = models.CharField(max_length=100,default="N/A",blank=True, null=True)
     l_name = models.CharField(max_length=100,default="N/A",blank=True, null=True)
     mobile = models.BigIntegerField(blank=True, null=True)
     p_reg_no=models.IntegerField(blank=True, null=True)
     amount=models.BigIntegerField(default="25000")
     pmode = models.CharField(max_length=120,choices=payment_mode,default="")
     pdate = models.DateField(blank=True, null=True)

class paystatus(models.Model):
     user= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
     s_name=models.CharField(max_length=100,default="N/A",blank=True, null=True)
     s_lname=models.CharField(max_length=100,default="N/A",blank=True, null=True)
     s_reg_no = models.BigIntegerField(blank=True, null=True)
     state=models.CharField(max_length=20,blank=True, null=True)