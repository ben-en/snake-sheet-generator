from setuptools import setup

import ssg as mod

setup(
    name='ssg',
    version='0.1',
    author='Ben Ennis',
    author_email='pnw.ben.ennis@gmail.com',
    description='Snake sheet generator for William\'s Forestry',
    packages=[mod.__name__],
    entry_points={
        'console_scripts': [
            'ssg = ssg.main:main',
        ],
    },
)
