from setuptools import setup

setup(
    name='Snapshotalyzer',
    version='0.1',
    author='Marcel van Noort',
    author_email='marcel@zag.team',
    description='Snapshotalyzer is a tool to manage AWS EC2 snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/marcelvn1104/snapshotalyzer',
    install_requires=['click','boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    '''
)
