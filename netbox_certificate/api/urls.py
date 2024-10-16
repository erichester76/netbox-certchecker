from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'netbox_certificate'

router = NetBoxRouter()
router.register('certificate', views.CertificateViewSet)
router.register('ca', views.CAViewSet)
router.register('hostname', views.HostnameViewSet)

urlpatterns = router.urls
