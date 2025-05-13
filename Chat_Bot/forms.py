from django import forms
from .models import *
from django.contrib.auth.models import User




class registerform(forms.ModelForm):
    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password')
        widgets={
            'password':forms.PasswordInput()
           
        }

class registerform1(forms.ModelForm):
    class Meta:
        model=registration
        fields=('address','phone','adno','dep','gen')
        # widgets={
        #     'gen':forms.RadioSelect()
        # }

class internalmarklist(forms.ModelForm):
    class Meta:
        model=internalmarklist
        fields=('Name','Register_Number','Department','Android_Programming','Operating_System','Software_Testing','Computer_Networks','Project')

class internalexammarklist(forms.ModelForm):
    class Meta:
        model=internalexammarklist
        fields=('Name','Register_Number','Department','Android_Programming','Operating_System','Software_Testing','Computer_Networks','Project')

class Attendence(forms.ModelForm):
    class Meta:
        model=Attendence
        fields=('Name','Register_Number','Department','Semester','From','To','ta')

class Fee_Payment(forms.ModelForm):
    class Meta:
        model=Fee_Payment
        fields=('Name','Register_Number','Department','Semester','Course_Fee','Paid','Due','Last_Date')
        
                
