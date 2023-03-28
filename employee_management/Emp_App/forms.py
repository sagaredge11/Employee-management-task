from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'department', 'salary', 'document']

    def clean_salary(self):
        salary = self.cleaned_data['salary']
        if salary < 0:
            raise ValidationError('Salary cannot be negative')
        return salary

    def clean_document(self):
        document = self.cleaned_data['document']
        if not document:
            return document
        if not hasattr(document, '_size'):
            return document
        if document._size > 4 * 1024 * 1024:
            raise ValidationError('Maximum file size is 4MB')
        if not FileExtensionValidator(allowed_extensions=['pdf'])(document):
            raise ValidationError('Only PDF files are allowed')
        return document
