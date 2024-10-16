from setuptools import find_packages, setup

setup(
    name='netbox-certificate',
    version='1.0',
    description='Netbox plugin for SSL certificate management',
    install_requires=['pyOpenSSL'],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
