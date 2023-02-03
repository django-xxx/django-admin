# -*- coding: utf-8 -*-

from setuptools import setup


version = '2.0.2'


setup(
    name='django-admin',
    version=version,
    keywords='Django Admin Extensions',
    description='Django Admin Extensions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',

    url='https://github.com/django-xxx/django-admin',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['django_admin'],
    py_modules=[],
    install_requires=['django-excel-response2>=3.0.0', 'django-six'],
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
