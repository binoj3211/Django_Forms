from django.urls import path

from myapp import views

urlpatterns = [
    path('', views.ContactView.as_view(), name="add-contact"),
    path('list/', views.ContactListView.as_view(), name="list-contact"),
    path('update/<id>/', views.ContactUpdateView.as_view(), name="update-contact"),
]