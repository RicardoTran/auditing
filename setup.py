from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in auditing/__init__.py
from auditing import __version__ as version

setup(
	name="auditing",
	version=version,
	description="Soft for all auditing company",
	author="TS68 Company",
	author_email="toantm@ts68.vn",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
