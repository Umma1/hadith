from setuptools import find_packages, setup

import hadith

setup(
    name='hadith',
    version=hadith.__version__,
    author="Umma Open Source",
    author_email="umma.opensource@gmail.com",
    description='Helps hadith scholars with quantitative research',
    url="https://github.com/Umma1/hadith/",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['pandas', 'pyyaml'],
    python_requires='>=3.6',
    include_package_data=True
)
