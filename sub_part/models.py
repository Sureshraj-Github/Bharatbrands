from django.db import models

# Create your models here.



class reg1(models.Model):
     nameid=models.CharField(max_length=100)
     emailid=models.EmailField()
     phone=models.CharField(max_length=100)
     userid=models.CharField(max_length=100)
     enterpassword=models.CharField(max_length=100)


     def __str__(self):
        return self.userid

class expensetyp(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class deptt(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class itemexpen(models.Model):
    tid=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    etype=models.CharField(max_length=100)
    iname=models.CharField(max_length=100)
    quant=models.CharField(max_length=100)
    amt=models.CharField(max_length=100)
    pacc=models.CharField(max_length=100)

    def __str__(self):
        return self.tid

class ex8(models.Model):
    tid=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    etype=models.CharField(max_length=100)
    stname=models.CharField(max_length=100)
    purp=models.CharField(max_length=100)
    amt=models.CharField(max_length=100)
    pacc=models.CharField(max_length=100)

    def __str__(self):
        return self.tid

class miscexpen(models.Model):
    tid=models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    etype=models.CharField(max_length=100)
    purp=models.CharField(max_length=100)
    amt=models.CharField(max_length=100)
    pacc=models.CharField(max_length=100)

    def __str__(self):
        return self.tid

class create(models.Model):
    numm=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    atype=models.CharField(max_length=100)
    bal=models.CharField(max_length=100)
    cbal=models.CharField(max_length=100)

    def __str__(self):
        return self.numm


class tabl(models.Model):
    et=models.CharField(max_length=100)
    an=models.CharField(max_length=100)
    d=models.CharField(max_length=100)
    it=models.CharField(max_length=100)
    fd=models.CharField(max_length=100)
    td=models.CharField(max_length=100)

    def __str__(self):
        return self.et

    