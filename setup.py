#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages
import glob


requirements = ["pyyaml",
                "nose>=1.3.7",
                "future-fstrings",
                "scabha >=2.0b1", 
                ## OMS: not a fan of this:
                # @ git+https://github.com/caracal-pipeline/scabha2",
                ## ...because it interferes with running scabha2 off a dev branch (i.e. if you have a local dev install of scabha,
                ## pip install stimela will blow it away and replace with master branch...)
                "ruamel.yaml",
                "munch",
                "omegaconf>=2.1pre1",
                "click",
                "pydantic",
                "pathos",
                "psutil",
                "rich"
                ],

PACKAGE_NAME = "stimela"
__version__ = "2.0rc1"

setup(name=PACKAGE_NAME,
      version=__version__,
      description="Dockerized radio interferometry scripting framework",
      author="Sphesihle Makhathini & RATT",
      author_email="sphemakh@gmail.com",
      url="https://github.com/ratt-ru/Stimela",
      packages=find_packages(),
      include_package_data=True,
      python_requires='>=3.6',
      install_requires=requirements,
      entry_points="""
            [console_scripts]
            stimela = stimela.main:cli
      """,
      scripts=glob.glob("stimela/cargo/cab/stimela_runscript"),
      classifiers=[],
      )
