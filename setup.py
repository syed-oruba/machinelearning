from setuptools import setup,find_packages
from typing import List
hyphen_e_dots="-e."
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("/n", " ") for req in requirements]
        if  hyphen_e_dots in  requirements:
            requirements.remove(hyphen_e_dots)
    return requirements

setup( 
    name="mlprOjects" , 
    author="syedoruba" , 
    version=0.01 , 
    packages=find_packages(), 
    install_requires=get_requirements("requirements.txt")
)