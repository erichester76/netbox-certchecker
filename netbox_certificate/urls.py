from django.urls import path
from netbox.views.generic import ObjectChangeLogView
from . import models, views

urlpatterns = (
    path('certificates/', views.CertificateListView.as_view(), name='certificate_list'),
    path('certificates/add/', views.CertificateEditView.as_view(), name='certificate_add'),
    path('certificates/<int:pk>/', views.CertificateView.as_view(), name='certificate'),
    path('certificates/<int:pk>/edit/', views.CertificateEditView.as_view(), name='certificate_edit'),
    path('certificates/<int:pk>/delete/', views.CertificateDeleteView.as_view(), name='certificate_delete'),
    path('certificates/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='certificate_changelog', kwargs={
        'model': models.Certificate
    }),
    path('hostnames/', views.HostnameListView.as_view(), name='hostname_list'),
    path('hostnames/add/', views.HostnameEditView.as_view(), name='hostname_add'),
    path('hostnames/<int:pk>/', views.HostnameView.as_view(), name='hostname'),
    path('hostnames/<int:pk>/edit/', views.HostnameEditView.as_view(), name='hostname_edit'),
    path('hostnames/<int:pk>/delete/', views.HostnameDeleteView.as_view(), name='hostname_delete'),
    path('hostnames/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='hostname_changelog', kwargs={
        'model': models.Hostname
    }),
    
    path('cas/', views.CAListView.as_view(), name='ca_list'),
    path('cas/add/', views.CAEditView.as_view(), name='ca_add'),
    path('cas/<int:pk>/', views.CAView.as_view(), name='ca'),
    path('cas/<int:pk>/edit/', views.CAEditView.as_view(), name='ca_edit'),
    path('cas/<int:pk>/delete/', views.CADeleteView.as_view(), name='ca_delete'),
    path('cas/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='ca_changelog', kwargs={
        'model': models.CA
    }),
)
