#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = ["reframed>=1.6.0", "pandas>=2.0.0"]

test_requirements = requirements + ['cplex']

script_list = [
    "scripts/smetana",
]


setup(
    author="Daniel Machado",
    author_email='cdanielmachado@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console', 
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: Apache Software License',
    ],
    description="Species METabolic interaction ANAlysis (SMETANA) is a python-based command line tool to analyse microbial communities.",
    scripts=script_list,
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme,
    include_package_data=True,
    keywords='smetana',
    name='smetana',
    test_suite='tests',
    tests_require=test_requirements,
    packages=find_packages(include=['smetana']),
    setup_requires=['setuptools_scm'],
    url='https://github.com/cdanielmachado/smetana',
    version='1.2.1',
    zip_safe=False,
)
