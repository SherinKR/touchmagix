from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in touchmagix/__init__.py
from touchmagix import __version__ as version

setup(
	name="touchmagix",
	version=version,
	description="Custom Developments for touchmagix",
	author="Indictrans",
	author_email="sherin.k@indictrans.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
