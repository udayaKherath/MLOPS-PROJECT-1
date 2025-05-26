from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="MLOPS-PROJECT-1",
    version="0.1",
    author="Udaya",
    packages=find_packages(),
    install_requires=requirements,
    py_modules=[],  # Add this if you have standalone .py files
)