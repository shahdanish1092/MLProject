from setuptools import find_packages, setup
from typing import List


HYPHEN = "-e ."

def get_requirements(file_path:str) -> List[str]:

    '''
    Find the required packages and install accordingly
    '''

    requirement_list = []

    with open(file_path) as file_obj:

        requirement_list = file_obj.readlines()

        requirement_list = [req.replace("\n"," ") for req in requirement_list]

        if HYPHEN in requirement_list:

            requirement_list.remove(HYPHEN)

    return requirement_list






setup(
    name="mlproject",
    version="0.0.1",
    author="danish",
    author_email="danishshah9749@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)