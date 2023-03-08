from django import forms
from employeeapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee 
        fields = "__all__"
        labels = {
            'fname' : 'First name',
            'lname' : 'Last name',
            'address' : 'Address',
            'gender': 'Sex',
            'pronouns': 'Pronouns',
            'birthdate': 'Birthdate',
            'department': 'Department',
            'salary': 'Salary',
            'cover' : 'Photo'
        }
        
        widgets = {
            'address': forms.Textarea(attrs={'rows' : '3'}),
            'gender': forms.RadioSelect(),
            'birthdate': forms.DateInput(attrs={'type':'date'})        
        }