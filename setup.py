from setuptools import setup, find_packages
import codecs
import os

# Get the directory containing this file
here = os.path.abspath(os.path.dirname(__file__))

# Read the README file for the long description
with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

# Define the package version
VERSION = "0.1.0"  # Initial version for edgestream

# Package description
DESCRIPTION = "edgestream: A Python library for seamless sensor data acquisition and logging."
LONG_DESCRIPTION = (
    "edgestream is a Python library developed by EdgeNeuron, designed for efficient sensor data acquisition, "
    "real-time processing, and logging. The library integrates with edge devices to streamline data pipelines for "
    "machine learning and IoT applications."
)

# Define the setup configuration
setup(
    name="edgestream",  # Unique package name for edgestream
    version=VERSION,
    author="EdgeNeuron",
    author_email="support@edgeneuron.ai",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ConsentiumIoT/EdgeStream",  # Repository URL
    packages=find_packages(),  # Automatically discover all packages
    install_requires=[
        "numpy",  # For numerical operations
        "pandas",  # For data logging and manipulation
        "pyserial",  # For serial port communication
        "tensorflow",  # If required for ML integrations
    ],
    extras_require={
        "dev": [
            "pytest",  # Testing framework for development
            "flake8",  # Linter for code quality
            "black",  # Code formatter
        ]
    },
    keywords=[
        "Python",
        "Edge Computing",
        "IoT",
        "Sensor Data",
        "Data Logging",
        "EdgeNeuron",
        "edgestream",
        "Machine Learning",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",  # Updated to Beta for edgestream
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",  # Specify the minimum supported Python version
    project_urls={
        "Bug Tracker": "https://github.com/EdgeNeuron/edgestream-py/issues",
        "Documentation": "https://github.com/EdgeNeuron/edgestream-py#readme",
        "Source Code": "https://github.com/EdgeNeuron/edgestream-py",
    },
)
