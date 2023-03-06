import setuptools
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="manga-dl4",
    version="0.0.2",
    author="Dexter",
    author_email="",
    description="A Python Package To Download Manga From Arabic Site [3asq]",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dexter-90/manga-dl4",
    install_requires=['requests', 'bs4', 'img2pdf'],
    project_urls={
        "Bug Tracker": "https://github.com/mahesh-maximus/helloworld-pyp/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    package_dir={'':"src"},
    packages=find_packages("src"),
    python_requires=">=3.6",
)
