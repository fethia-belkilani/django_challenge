from django.urls import path
from printer import views

urlpatterns = [
    path("",views.ListPrinterAPIView.as_view(),name="printer_list"),
    path("create/", views.CreatePrinterAPIView.as_view(),name="printer_create"),
    path("update/<int:pk>/",views.UpdatePrinterAPIView.as_view(),name="update_printer"),
    path("delete/<int:pk>/",views.DeletePrinterAPIView.as_view(),name="delete_printer")
]