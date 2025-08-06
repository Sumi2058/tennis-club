from django.db import models
from django import forms

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  dob=models.CharField(max_length=20)



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname','dob']  