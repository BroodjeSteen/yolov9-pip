import os
import re

import setuptools


def get_requirements(req_path: str):
    with open(req_path, encoding='utf8') as f:
        return f.read().splitlines()


INSTALL_REQUIRES = get_requirements("requirements.txt")


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_dir, 'README.md'), encoding='utf-8') as f:
        return f.read()


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, 'yolov9', '__init__.py')
    with open(version_file, encoding='utf-8') as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


def get_author():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    init_file = os.path.join(current_dir, 'yolov9', '__init__.py')
    with open(init_file, encoding='utf-8') as f:
        return re.search(r'^__author__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


def get_license():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    init_file = os.path.join(current_dir, 'yolov9', '__init__.py')
    with open(init_file, encoding='utf-8') as f:
        return re.search(r'^__license__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


setuptools.setup(
    name='yolov9pip',
    version=get_version(),
    author=get_author(),
    author_email='aronkoppes@gmail.com',
    license=get_license(),
    description="yolov9pip",
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    url='https://github.com/BroodjeSteen/yolov9-pip',
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
