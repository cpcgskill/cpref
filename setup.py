#!/usr/bin/python
# -*-coding:utf-8 -*-
from __future__ import unicode_literals, print_function
import setuptools

with open("README.md", "rb") as f:
    long_description = f.read().decode(encoding="utf-8")

setuptools.setup(
    name="cpref",
    version="1.0.0",
    author="cpcgskill",
    author_email="cpcgskill@outlook.com",
    description="Maya 对象引用库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cpcgskill/cpref",
    project_urls={
        "Bug Tracker": "https://github.com/cpcgskill/cpref/issues",
    },
    license="Apache Software License (Apache 2.0)",
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    package_dir={"": "src"},
    # 不使用自动搜索
    # packages=setuptools.find_packages(where="src"),
    packages=["cpref"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*",
    # 指定依赖
    install_requires=[]
)
