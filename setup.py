from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Get universities data package'
LONG_DESCRIPTION = 'A package that gets data about the universities from a given url'

setup(
    name="universities",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="David Ginzburg",
    author_email="davidginzburg123@gmail.com",
    packages=find_packages(),
    install_requires=['requests'],
    keywords='conversion',
)