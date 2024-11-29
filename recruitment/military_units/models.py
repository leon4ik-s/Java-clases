from django.db import models


class MilitaryUnit(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=5)  # Изменен на CharField, если это строка (например, номер части)
    location = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=11)  # Используем CharField для телефона
    speciality = models.CharField(max_length=70)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[  # Исправление выбора
        ('не подтверждено', 'Не подтверждено'),
        ('подтверждено', 'Подтверждено'),
        ('отклонено', 'Отклонено')
    ], default='не подтверждено')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.name


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    registered_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.first_name} {self.last_name}"


class DoctorApplication(models.Model):
    doctor = models.ForeignKey('Doctor', on_delete=models.CASCADE)  # Используем строковое представление модели
    military_unit = models.ForeignKey('MilitaryUnit', on_delete=models.CASCADE)  # Используем строковое представление модели

    status = models.CharField(max_length=20, choices=[
        ('новый', 'Новый'),
        ('обработан', 'Обработан'),
        ('отклонен', 'Отклонен')
    ], default='новый')

    applied_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Отклик {self.doctor} на {self.military_unit.name}"

class HumanitarianAidRequest(models.Model):
    military_unit = models.ForeignKey('MilitaryUnit', on_delete=models.CASCADE)  # Связь с частью
    aid_type = models.CharField(max_length=100)  # Тип помощи
    description = models.TextField()  # Подробности о помощи
    quantity = models.IntegerField()  # Количество единиц помощи
    status = models.CharField(max_length=20, choices=[
        ('ожидание', 'Ожидание'),
        ('одобрено', 'Одобрено'),
        ('отклонено', 'Отклонено')
    ], default='ожидание')
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"Запрос на помощь от {self.military_unit.name}: {self.aid_type}"


