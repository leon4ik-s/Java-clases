from django.shortcuts import render, redirect
from django import forms  # импортируем модуль forms

# Импорт модели HumanitarianAidRequest
from .models import HumanitarianAidRequest

# Создаем форму для модели HumanitarianAidRequest
class HumanitarianAidRequestForm(forms.ModelForm):
    class Meta:
        model = HumanitarianAidRequest  # Указываем модель, для которой создаем форму
        fields = ['military_unit', 'aid_type', 'description', 'quantity', 'status']  # Поля формы