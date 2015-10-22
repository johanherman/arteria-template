from setuptools import setup, find_packages
import os
from template import __version__


def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='arteria-template',
    version=__version__,
    description="Initial arteria service template",
    long_description=read_file('README'),
    keywords='bioinformatics',
    author='SNP&SEQ Technology Platform, Uppsala University',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': ['template-ws = template.app:start']
    }
)
