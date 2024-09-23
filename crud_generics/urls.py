"""
URL configuration for crud_generics project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import BookView,BookViewDelete, GetOneBook,Book_All

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',BookView.as_view(),name='book'),
    path('book/update/<uuid:book_id>',BookView.as_view(),name='book_update'),
    # path('book/delete/<str:book_id>',BookViewDelete.as_view(),name='book_remove')
    path('book/delete/',BookViewDelete.as_view(),name='book_remove'),
    # path('get_book/<uuid:book_id>',GetOneBook.as_view(),name='get_one'),
    path('get_book',GetOneBook.as_view(),name='get_one'),
    path('book_all/<uuid:book_id>',Book_All.as_view(),name='get_book')


]
