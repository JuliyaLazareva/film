from django.contrib import admin
from datetime import date
from .models import *
from django.utils.translation import gettext_lazy as _
# Register your models here.

admin.site.register(GenresModel)


class DataFilter(admin.SimpleListFilter):
    title = _('Диапазон даты выхода')
    parameter_name = 'decade'

    def lookups(self, request, model_admin):

        return (
            ('1990', _('девяностые')),
            ('2000', _('нулевые')),
            ('2010', _('десятые')),
            ('2020', _('двадцатые')),
        )

    def queryset(self, request, queryset):
        if self.value() == '1990':
            return queryset.filter(year__gte=date(1990, 1, 1), year__lte=date(1999, 12, 31))
        if self.value() == '2000':
            return queryset.filter(year__gte=date(2000, 1, 1), year__lte=date(2009, 12, 31))
        if self.value() == '2010':
            return queryset.filter(year__gte=date(2010, 1, 1), year__lte=date(2019, 12, 31))
        if self.value() == '2020':
            return queryset.filter(year__gte=date(2020, 1, 1), year__lte=date(2029, 12, 31))



@admin.register(MyFilmsModel)
class MyFilmsAdmin(admin.ModelAdmin):
    list_filter = ['genre', 'rating', 'views', DataFilter]



