import os
import re
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def find_version(fname):
    '''Attempts to find the version number in the file names fname.
    Raises RuntimeError if not found.
    '''
    version = ''
    with open(fname, 'r') as fp:
        reg = re.compile(r'__version__ = [\'"]([^\'"]*)[\'"]')
        for line in fp:
            m = reg.match(line)
            if m:
                version = m.group(1)
                break
    if not version:
        raise RuntimeError('Cannot find version information')
    return version


__version__ = find_version(os.path.join("flask_page", "__init__.py"))

setup(
    name='flask_page',
    version=__version__,
    long_description=read('README.md'),
    packages=['flask_page'],
    url='http://github.com/yoophi/flask-page',
    license='MIT License',
    author='Pyunghyuk Yoo',
    author_email='yoophi@gmail.com',
    description='Jinja2 static template page route for Flask',
    include_package_data=True,
    zip_safe=False,
    entry_points={
    },
    install_requires=[
        'Flask==0.10.1',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)

