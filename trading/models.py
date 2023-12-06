from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продукта"""
    name = models.CharField(max_length=200, verbose_name='название')
    model = models.CharField(max_length=100, verbose_name='модел')
    release_date = models.DateField(verbose_name='дата выхода')

    def __str__(self):
        return f'{self.name} - {self.model}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Contact(models.Model):
    """Модель создания контактов """
    email = models.EmailField(verbose_name='почта')
    country = models.CharField(max_length=100, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=100, verbose_name='улица')
    number_home = models.PositiveIntegerField(verbose_name='номер дома')

    def __str__(self):
        return f'{self.email} - {self.country}, {self.city}, {self.street}, {self.number_home}'

    class Meta:
        verbose_name = 'контакты'
        verbose_name_plural = 'контакты'


class NetworkNode(models.Model):
    """Модель узла сети"""
    name = models.CharField(max_length=200, verbose_name='название')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='контакты')
    products = models.ManyToManyField(Product, verbose_name='продукты')
    supplier = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='поставщик', **NULLABLE)
    debt_to_supplier = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        return f'{self.name} - {self.products}'

    class Meta:
        verbose_name = 'сеть'
        verbose_name_plural = 'сети'
