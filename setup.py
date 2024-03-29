# -*- coding: utf-8 -*-
"""Installer for the eea.privacyscreen package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='eea.privacyscreen',
    version='1.0a1',
    description="Privacy Screen for embedded content",
    long_description=long_description,
    # Get more from https://pypi.org/classifiers/
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: Addon",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='Tiberiu Ichim',
    author_email='tiberiu.ichim@eaudeweb.ro',
    url='https://github.com/eea/eea.privacyscreen',
    project_urls={
        'PyPI': 'https://pypi.python.org/pypi/eea.privacyscreen',
        'Source': 'https://github.com/eea/eea.privacyscreen',
        'Tracker': 'https://github.com/eea/eea.privacyscreen/issues',
    },
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['eea'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    python_requires="==2.7",
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
        'Products.GenericSetup>=1.8.2',
        'plone.api>=1.8.4',
        'plone.restapi',
        'plone.schema',
        "collective.z3cform.datagridfield",
    ],
    extras_require={
        # 'test': [
        #     'plone.app.testing',
        #     # Plone KGS does not use this version, because it would break
        #     # Remove if your package shall be part of coredev.
        #     # plone_coredev tests as of 2016-04-01.
        #     'plone.testing>=5.0.0',
        #     'plone.app.robotframework[debug]',
        # ],
    },
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    [console_scripts]
    update_locale = eea.privacyscreen.locales.update:update_locale
    """,
)
