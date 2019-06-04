import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robo-components-kashank",
    version="0.0.1",
    author="Kyle Shankin",
    author_email="kyle.shankin@gmail.com",
    description="A library which provides implementations for robotics components on the raspberry pi.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kashank/robo-components",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU General Public License v3.0",
        "Operating System :: Raspbian",
    ],
)