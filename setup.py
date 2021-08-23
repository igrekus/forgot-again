from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Simple helpers'
LONG_DESCRIPTION = 'Simple helper functions you always have to write from scratch.'

setup(
    name="forgot-again",
    version=VERSION,
    author="igrekus",
    author_email="",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)
