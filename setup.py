from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='netwix',
    version='0.1.8',
    license='MIT',
    description='Netwix is a python client for Netflix. With netwix by simply entering the Netflix ID the user can access data related to movies and tv shows available on Netflix',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='new92',
    author_email='new92github@gmail.com',
    maintainer='new92',
    maintainer_email='new92github@gmail.com',
    keywords='python netflix movies series data retrieval module',
    url='https://www.github.com/new92/netwix',
    packages=find_packages(),
    install_requires=[
        "requests",
        "bs4"
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.6',
    project_urls={
        'Github Repository': 'https://github.com/new92/netwix'
    }
)
