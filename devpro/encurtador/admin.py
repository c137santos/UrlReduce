from django.contrib import admin

# Register your models here.
from devpro.encurtador.models import UrlRedirect, UrlLogs


@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):
   list_display =('destino', 'slug', 'criado_em', 'atualizado_em')

@admin.register(UrlLogs)
class UrlLogsAdmin(admin.ModelAdmin):
   list_display = ('origem', 'criado_em', 'user_agent', 'host', 'ip', 'url_redirect')

   def has_change_permission(self, request, obj=None):
      return False

   def has_delete_permission(self, request, obj=None):
      return False