import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python-mysql-manager",
    version="1.3.0.0",
    author="Stephen Ayre",
    author_email="stevemamajama@gmail.com",
    description="A wrapper for simplifying python mysql operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stevekineeve88/python-mysql-manager.git",
    packages=setuptools.find_packages(),
    install_requires=[
        "mysql-connector-python"
    ],
    python_requires='>=3.8'
)