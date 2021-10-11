#!/usr/bin/python3
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="elevator-Jocomol",
    version="0.0.2",
    author="Joel Meier",
    author_email="joelmeier08@gmail.com",
    description="Wrapper for selenium. Strives to be easy to use for everyone.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3",
        "Operating System :: Linux",
    ],
    python_requires='>=3.8.10',
)
