from django.db import models


class Subject(models.Model):
    SName = models.CharField(max_length = 100) 
    #imageurl = models.ImageField(upload_to = "Images/")
   
    def __str__(self):
        return self.SName 

    class Meta:
        db_table = "Subject"

class webimages(models.Model):
    imagex = models.ImageField(upload_to="Images/")

    class Meta:
        db_table = "webimages"

class QuestionMaster(models.Model):
    QName = models.CharField(max_length=400)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    cans = models.CharField(max_length=100)
    
    subject =  models.ForeignKey(Subject, on_delete=models.CASCADE)
    def __str__(self):
        return self.QName
        
    class Meta:
        db_table = "QuestionMaster"

class UserInfo(models.Model):
    Usern = models.CharField(max_length=100)
    emailadd = models.CharField(max_length=400)
    passw = models.CharField(max_length=100)
    passwr = models.CharField(max_length=100)

    class Meta:
        db_table = "register"
