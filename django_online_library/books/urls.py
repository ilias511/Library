from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from django_online_library.books.views import home_page, add_book, edit_book, book_details_page, profile, profile_edit, \
    profile_delete

urlpatterns = [
    path('', home_page, name='home page'),
    path('add/', add_book, name='add book'),
    path('edit/<int:id>', edit_book, name='edit book'),
    path('details/<int:id>', book_details_page, name='book details'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', profile_edit, name='edit profile'),
    path('profile/delete/', profile_delete, name='delete profile'),
]
