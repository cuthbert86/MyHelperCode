from setuptools import setup, find_packages

setup(
    name="myhelpercode",                    # PyPI package name (lowercase)
    version="0.1.0",                        # Semantic versioning (major.minor.patch)
    author="Cuthbert Baines",
    author_email="cuthbertbaines@gmail.com",
    description="Useful helper functions for MicroPython on Pico",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/cuthbert86/MyHelperCode",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: MicroPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="micropython pico helpers utilities",
)
