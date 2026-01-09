"""
Setup configuration for the project.
"""

from setuptools import setup, find_packages

setup(
    name="high-quality-project",
    version="1.0.0",
    description="A well-structured project with comprehensive test coverage",
    author="Developer",
    packages=find_packages(),
    install_requires=[
        "pytest>=7.0.0",
        "pytest-cov>=4.0.0",
        "requests>=2.31.0",
    ],
    python_requires=">=3.9",
)
