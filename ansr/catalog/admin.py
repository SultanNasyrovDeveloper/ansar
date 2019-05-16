from django.contrib import admin

from .models import (Product, Vitamins, Minerals, Fat, OtherIngredient,
                     ProductDescription, DescriptionParagraph, ProductAdvantage)


class VitaminsInlineAdmin(admin.TabularInline):
    model = Vitamins
    extra = 0


class MineralsInlineAdmin(admin.TabularInline):
    model = Minerals
    extra = 0


class FatInlineAdmin(admin.TabularInline):
    model = Fat
    extra = 0


class OtherIngredientInlineAdmin(admin.TabularInline):
    model = OtherIngredient
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = (VitaminsInlineAdmin, MineralsInlineAdmin, FatInlineAdmin, OtherIngredientInlineAdmin, )


class DescriptionParagraphInline(admin.TabularInline):
    model = DescriptionParagraph
    extra = 0


@admin.register(ProductDescription)
class ProductDescriptionAdmin(admin.ModelAdmin):
    inlines = (DescriptionParagraphInline, )


@admin.register(ProductAdvantage)
class ProductAdvantageAdmin(admin.ModelAdmin):
    pass

