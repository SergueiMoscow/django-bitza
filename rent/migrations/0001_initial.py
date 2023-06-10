# Generated by Django 4.1 on 2023-06-06 20:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('address1', models.CharField(blank=True, default='', max_length=100, verbose_name='Адрес')),
                ('address2', models.CharField(blank=True, default='', max_length=100, verbose_name='Регион')),
                ('zip', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='Индекс')),
                ('notes', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('A', 'Сдаётся'), ('B', 'Не сдаётся')], max_length=20, verbose_name='Статус')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': 'Строения',
                'verbose_name_plural': 'Строения',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(blank=True, help_text='Фамилия', max_length=40, null=True, verbose_name='Фамилия')),
                ('name', models.CharField(blank=True, help_text='Имя', max_length=40, null=True, verbose_name='Имя')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('birth_place', models.CharField(blank=True, max_length=100, null=True, verbose_name='Место рождения')),
                ('document_name', models.CharField(blank=True, choices=[('Паспорт РФ', 'Паспорт РФ'), ('Паспорт другого государства', 'Паспорт другого государства'), ('Удостоверение', 'Удостоверение'), ('Военный билет', 'Военный билет'), ('Паспорт Таджикистана', 'Паспорт Таджикистана'), ('Паспорт Узбекистана', 'Паспорт Узбекистана')], default=('Паспорт РФ', 'Паспорт РФ'), max_length=30, null=True, verbose_name='Документ')),
                ('doc_series', models.CharField(blank=True, max_length=4, null=True, verbose_name='Серия')),
                ('doc_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='Номер')),
                ('doc_date', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('doc_issued', models.CharField(blank=True, max_length=255, null=True, verbose_name='Кем выдан')),
                ('address1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('address2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Адрес')),
                ('city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Город')),
                ('notes', models.CharField(blank=True, max_length=255, null=True, verbose_name='Заметки')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ['surname', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('date_begin', models.DateField(verbose_name='Дата')),
                ('date_end', models.DateField(blank=True, null=True, verbose_name='Дата закрытия')),
                ('number', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True, verbose_name='Номер')),
                ('pay_day', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Дата оплаты')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('deposit', models.IntegerField(default=0, verbose_name='Депозит')),
                ('discount', models.IntegerField(default=0, verbose_name='Скидка')),
                ('status', models.CharField(choices=[('A', 'Активный'), ('B', 'Закрыт')], max_length=1, verbose_name='Статус')),
                ('close_date', models.DateField(blank=True, default=None, null=True, verbose_name='Дата закрытия')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
                ('contact', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='rent.contact')),
            ],
            options={
                'verbose_name': 'Договор',
                'verbose_name_plural': 'Договоры',
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='ContractForm',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Название')),
                ('description', models.CharField(max_length=50, verbose_name='Описание')),
                ('html_file', models.CharField(max_length=20, verbose_name='Файл')),
                ('status', models.CharField(choices=[('A', 'Активный'), ('B', 'Устаревший')], max_length=20, verbose_name='Статус')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': 'Бланк договора',
                'verbose_name_plural': 'Бланки договоров',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('shortname', models.CharField(help_text='Комната', max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Комната')),
                ('name', models.CharField(help_text='Комната', max_length=30, verbose_name='Комната')),
                ('floor', models.IntegerField(blank=True, help_text='Этаж', null=True, verbose_name='Этаж')),
                ('square', models.DecimalField(blank=True, decimal_places=2, help_text='Площадь', max_digits=10, null=True, verbose_name='Площадь')),
                ('price1', models.IntegerField(blank=True, help_text='Цена', null=True, verbose_name='Цена')),
                ('price2', models.IntegerField(blank=True, help_text='Цена', null=True, verbose_name='Цена')),
                ('description', models.CharField(blank=True, help_text='Описание', max_length=255, null=True, verbose_name='Описание')),
                ('status', models.CharField(choices=[('A', 'Сдаётся'), ('B', 'Не сдаётся')], default='A', help_text='Статус', max_length=1, verbose_name='Статус')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
            ],
            options={
                'verbose_name': ('Комнаты',),
                'verbose_name_plural': 'Комнаты',
                'ordering': ['shortname'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[('Man', 'Ручной ввод'), ('Alq', 'Аренда'), ('Aju', 'Корректировка')], default=('Man', 'Ручной ввод'), max_length=5, null=True, verbose_name='Тип')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='Время регистрации')),
                ('date', models.DateField(verbose_name='Дата')),
                ('amount', models.IntegerField(verbose_name='Сумма')),
                ('discount', models.IntegerField(blank=True, default=0, null=True, verbose_name='Скидка')),
                ('total', models.IntegerField(verbose_name='Всего')),
                ('bank_account', models.CharField(blank=True, choices=[('Валя', 'Валя'), ('Ольга', 'Ольга'), ('Сергей', 'Сергей'), ('Сбер', 'Сбер'), ('Авангард', 'Авангард'), ('Тинькофф', 'Тинькофф')], max_length=20, null=True, verbose_name='Счёт')),
                ('book_account', models.CharField(blank=True, choices=[('+', 'Приход'), ('-', 'Расход'), ('=', 'Корректировка')], max_length=20, null=True, verbose_name='Тип')),
                ('concept', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
                ('contract', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rent.contract')),
                ('room', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rent.room')),
                ('user', models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Платёж',
                'verbose_name_plural': 'Платежи',
                'ordering': ['-updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_file', models.ImageField(upload_to='documents', verbose_name='Изображение')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Описание')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='Создан')),
                ('updated_at', models.DateField(auto_now=True, null=True, verbose_name='Обновлён')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rent.contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Документ',
                'verbose_name_plural': 'Документы',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='contract',
            name='form',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='rent.contractform', verbose_name='Бланк договора'),
        ),
        migrations.AddField(
            model_name='contract',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='rent.room', verbose_name='Комната'),
        ),
    ]
