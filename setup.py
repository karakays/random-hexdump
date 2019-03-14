from setuptools import setup, find_packages

pkg_vars = {}

with open("random-hexdump/_version.py") as fp:
    exec(fp.read(), pkg_vars)

setup(
    name='random-hexdump',
    version=pkg_vars['__version__'],
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    maintainer='Selçuk Karakayalı',
    url='http://github.com/karakays/random-hexdump/',
    packages=find_packages(),
    python_requires='>=3',
    license='MIT',
    description='Generate random hexdumps',
    long_description=open('README.rst').read(),
    classifiers=[ "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
