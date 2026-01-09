"""
Setup configuration for the project.
"""

from setuptools import setup, find_packages

setup(
    name="professional-dev-platform",
    version="1.0.0",
    description="A comprehensive software platform with extensive test coverage and CI/CD",
    author="Developer",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "requests>=2.31.0",
    ],
    python_requires=">=3.9",
)
