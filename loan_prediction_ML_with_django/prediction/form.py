from django import forms
from .models import file_upload

class file_upload_form(forms.ModelForm):
    class Meta:
        model = file_upload
        fields = "__all__"


class fill_form(forms.Form):

    gender_choices = [(1,'Male'),(0,'Female')]
    married_choices = [(1,'Yes'),(0,'No')]
    dependents_choices = [(3,'Zero'),(0,'one'),(2,'two'),(1,'Three Plus')]
    education_choices = [(0,'Graduate'),(1,'Non Graduate')]
    self_emp_choices = [(1,'Yes'),(0,'No')]
    prop_area_choices = [(2,'Urban'),(0,'Rural'),(1,'Semi Urban')]
    Credit_History_choices = [(0,0),(1,1)]
    gender = forms.CharField(label='What is your gender ? ', widget=forms.Select(choices=gender_choices))
    married = forms.CharField(label='Are you married ? ', widget=forms.Select(choices=married_choices))
    dependents = forms.CharField(label='How many dependents ? ', widget=forms.Select(choices=dependents_choices))
    education = forms.CharField(label='What is your education ? ', widget=forms.Select(choices=education_choices))
    self_emp = forms.CharField(label='Are you self employed ? ', widget=forms.Select(choices=self_emp_choices))
    ApplicantIncome = forms.FloatField(label="Applicant Income ? ")
    CoapplicantIncome = forms.FloatField(label="Coapplicant Income ? ")
    LoanAmount = forms.FloatField(label="Loan Amount ? ")
    Loan_Amount_Term = forms.FloatField(label="Loan Amount Term ? ")
    Credit_History = forms.CharField(label='Credit History ? ', widget=forms.Select(choices=Credit_History_choices))
    prop_area = forms.CharField(label='Type of property area ? ', widget=forms.Select(choices=prop_area_choices))