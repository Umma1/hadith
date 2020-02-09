from setuptools import find_packages, setup

import hadith

setup(
    name='hadith',
    version=hadith.__version__,
    description='Helps hadith scholars with quantitative research',
    packages=find_packages(),
    install_requires=['pandas']
)
