from setuptools import setup, find_packages

setup(
    name='snscrape',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'requests[socks]',
        'lxml',
        'beautifulsoup4',
        'filelock',
        'pytz;python_version<"3.9.0"'
    ],
    entry_points={
        'console_scripts': [
            'snscrape=snscrape._cli:main',
        ],
    }
)