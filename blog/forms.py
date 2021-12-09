from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings

from blog.models import News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category', 'photo']
        exclude = ('author', )
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # важно при загрузке изображения!!!
            'photo': forms.FileInput(attrs={'class': 'input-image-control'})
                 }


class EditNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'category']
        exclude = ('author', 'photo')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            # важно при загрузке изображения!!!
            'photo': forms.FileInput(attrs={'class': 'input-image-control'})
                 }





#  форма регистрации нового пользователя
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Подтверждение пароля", widget=forms.PasswordInput(attrs={'class': 'form-control'}))