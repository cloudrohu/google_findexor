import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from . import models
from .models import Category,City,Locality

class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','image_tag',]


@admin_thumbnails.thumbnail('image')
class LocalityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','city', 'tree_actions', 'indented_title', 'image_thumbnail','slug',
                    )
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}    
  

@admin_thumbnails.thumbnail('image')
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('id','tree_actions', 'indented_title', 'image_thumbnail','slug',
                    )
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug': ('title',)}    


admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Category,CategoryAdmin)


