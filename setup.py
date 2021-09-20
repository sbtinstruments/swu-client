"""Setup of swu_client."""
import os
from setuptools import find_packages, setup


name = 'swu_client'


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def _read(fname):
	with open(os.path.join(os.path.dirname(__file__), fname)) as readme:
		return readme.read()


setup(
	name=name,
	version="0.1.0",
	author='Frederik Aalund',
	author_email='fpa@sbtinstruments.com',
	description=('Simple SWUpdate HTTP client.'),
	license='MIT',
	keywords='swupdate http client',
	url='https://sbtinstruments.com',
	packages=find_packages(),
	long_description=_read('README.md'),
	include_package_data=True,
	install_requires=[
		'aiohttp',
	],
	scripts = ['scripts/swu_client'],
	classifiers=[
		'Development Status :: 4 - Beta',
		'Topic :: Utilities',
    	"License :: OSI Approved :: MIT License",
	],
)
