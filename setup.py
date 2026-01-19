from setuptools import setup, find_packages

setup(
    name="speckit",
    version="0.0.1",
    description="Speckit project placeholder for uvx initialization",
    packages=find_packages(),
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
            "specify=speckit.cli:main",
        ],
    },
)
