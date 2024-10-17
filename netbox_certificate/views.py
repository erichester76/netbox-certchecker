from netbox.views import generic
from . import forms, models, tables
from netbox.config import get_config
from OpenSSL import crypto
from datetime import datetime
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

class CAView(generic.ObjectView):
    queryset = models.CA.objects.all()

class HostnameView(generic.ObjectView):
    queryset = models.CA.objects.all()
    
class CertificateView(generic.ObjectView):
    queryset = models.Certificate.objects.all()

    def get_extra_context(self, request, instance):
        if not instance.cert:
            instance.not_before = ''
            instance.not_after = ''
            instance.subject = ''
            return {
                'cert': instance,
            }

        settings = get_config()
        cert_file_path = settings.MEDIA_ROOT + '/' + str(instance.cert)

        with open(cert_file_path, 'rt') as cert_file:
            cert_data = cert_file.read()
        try:
            cert = crypto.load_certificate(crypto.FILETYPE_PEM, cert_data)
            not_before = datetime.strptime(cert.get_notBefore().decode('utf-8'), "%Y%m%d%H%M%SZ")
            not_after = datetime.strptime(cert.get_notAfter().decode('utf-8'), "%Y%m%d%H%M%SZ")
            subject = dict(cert.get_subject().get_components())
            instance.not_before = not_before
            instance.not_after = not_after
            keys = list(subject.keys())
            instance.subject = keys[0].decode('utf-8') + '=' + subject[keys[0]].decode('utf-8')
        except:
            instance.subject = "Invalid Certificate"

        return {
            'cert': instance,
        }

class CertificateListView(generic.ObjectListView):
    queryset = models.Certificate.objects.all()
    table = tables.CertificateTable

class CAListView(generic.ObjectListView):
    queryset = models.CA.objects.all()
    table = tables.CATable

class HostnameListView(generic.ObjectListView):
    queryset = models.Hostname.objects.all()
    table = tables.HostnameTable

class CertificateEditView(generic.ObjectEditView):
    queryset = models.Certificate.objects.all()
    form = forms.CertificateForm

class CAEditView(generic.ObjectEditView):
    queryset = models.CA.objects.all()
    form = forms.CAForm

class HostnameEditView(generic.ObjectEditView):
    queryset = models.Hostname.objects.all()
    form = forms.HostnameForm

class CertificateDeleteView(generic.ObjectDeleteView):
    queryset = models.Certificate.objects.all()

class CADeleteView(generic.ObjectDeleteView):
    queryset = models.CA.objects.all()

class HostnameDeleteView(generic.ObjectDeleteView):
    queryset = models.Hostname.objects.all()
