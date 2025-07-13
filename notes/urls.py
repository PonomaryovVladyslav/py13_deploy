from django.urls import path
from .views import NoteListView, Login, Logout, Register, NoteCreateView, NoteDeleteView

urlpatterns = [
    path('', NoteListView.as_view(), name='index'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
path('note/create/', NoteCreateView.as_view(), name='note-create'),
path('note/delete/<int:pk>/', NoteDeleteView.as_view(), name='note-delete'),
]
