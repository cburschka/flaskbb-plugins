# -*- coding: utf-8 -*-
"""
    conversations
    ~~~~~~~~~~~~~

    Private messaging for FlaskBB

    :copyright: (c) 2018 by Peter Justin.
    :license: BSD License, see LICENSE for more details.
"""
import ast
import re

from setuptools import find_packages, setup


with open("conversations/__init__.py", "rb") as f:
    version_line = re.search(
        r"__version__\s+=\s+(.*)", f.read().decode("utf-8")
    ).group(1)
    version = str(ast.literal_eval(version_line))


setup(
    name="flaskbb-plugin-conversations",
    version=version,
    url="https://flaskbb.org",
    license="BSD License",
    author="Peter Justin",
    author_email="peter.justin@outlook.com",
    description="Private messaging for FlaskBB",
    long_description=__doc__,
    keywords="flaskbb plugin conversations messaging",
    packages=find_packages("."),
    include_package_data=True,
    package_data={
        "": ["conversations/translations/*/*/*.mo",
             "conversations/translations/*/*/*.po"]
    },
    zip_safe=False,
    platforms="any",
    entry_points={
        "flaskbb_plugins": [
            "conversations = conversations"
        ]
    },
    install_requires=[
        "FlaskBB>=2.0.dev0"
    ],
    setup_requires=[
        "Babel",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Environment :: Plugins",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
)
