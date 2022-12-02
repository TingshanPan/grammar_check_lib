# from distutils.core import setup
from setuptools import setup, find_packages

import pathlib

current_location = pathlib.Path(__file__).parent
readme = (current_location / "README.md").read_text()

setup(
    name = 'grammarlib',
    packages = find_packages(),
    version = '1.0.0',
    license='Apache 2.0',
    description = ".",
    long_description= readme,
    long_description_content_type='text/markdown',
    author = "The AI Grammar Check Development Team",
    author_email = 'tingshan1114@gmail.com',
    url = 'https://github.com/TingshanPan/grammar_check_lib',
    keywords = ['bert', 'roberta', 'xlnet', "transformer",  "nlp", "nlu", "natural", "language", "processing", "grammar"],

    install_requires=[
            'torch>=1.0',
            'tqdm>=4.43',
            'transformers>=4.4.0',
            'datasets>=1.6.0',
            'dataclasses; python_version < "3.7"',
            'sentencepiece',
            'protobuf'

    ],
    classifiers=[
        'Intended Audience :: Developers',
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",

      ],
    )