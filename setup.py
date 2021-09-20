import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "oneNeuron.pypi"
USER_NAME = "pk_164"


setuptools.setup(
    name="f{PROJECT_NAME}-{USER_NAME}",
    version="0.0.1",
    author= USER_NAME,
    author_email="pavanram2000@gmail.com",
    description="A small implimentation of perceptron",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pavan164-ml/oneNeuron_pypi",
    project_urls={
        "Bug Tracker": "https://github.com/Pavan164-ml/oneNeuron_pypi/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    install_requires=["numpy","tqdm"]
)