
from django.shortcuts import render, redirect
from .models import MilitaryUnit, Doctor, DoctorApplication, HumanitarianAidRequest
from .forms import HumanitarianAidRequestForm
from django.shortcuts import render

def create_aid_request(request):
    if request.method == 'POST':
        form = HumanitarianAidRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aid_request_success')  # Перенаправление на страницу успеха
    else:
        form = HumanitarianAidRequestForm()
    return render(request, 'military_units/create_aid_request.html', {'form': form})


def index(request):
    return render(request, 'index.html')  # Убедитесь, что у вас есть файл index.html


# Представление для списка воинских частей
def military_unit_list(request):
    units = MilitaryUnit.objects.all()  # Получение всех данных из таблицы MilitaryUnit
    return render(request, 'military_units_list.html', {'units': units})

# Представление для списка докторов
def doctor_list(request):
    doctors = Doctor.objects.all()  # Получение всех данных из таблицы Doctor
    return render(request, 'doctor_list.html', {'doctors': doctors})

# Представление для списка заявок докторов
def doctor_application_list(request):
    applications = DoctorApplication.objects.all()  # Получение всех данных из таблицы DoctorApplication
    return render(request, 'doctor_application_list.html', {'applications': applications})

# Представление для списка запросов гуманитарной помощи
def humanitarian_aid_request_list(request):
    aid_requests = HumanitarianAidRequest.objects.all()  # Получение всех данных из таблицы HumanitarianAidRequest
    return render(request, 'humanitarian_aid_request_list.html', {'aid_requests': aid_requests})
