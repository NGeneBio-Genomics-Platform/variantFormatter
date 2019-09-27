#!/usr/bin/env python

# Prefer setuptools over distutils
from setuptools import setup, find_packages

setup(
    name='VariantFormatter',
    version=open('VERSION.txt').read(),
    description='Accurate conversion of Pseudo VCF variants into the HGVS format and mapping between reference sequences',
    long_description=open('README.txt').read(),
    url='https://github.com/openvar/variantFormatter',
    author='Peter J. Causey-Freeman',
    author_email='admin@variantvalidator.org',
    packages=find_packages(),
    include_package_data=True,
    license="GNU AFFERO GENERAL PUBLIC LICENSE, Version 3 (https://www.gnu.org/licenses/agpl-3.0.en.html)",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Audience
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Specify the Python versions
        'Programming Language :: Python',
    ],
 
    # What does your project relate to?
      keywords=[
          "bioinformatics",
          "computational biology",
          "genome variants",
          "genome variation",
          "genomic variants",
          "genomic variation",
          "genomics",
          "hgvs",
          "HGVS",
          "sequencevariants",
      ],

    # List run-time dependencies here.  These will be installed by pip when the project is installed.
    install_requires=[
        "VariantValidator >= 1.0.0", # This will install BioPython
        "hgvs==1.3.0.post0"
    ],
)

# <LICENSE>
# Copyright (C) 2019  Peter Causey-Freeman, University of Manchester
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# </LICENSE>