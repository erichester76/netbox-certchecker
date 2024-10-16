from setuptools import find_packages, setup

setup(
    name='netbox-certificate',
    version='1.0',
    description='Netbox plugin for SSL certificate management',
    install_requires=['pyOpenSSL'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={
        'netbox_certificate': ['templates/**'],
    },
    entry_points={
        'netbox_plugins': [
            'netbox_certificate = netbox_certificate:Plugin',
        ],
    },
)
