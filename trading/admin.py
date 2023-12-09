from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from trading.models import NetworkNode


class ContactCountryFilter(admin.SimpleListFilter):
    """Кастомный фильтр для фильтрации по стране"""

    title = 'Страна'
    parameter_name = 'country'

    def lookups(self, request, model_admin):
        contact_countries = NetworkNode.objects.values_list('contact__country', flat=True).distinct()
        return [(country, country) for country in contact_countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__country=self.value())


class CityCountryFilter(admin.SimpleListFilter):
    """Кастомный фильтр для фильтрации по городу"""

    title = 'Город'
    parameter_name = 'city'

    def lookups(self, request, model_admin):
        contact_countries = NetworkNode.objects.values_list('contact__city', flat=True).distinct()
        return [(country, country) for country in contact_countries]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(contact__city=self.value())


@admin.action(description='Очистить задолжность')
def clear_debt(modeladmin, request, queryset):
    """Action для очистки задалжности"""

    queryset.update(debt_to_supplier=0)


@admin.register(NetworkNode)
class NetworkNodeAdmin(admin.ModelAdmin):
    """Панель администратора для объекта сети"""

    list_display = ('name', 'link_to_supplier', 'contact',)
    list_filter = (ContactCountryFilter, CityCountryFilter,)
    actions = [clear_debt]

    def link_to_supplier(self, obj):
        """Ссылка на поставщика"""

        if obj.supplier_id:
            supplier_admin_url = reverse('admin:trading_networknode_change', args=(obj.supplier_id,))
            return format_html('<a href="{url}">{supplier_name}</a>', url=supplier_admin_url,
                               supplier_name=obj.supplier.name)
        else:
            return '-'

    link_to_supplier.short_description = 'Supplier'
