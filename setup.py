from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='manga-dl0',
    version='0.0.1',
    author='Dexter',
    description='A Python Package To Download Manga From Arabic Site [3asq]',
    long_description=long_description,
    url='https://github.com/dexter-90/manga-dl0',
    keywords='manga, 3asq, arabic, download',
    python_requires='>=3.7',
    package_dir={'': "src"},
    packages=find_packages("src"),
    install_requires=[
        'requests',
        'bs4',
        'beautifulsoup4',
        'Pillow'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11', ],

)
