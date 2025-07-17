""""
The setup.py is an essential part of packaging and distributing the python projects. 
It is used by setup tools to define the configuration of your project such as metadata,
dependencies and more

"""

from setuptools import find_packages,setup
from typing import List

def get_requirement()->list[str]:
    """"
    this function will return the list of the requirement
    """
    requirement_lst:list[str] = []
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("file is not found")
    
    return requirement_lst

setup(
    name = "networksecurity",
    version="0.0.1",
    author = "HimanshuPatidar",
    author_email="piyushpatidar2210@gmail.com",
    packages=find_packages(),
    install_requires = get_requirement()
)