from django import views
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('blog/<int:id>', blog.views.detail, name = "detail"),
    path('new', blog.views.new, name = "new"),
    path('create', blog.views.create, name = "create"),
    path('blog/edit/<int:id>', blog.views.edit, name = "edit_blog"),
    path('blog/update/<int:id>', blog.views.update, name = "update"),
    path('blog/delete/<int:id>', blog.views.delete, name = "delete"),
    path('search', blog.views.search, name = "search"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)