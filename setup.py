import setuptools

with open('README.md', "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="simple-paramiko",
    version="0.0.1",
    author="Sergey Parshin",
    author_email="parshinsp@gmail.com",
    description="Simplified Paramiko connection package. That allows command execution without any configuration headache.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Shooshp/simple-paramiko",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
