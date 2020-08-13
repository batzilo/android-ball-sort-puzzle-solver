"""The setup.py file."""

from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fh:
    requirements = fh.read().splitlines()

with open("requirements-dev.txt") as fh:
    tests_requirements = [
        r for r in fh.read().splitlines() if "-r requirements.txt" not in r
    ]

setup(
    name="android-bubble-sort-puzzle-solver",
    version="0.0.1",
    author="Vasileios Souleles",
    author_email="vasilis.souleles@gmail.com",
    description="Solve the Android Bubble Sort Puzzle",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/batzilo/android-ball-sort-puzzle-solver",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    install_requires=requirements,
    tests_require=tests_requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "android-bubble-sort-puzzle-solver = solver.solver:main"
        ]
    },
)
