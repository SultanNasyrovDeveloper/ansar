from django.db import models
from django.shortcuts import reverse


class Product(models.Model):
    """ Продукт(Масло) """
    carousel = models.BooleanField(default=False, verbose_name='Отображать в карусели')
    img = models.FileField(upload_to='images/', verbose_name='Изображение 1(Большое')
    img_mini = models.FileField(upload_to='images/', verbose_name='Изображение 1(миниатюра)')
    badge = models.CharField(max_length=15, null=True, blank=True, default=None, verbose_name='Бейдж')
    name = models.CharField(max_length=100, verbose_name='Название')

    health_text = models.ForeignKey('ProductDescription', null=True, blank=True, on_delete=models.SET_NULL,
                                    verbose_name='Текст о здоровье', related_name='product')
    cooking_text = models.ForeignKey('ProductDescription', null=True, blank=True, on_delete=models.SET_NULL,
                                     verbose_name='Текст о кулинарии', related_name='product2')
    beauty_text = models.ForeignKey('ProductDescription', null=True, blank=True, on_delete=models.SET_NULL,
                                    verbose_name='Текст о красоте', related_name='product3')

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])


class Ingredient(models.Model):
    """ Базовый класс ингредиента продукта """
    name = models.CharField(max_length=75, verbose_name='Название')
    amount = models.CharField(max_length=50, verbose_name='На 100гр.')

    class Meta:
        abstract = True
        ordering = ('name', )


class Vitamins(Ingredient):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name='vitamins', verbose_name='Продукт')

    def __str__(self):
        return self.name


class Minerals(Ingredient):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name='minerals', verbose_name='Продукт')
    chemistry_name = models.CharField(max_length=20, verbose_name='Химическое название')

    def __str__(self):
        return self.name


class Fat(Ingredient):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name='fat', verbose_name='Продукт')

    def __str__(self):
        return self.name


class OtherIngredient(Ingredient):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_query_name='other_ingr', verbose_name='Продукт')

    def __str__(self):
        return self.name


class ProductDescription(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')


class DescriptionParagraph(models.Model):
    description = models.ForeignKey(ProductDescription, on_delete=models.CASCADE, related_name='paragraphs',
                                    related_query_name='paragraphs')
    position = models.IntegerField(null=True, blank=True, verbose_name='Порядковый номер порядка',
                                   help_text='Влияет на порядок вывода текста')
    title = models.CharField(max_length=150, null=True, blank=True, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Текст')

    class Meta:
        ordering = ('position', )

    def __str__(self):
        return 'Параграф'


class ProductAdvantage(models.Model):
    icon = models.FileField(upload_to='product_advantages/', null=True, blank=True, verbose_name='Иконка')
    title = models.CharField(max_length=30, verbose_name='Название преимущества')
    text = models.CharField(max_length=150, verbose_name='Описание преимущества')

    def __str__(self):
        return self.title


