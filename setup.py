from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list of requirements from requirements.txt
    :param file_path:
    :return:
    '''
    requirements = []
    with open(file_path, 'r') as f:
        requirements=f.readline()
        requirements=[i.replace("\n",'')  for i in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name='practiceml',
    version='0.0.1',
    author='Fahim',
    author_email='fjaragal@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements('requirements.txt')
)