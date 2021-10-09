from django.db import models


service_types = [
    ('all', 'Все услуги'),
    ('manicure', 'Маникюр'),
    ('pedicure', 'Педикюр'),
    ('design', 'Дизайн'),
    ('combo', 'Комбо'),
    ('cut', 'Снятие'),
]


class Service(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=8, choices=service_types, default='all')

    def __str__(self):
        return self.title
