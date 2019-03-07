from setuptools import setup

setup(
    name='easy_daemon',
    version='0.0.3',
    packages=['easy_daemon'],
    requires=[],
    url='https://github.com/oleglpts/easy_daemon',
    license='MIT',
    platforms='any',
    author='Oleg Lupats',
    author_email='oleglupats@gmail.com',
    description='Easy daemon base class',
    long_description='Very simple base daemon class. Just override method \'run\'. See examples',
    classifiers=[
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
