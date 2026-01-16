from setuptools import find_packages,setup
from typing import List
hyphen_e_dot = '-e .'
def get_requirements(file_path: str)->list[str]:
    '''
    Docstring for get_requirements
    
    :param file_path: Description
    :type file_path: str
    :return: Description
    :rtype: list[str]
    '''
    requirements = []
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='Ml Project',
    version='0.0.1',
    author='Amar',
    author_email='amarbarade6@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)