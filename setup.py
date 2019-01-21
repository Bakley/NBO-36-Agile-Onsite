from setuptools import setup
setup(
    name='nbo-agile',
    version='0.1',
    entry_points='''
        [console_scripts]
        nbo-agile=main:getUsers
    ''',
)