# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

# To update the package version number, edit deeprank/__version__.py
version = {}
with open(os.path.join(here, 'deeprank', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='deeprank',
    version=version['__version__'],
    description='Rank Protein-Protein Interactions using Deep Learning',
    long_description=readme + '\n\n',
    author='Nicolas Renaud et al.',
    url='https://github.com/DeepRank/deeprank',
    project_urls={
        'Source Code': 'https://github.com/DeepRank/deeprank',
        'Documentation': 'https://deeprank.readthedocs.io',
        'Issue tracker': 'https://github.com/DeepRank/deeprank/issues'
    },
    packages=find_packages(),
    include_package_data=True,
    license="Apache Software License 2.0",
    keywords='deeprank',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience:: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'numpy >= 1.13',
        'scipy',
        'h5py',
        'tqdm',
        'pandas',
        'mpi4py',
        'matplotlib',
        'torchsummary',
        'torch < 1.4.0',
        'pdb2sql >= 0.2.1',
        'freesasa==2.0.3.post7;platform_system=="Linux"',
        'freesasa==2.0.3.post6;platform_system=="Darwin"'
        ],
    extras_require={
        'test': ['nose', 'coverage', 'pytest', 'pytest-cov',
            'codacy-coverage', 'coveralls'],
        'dev':  ['prospector[with_pyroma]', 'autopep8', 'isort', 'sphinx'],
        'cuda': ['pycuda'],
    }
)