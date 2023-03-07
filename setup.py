from setuptools import setup, find_packages
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="manga-dl0",
    version="0.0.2",
    author="Dexter",
    author_email="",
    description="A Python Package To Download Manga From Arabic Site [3asq]",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dexter-90/manga-dl0",
    install_requires=['requests', 'bs4', 'img2pdf'],
    project_urls={
        "Bug Tracker": "https://github.com/mahesh-maximus/helloworld-pyp/issues",
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11', ],
    package_dir={'': "src"},
    packages=find_packages("src"),
    python_requires=">=3.7",
)
