from setuptools import setup, find_packages

setup(
name="ft_package",
version="0.0.1",
packages=find_packages(),
description="A sample test package",
long_description=(open("README.md").read()),
long_description_content_type="text/markdown",
author="eagle",
author_email="eagle@42.fr",
url="https://github.com/eagle/ft_package",
license="MIT",
classifiers=["License:: OSI Approved :: MIT License", "Programming Language :: Python :: 3"],
python_requires=">=3.6",
)