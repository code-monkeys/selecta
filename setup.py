# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='selecta',
    version='0.0.7',
    author='Thomas Schüßler',
    author_email='vindolin@gmail.com',
    packages=['selecta'],
    scripts=['bin/selecta'],
    url='https://github.com/vindolin/selecta',
    license='MIT',
    description='Interactively select an entry from your bash/zsh history.',
    long_description=open('README.rst').read(),
    install_requires=['urwid'],
    include_package_data=True,
    keywords = ['bash', 'zsh', 'curses', 'history'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console :: Curses',
    ],
)
