from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_file = f.read()

setup(
    name='openfema-api-python-client',
    version='0.1.0',
    description='OpenFEMA API Client Library for Python',
    python_requires=">=3.7",
    long_description=readme,
    author='Drew Lindsey',
    author_email='drew.a.lindsey@gmail.com',
    url='https://github.com/schemeflex/openfema-api-python-client',
    license=license_file,
    packages=find_packages(exclude=('tests', 'docs'))
)