#!/usr/bin/env python

from setuptools import setup

setup(
    name="push",
    version="0.1",
    description="Twitter as a push notification service",
    author="Zach Williams",
    author_email="hey@zachwill.com",
    url="http://github.com/zachwill/push",
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    scripts=[
        "push"
    ],
    install_requires=[
        "requests",
        "termcolor"
    ]
)
