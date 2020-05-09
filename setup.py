from setuptools import setup, find_packages

pkg_vars = {}

with open("rhd/_version.py") as fp:
    exec(fp.read(), pkg_vars)

setup(
    name='rhd',
    description='Generate random hexdumps',
    version=pkg_vars['__version__'],
    author='Selçuk Karakayalı',
    author_email='skarakayali@gmail.com',
    maintainer='Selçuk Karakayalı',
    url='http://github.com/karakays/random-hexdump/',
    packages=find_packages(),
    python_requires='>=3',
    license='MIT',
    long_description=open('README.rst').read(),
    classifiers=[ "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
