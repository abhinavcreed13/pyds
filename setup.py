import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyds",
    version="0.0.2",
    author="Abhinav Sharma",
    author_email="abhinavcs13@gmail.com",
    description="Data Structures Implementation in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abhinavcreed13/pyds",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)