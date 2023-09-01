from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netwix',
    version='0.1.5',
    license='MIT',
    description='Netwix is a python client for Netflix. With netwix by simply entering the Netflix ID the user can access data related to movies and tv shows available on Netflix',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='new92',
    author_email='new92github@gmail.com',
    maintainer='new92',
    maintainer_email='new92github@gmail.com',
    url='https://www.github.com/new92/netwix',
    packages=find_packages(),
    install_requires=[
        "requests",
        "bs4"
    ]
)
