#!/usr/bin/env python3
from setuptools import setup, find_packages
import glob

setup(
    name='DJ-Roomba',
    version='0.1.0',
    author='Marcell Vazquez-Chanlatte',
    packages=find_packages(),
    url='',
    license='LICENSE',
    description='',
    long_description=open('README.md').read(),
    install_requires=['pyroomba', 'amqp', 'evdev'],
    entry_points= {
        'console_scripts': [
            'roomba_drive = dj_roomba.drive:main',
            'roomba_joystick = dj_roomba.joystick:main',
        ]
    },
    data_files = [('configs', ['configs/ps4.json'])],
)
