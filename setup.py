from setuptools import setup, find_packages

setup(
    name='templater-cli',
    version='0.1',
    author='Sayam.py',
    author_email='sujata.howrah.belgachia@gmail.com',
    description='Template Project Manager',
    
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        
    ],
    entry_points='''
        [console_scripts]
        tmt=templater.main:main
    ''',
)
