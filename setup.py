from setuptools import find_packages, setup

import hadith

setup(
    name='hadith',
    version=hadith.__version__,
    description='Helps hadith scholars with quantitative research',
    packages=find_packages(),
    install_requires=['pandas'],
    python_requires='>=3.6',
    include_package_data=True
)
