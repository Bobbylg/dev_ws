from setuptools import find_packages
from setuptools import setup

setup(
    name='controller_manager_msgs',
    version='4.17.0',
    packages=find_packages(
        include=('controller_manager_msgs', 'controller_manager_msgs.*')),
)
