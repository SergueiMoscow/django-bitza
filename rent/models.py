from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Building(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='Название',
    )
    address1 = models.CharField(
        max_length=100,
        verbose_name='Адрес',
        blank=True,
        default=''
    )
    address2 = models.CharField(
        max_length=100,
        verbose_name='Регион',
        blank=True,
        default=''
    )
    zip = models.CharField(
        max_length=10,
        verbose_name='Индекс',
        blank=True,
        null=True,
        default=''
    )
    notes = models.CharField(
        max_length=255,
        verbose_name='Описание',
        blank=True,
        null=True,
        default=''
    )
    BUILDING_STATUSES = [
        ('A', 'Сдаётся'),
        ('B', 'Не сдаётся')
    ]
    status = models.CharField(
        choices=BUILDING_STATUSES,
        max_length=20,
        verbose_name='Статус'
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Строения'
        verbose_name_plural = 'Строения'

    def __str__(self):
        return self.name


class Room(models.Model):
    shortname = models.CharField(
        primary_key=True,
        max_length=5,
        help_text='Комната',
        unique=True,
        verbose_name='Комната'
    )
    name = models.CharField(
        max_length=30,
        help_text='Комната',
        verbose_name='Комната'
    )
    building = models.ForeignKey(
        Building,
        verbose_name='Строение',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=None
    )
    floor = models.IntegerField(
        help_text='Этаж',
        verbose_name='Этаж',
        blank=True,
        null=True
    )
    square = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text='Площадь',
        verbose_name='Площадь',
        blank=True,
        null=True
    )
    price1 = models.IntegerField(
        help_text='Цена',
        verbose_name='Цена',
        blank=True,
        null=True
    )
    price2 = models.IntegerField(
        help_text='Цена',
        verbose_name='Цена',
        blank=True,
        null=True
    )
    description = models.CharField(
        max_length=255,
        help_text='Описание',
        verbose_name='Описание',
        blank=True,
        null=True
    )
    ROOM_STATUSES = [
        ('A', 'Сдаётся'),
        ('B', 'Не сдаётся')
    ]
    status = models.CharField(
        choices=ROOM_STATUSES,
        max_length=1,
        help_text='Статус',
        verbose_name='Статус',
        default='A'
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['shortname']
        verbose_name = 'Комнаты',
        verbose_name_plural = 'Комнаты'

    def __str__(self):
        return self.shortname


class Contact(models.Model):
    surname = models.CharField(
        max_length=40,
        help_text='Фамилия',
        verbose_name='Фамилия',
        blank=True,
        null=True
    )
    name = models.CharField(
        max_length=40,
        help_text='Имя',
        verbose_name='Имя',
        blank=True,
        null=True
    )
    birth_date = models.DateField(
        verbose_name='Дата рождения',
        blank=True,
        null=True
    )
    birth_place = models.CharField(
        max_length=100,
        verbose_name='Место рождения',
        blank=True,
        null=True
    )
    DOCUMENTS = [
        ('Паспорт РФ', 'Паспорт РФ'),
        ('Паспорт другого государства', 'Паспорт другого государства'),
        ('Удостоверение', 'Удостоверение'),
        ('Военный билет', 'Военный билет'),
        ('Паспорт Таджикистана', 'Паспорт Таджикистана'),
        ('Паспорт Узбекистана', 'Паспорт Узбекистана')
    ]
    document_name = models.CharField(
        choices=DOCUMENTS,
        max_length=30,
        default=DOCUMENTS[0],
        verbose_name='Документ',
        blank=True,
        null=True
    )
    doc_series = models.CharField(
        max_length=4,
        verbose_name='Серия',
        blank=True,
        null=True
    )
    doc_number = models.CharField(
        max_length=10,
        verbose_name='Номер',
        blank=True,
        null=True
    )
    doc_date = models.DateField(
        verbose_name='Дата выдачи',
        blank=True,
        null=True
    )
    doc_issued = models.CharField(
        max_length=255,
        verbose_name='Кем выдан',
        blank=True,
        null=True
    )
    address1 = models.CharField(
        max_length=100,
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    address2 = models.CharField(
        max_length=100,
        verbose_name='Адрес',
        blank=True,
        null=True,
    )
    city = models.CharField(
        max_length=50,
        verbose_name='Город',
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=True,
        null=True
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон',
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=50,
        verbose_name='Город',
        blank=True,
        null=True
    )
    notes = models.CharField(
        max_length=255,
        verbose_name='Заметки',
        blank=True,
        null=True
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        ordering = ['surname', 'name']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class ContractForm(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Название',
        primary_key=True
    )
    description = models.CharField(
        max_length=50,
        verbose_name='Описание',
    )
    html_file = models.CharField(
        max_length=20,
        verbose_name='Файл',
    )
    FORM_STATUSES = [
        ('A', 'Активный'),
        ('B', 'Устаревший'),
    ]
    status = models.CharField(
        choices=FORM_STATUSES,
        max_length=20,
        verbose_name='Статус'
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Бланк договора'
        verbose_name_plural = 'Бланки договоров'


class Contract(models.Model):
    date_begin = models.DateField(
        verbose_name='Дата'
    )
    date_end = models.DateField(
        verbose_name='Дата закрытия',
        blank=True,
        null=True
    )
    form = models.ForeignKey(
        ContractForm,
        on_delete=models.DO_NOTHING,
        verbose_name='Бланк договора',
        blank=True,
        null=True,
        default=None
    )
    number = models.CharField(
        primary_key=True,
        max_length=20,
        verbose_name='Номер',
        unique=True
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.PROTECT,
        verbose_name='Комната'
    )
    pay_day = models.IntegerField(
        verbose_name='Дата оплаты',
        validators=[MinValueValidator(1), MaxValueValidator(30)],
    )
    price = models.IntegerField(
        verbose_name='Цена',
    )
    deposit = models.IntegerField(
        verbose_name='Депозит',
        default=0
    )
    discount = models.IntegerField(
        verbose_name='Скидка',
        default=0
    )
    contact = models.ForeignKey(
        Contact,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        default=None
    )
    CONTRACT_STATUSES = [
        ('A', 'Активный'),
        ('B', 'Закрыт')
    ]
    status = models.CharField(
        choices=CONTRACT_STATUSES,
        max_length=1,
        verbose_name='Статус'
    )
    close_date = models.DateField(
        verbose_name='Дата закрытия',
        blank=True,
        null=True,
        default=None
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-number']
        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'

    def __str__(self):
        return f'{self.room}, {self.date_begin}, {self.price}, {self.status}'


class Document(models.Model):
    contact = models.ForeignKey(
        Contact,
        on_delete=models.CASCADE,
        verbose_name='Контакт'
    )
    image_file = models.ImageField(
        upload_to='documents',
        verbose_name='Изображение'
    )
    description = models.CharField(
        max_length=100,
        verbose_name='Описание',
        blank=True,
        null=True
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Payment(models.Model):
    PAYMENT_TYPES = [
        ('Man', 'Ручной ввод'),
        ('Alq', 'Аренда'),
        ('Aju', 'Корректировка'),
    ]

    type = models.CharField(
        choices=PAYMENT_TYPES,
        max_length=5,
        verbose_name='Тип',
        default=PAYMENT_TYPES[0],
        blank=True,
        null=True
    )
    time = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Время регистрации'
    )
    contract = models.ForeignKey(
        Contract,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=''
    )
    room = models.ForeignKey(
        Room,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    # building_id
    date = models.DateField(
        verbose_name='Дата'
    )
    amount = models.IntegerField(
        verbose_name='Сумма'
    )
    discount = models.IntegerField(
        verbose_name='Скидка',
        blank=True,
        null=True,
        default=0
    )
    total = models.IntegerField(
        verbose_name='Всего'
    )
    BANK_ACCOUNTS = [
        ('Валя', 'Валя'),
        ('Ольга', 'Ольга'),
        ('Сергей', 'Сергей'),
        ('Сбер', 'Сбер'),
        ('Авангард', 'Авангард'),
        ('Тинькофф', 'Тинькофф')
    ]
    bank_account = models.CharField(
        max_length=20,
        choices=BANK_ACCOUNTS,
        verbose_name='Счёт',
        blank=True,
        null=True,
    )
    BOOK_ACCOUNTS = [
        ('+', 'Приход'),
        ('-', 'Расход'),
        ('=', 'Корректировка')
    ]
    book_account = models.CharField(
        max_length=20,
        choices=BOOK_ACCOUNTS,
        verbose_name='Тип',
        blank=True,
        null=True,
    )
    concept = models.CharField(
        max_length=100,
        verbose_name='Описание',
        blank=True,
        null=True,
        default=''
    )
    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=0
    )
    created_at = models.DateField(
        verbose_name='Создан',
        auto_now_add=True,
        blank=True,
        null=True
    )
    updated_at = models.DateField(
        verbose_name='Обновлён',
        auto_now=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-time']
        verbose_name = 'Платёж'
        verbose_name_plural = 'Платежи'

    def list_years(self):
        query = """
            SELECT 
	            uuid() as id,
	            year as years
            FROM 
	            (SELECT DISTINCT YEAR(`date`) as year FROM rent_payment ORDER BY year DESC) as years;
        """
        years = []
        for year in self.objects.raw(query):
            years.append(year.years)
        print(years)
        return years


class ExpectedPayments(models.Model):
    number = models.CharField(max_length=50)
    date_begin = models.CharField(max_length=10)
    room = models.CharField(max_length=10)
    price = models.IntegerField()
    payed = models.IntegerField()
    diff = models.IntegerField()
    month_diff = models.DecimalField(max_digits=10, decimal_places=1)
    paid_months = models.DecimalField(max_digits=10, decimal_places=1)
    debt_month = models.DecimalField(max_digits=10, decimal_places=1)
    debt_rur = models.IntegerField()

    def background(self):
        if self.debt_month < 0:
            return 'bg-greenyellow'
        elif self.debt_month < 1:
            return 'bg-gold'
        else:
            return 'bg-red'

    class Meta:
        managed = False
        db_table = "expected_payments"