from setuptools import setup, find_packages

setup(
	name='dpp-package',
	version='0.1',
	packages=find_packages(exclude=['tests*']),
	license='MIT',
	description='Example DPP package',
	long_description=open('README.md').read(),
	url='https://github.com/dorianwalega96/DPP',
	author='Dorian Walega',
	author_email='dorianwalega96@gmail.com'
)
