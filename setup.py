import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qiell-sample-pkg",
    version="0.0.1",
    author="Akash Srivastava",
    author_email="akgec.akash@gmail.com",
    description="A small example package",
    long_description="A sample package created for fun in PYcon Chennai 2019",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
