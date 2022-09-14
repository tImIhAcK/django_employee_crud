from django.db import models
import uuid
from phonenumber_field.modelfields import PhoneNumberField

class Employee(models.Model):
    GENDER_CHOICE = (
        ('', 'Select gender'),
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    ROLE_CHOICES = (
        ('', 'Select role'),
        ('CEO', 'Cheif Executive Officer'),
        ('MD', 'Managing Director'),
        ('CTO', 'Chief Technology Officer'),
        ('CFO', 'Chief Financial Officier'),
        ('DAT', 'Data Analyst Team Lead'),
        ('SDA', 'Senior Data Analyst'),
        ('JNA', 'Junior Data Analyst'),
        ('WDT', 'Web Developer Team Lead'),
        ('SBD', 'Senior Back-End Developer'),
        ('JBD', 'Junior Back-End Developer'),
        ('SFD', 'Senior Front-End Developer'),
        ('JFD', 'Junior Front-End Developer'),
        ('INT', 'Intern')
    )
    name = models.CharField(verbose_name='fullname', max_length=100)
    email = models.EmailField()
    contact = PhoneNumberField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICE)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    salary = models.IntegerField(verbose_name='salary ($)')
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ('id',)