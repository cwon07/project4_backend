from django.db import models

# Create your models here.
class Todo(models.Model):
    company = models.CharField(max_length=1000)
    about = models.CharField(max_length=1000)
    process = models.CharField(max_length=1000)
    remarks = models.CharField(max_length=1000, default = 'none')
    companyBenefits = models.CharField(max_length=1000, default = 'none')
    questionsToAsk = models.CharField(max_length=1000, default = 'what would you like to ask the interviewer')
    questionsToAnswer = models.CharField(max_length=1000, default = 'what would the interviewer ask you')
    technicalSkills= models.CharField(max_length=1000, default = 'DSA')
    softSkills = models.CharField(max_length=1000, default = 'people skills')
    cultureFit = models.CharField(max_length=1000, default = 'casual')
    helpfulLinks = models.CharField(max_length=1000, default = 'company website')
    
    
    
 
