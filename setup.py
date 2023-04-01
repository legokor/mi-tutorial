from setuptools import find_packages, setup  # type: ignore

DESCRIPTION = "Python tutorial & template project"

setup(
    name="tuttemp",
    version="0.1",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    # author_email="dev@org.com",
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["*.py"]},
    install_requires=[],
)
