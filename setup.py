from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in tacten_client_feedback/__init__.py
from tacten_client_feedback import __version__ as version

setup(
	name="tacten_client_feedback",
	version=version,
	description="Client Feedback Tool",
	author="Tacten Services LLP",
	author_email="info@tacten.co",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
