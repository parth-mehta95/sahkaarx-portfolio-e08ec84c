from setuptools import setup, find_packages

setup(
    name="shared-utils",
    version="0.1.0",
    description="A shared Python utility module providing reusable helpers across team projects.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(include=["shared_utils", "shared_utils.*"]),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "flake8>=6.0",
        ],
    },
)
