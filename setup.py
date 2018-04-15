from setuptools import setup

setuptools(
    name='shotty',
    version='0.1',
    author="Rahul Sharma",
    author_email="er.csrahul@gmail.com",
    description="Takes a snapshot of sce instances based on project tag",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/rayl15/shotty",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)