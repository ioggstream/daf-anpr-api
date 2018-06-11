# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion"]

setup(
    name=NAME,
    version=VERSION,
    description="Ora esatta.",
    author_email="robipolli@gmail.com",
    url="",
    keywords=["Swagger", "Ora esatta."],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    Questo servizio ritorna la data e l&#39;ora attuali in UTC.  #### Documentazione Il servizio Ora esatta ritorna l&#39;ora del server in formato RFC5424 (syslog).  &#x60;2018-12-30T12:23:32Z&#x60;  ##### Sottosezioni E&#39; possibile utilizzare - con criterio - delle sottosezioni.  #### Note  Il servizio non richiede autenticazione, ma va&#39; usato rispettando gli header di throttling esposti in conformita&#39; alle Linee Guida del Modello di interoperabilita&#39;.  #### Informazioni tecniche ed esempi  Esempio:  &#x60;&#x60;&#x60; http http://localhost:8443/datetime/v1/echo {   &#39;datetime&#39;: &#39;2018-12-30T12:23:32Z&#39; } &#x60;&#x60;&#x60; 
    """
)

