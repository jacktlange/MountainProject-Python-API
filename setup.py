import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MountainProjectPublicAPI",
    version="0.1.0",
    author="Jack Lange",
    author_email="jacktlange@gmail.com",
    description="Python Wrapper for Mountain Project public data API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacktlange/MountainProject-Python-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
