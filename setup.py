# To install our project locally with pip install . — so we can import our code from anywhere on our system
# To upload your package to PyPI (Python Package Index) and share it publicly or privately
# To easily manage dependencies and entry points for our project
# Its not a necessity, we can delete that file if u want to
from setuptools import setup, find_packages

setup(
    name="climate_weather_analysis",
    version="0.1",
    author=" Danylo, Karolina",
    description="A project for climate and weather data analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        # other dependencies here
    ],
    python_requires=">=3.7",
)
