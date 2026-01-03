from setuptools import find_packages,setup
 
def get_requirements(file_path:str)-> List[str]:
    
    
    "this function will retun the list of requirments" 
    
    
     requirments=[] 
     with open(requirements.txt) as file_obj:
         requirements=file_obj.readlines()
         requirements=[req.replace("\n","") for req in requirements]
         
           if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements

setup (
name = 'mlproject',
version='0.0.1',
author= 'Ema',
author_email:effatema17@cse.pstu.ac.bd,
packages= find_packages(),
install_requires=get_requirements('requirement.txt')

)