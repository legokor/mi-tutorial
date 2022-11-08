from setuptools import find_packages, setup  # type: ignore

DESCRIPTION = "Lego MI Turorial"

setup(
    name="lego-mi-tutorial",
    version="0.1",
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    package_dir={"": "src"},
    packages=find_packages("src"),
    package_data={"": ["*.py"]},
    install_requires=[],
)
