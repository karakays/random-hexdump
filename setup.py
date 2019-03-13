from setuptools import setup, find_packages

VERSION = open('VERSION').read()

setup(
    name='random-hexdump',
    version=VERSION,
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    maintainer='Selçuk Karakayalı',
    url='http://github.com/karakays/random-hexdump/',
    packages=find_packages(),
    python_requires='>=3',
    license='MIT',
    description='Generate random hexdumps',
    long_description=open('README.rst').read(),
)
