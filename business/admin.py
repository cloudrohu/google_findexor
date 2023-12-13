import admin_thumbnails
from django.contrib import admin

# Register your models here.
from mptt.admin import DraggableMPTTAdmin

from .models import *


@admin_thumbnails.thumbnail('image')
class CityAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'image_thumbnail',
                    'related_locality_count','related_company_count',)
    list_display_links = ('indented_title',)
    list_per_page = 30 
    prepopulated_fields = {'slug': ('title',)}
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
       
        # Add non cumulative product count
        qs = City.objects.add_related_count(qs,
                 Locality,
                 'city',
                 'locality_count',
                 cumulative=False)
        qs = City.objects.add_related_count(qs,
                 Company,
                 'city',
                 'company_count',
                 cumulative=False)     
        return qs 

    def related_locality_count(self, instance):
        return instance.locality_count
    related_locality_count.short_description = 'Related Project (for this specific Locality)'
       

    def related_company_count(self, instance):
        return instance.company_count
    related_company_count.short_description = 'Related Locality (for this specific City)'


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


@admin_thumbnails.thumbnail('image')
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'title', 'contact_person','contact_no','email','address','locality','city','image_thumbnail']    
    list_editable=('title', 'contact_person','contact_no','email','address','locality','city') 
    list_filter = ('locality','city',) 
    search_fields = ['title']
    list_per_page = 30 


admin.site.register(City,CityAdmin)
admin.site.register(Locality,LocalityAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Company,CompanyAdmin)





