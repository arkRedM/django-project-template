from django.contrib import admin

from master.models import MasterKeyValueData


class MasterKeyValueDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'key', 'value']
    search_fields = ['id', 'key', 'value']


admin.site.register(MasterKeyValueData, MasterKeyValueDataAdmin)
