from django.contrib import admin

from .models import (Product, Ingredient, ProductDescription, DescriptionParagraph, ProductAdvantage)


class IngredientInlineAdmin(admin.TabularInline):
    model = Ingredient
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (IngredientInlineAdmin, )


class DescriptionParagraphInline(admin.TabularInline):
    model = DescriptionParagraph
    extra = 0


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    inlines = (DescriptionParagraphInline, )


@admin.register(ProductAdvantage)
class ProductAdvantageAdmin(admin.ModelAdmin):
    pass

