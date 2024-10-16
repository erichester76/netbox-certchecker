# netbox-certificate-plugin
## overview
Netbox Cert Checker is a Netbox plugin that helps you monitor SSL certificates and websites that use them.

Key Features:

* SSL Certificate Information Registration:
  + Identification name
  + Certificate upload
  + Display information of uploaded certificates:
    - Subject
    - Certificate start date
    - Expiration date
  + Website URL using the SSL certificate
  + Enable/disable expiration alerts
* Expiration monitoring and alert email sending via external scripts


## install

1. Get the latest release from this repository
2. Install openssl libraries if not installed
```
CentOS:
$ yum install openssl-devel libffi-devel

Ubuntu:
$ apt-get install libssl-dev libffi-dev
```
3. install plugin

```
$ pip install netbox_certificate.tar.gz
```

4. Add netbox configuration

```
PLUGINS = ['netbox_certificate']
```

5. Restart netbox service

5. Enjoy plugin!
