import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="BlockchainDataBase",
    version="1.1.4",
    author="David Mendez Guardado",
    author_email="demg@outlook.com",
    description="A Simple Blockchain Database.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/DEMG-DEV/SimpleBlockchainDataBase",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
