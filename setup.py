from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

name = 'py-scraper'

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open(f'{name}/__init__.py').read(),
    re.M
    ).group(1)

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
        name = name,
        packages = [name], # this must be the same as the name above
        version = version,
        description = long_description,
        author = 'joeyism',
        author_email = 'joeyism101@gmail.com',
        url = f'https://github.com/untitled-scraper-project/{name}', # use the URL to the github repo
        download_url = f'https://github.com/untitled-scraper-project/{name}/dist' + version + '.tar.gz',
        keywords = [], 
        classifiers = [],
        install_requires=[dependency.split("\n")[0] for dependency in open("requirements.txt", "r").readlines()]
        )
