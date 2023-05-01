from setuptools import setup, find_packages

with open("README.md") as f:
	long_description = f.read()

setup(
	name="tdfmt",
	version="0.0.4",
	author="Briano Goestiawan",
	author_email="b@briano.io",
	description="tdfmt formats datetime.timedelta",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/bbriano/tdfmt",
	packages=find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
		"License :: OSI Approved :: ISC License (ISCL)"
	],
	python_requires=">=3"
)
