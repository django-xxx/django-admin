# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.2.0'


setup(
    name='django-admin',
    version=version,
    keywords='Django Admin Extensions',
    description='Django Admin Extensions',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-admin',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_admin'],
    py_modules=[],
    install_requires=['django-excel-response2>=2.0.8'],
    include_package_data=True,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
