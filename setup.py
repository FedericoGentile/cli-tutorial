from setuptools import find_packages, setup

setup(
    name='Calculator tutorial',
    version='0.0.1',
    packages= find_packages(),
    entry_points={
        'console_scripts':['calculator=src.calculator:main']
    }
)