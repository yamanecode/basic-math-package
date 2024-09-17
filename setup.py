from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="basic-math-testpack",
    version="0.0.1",
    author="Andre",
    author_email="yamane.a.contact@gmail.com",
    description="Basic math functions just to test the package construction",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yamanecode/basic-math-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)