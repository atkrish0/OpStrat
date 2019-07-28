from setuptools import setup
import re

with open("README.md", "r") as f:
    desc = f.read()
    desc = desc.split("<!-- content -->")[-1]
    desc = re.sub("<[^<]+?>", "", desc)  # Remove html


setup(
    name="OpStat",
    version="0.0.2",
    description="Implementations of Financial Derivative Options Trading Strategies",
    long_description=desc,
    long_description_content_type="text/markdown",
    url="https://github.com/atheesh1998/OpStrat",
    author="Atheesh Krishnan",
    author_email="atheesh.krishnan@outlook.com",
    license="MIT",
    packages=["opstrat"],
    classifiers=[
        "Development Status :: 1 - Beta",
        "Environment :: Console",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    keywords="derivatives options futures finance optimization quant trading investing",
    install_requires=["numpy", "pandas", "scikit-learn", "scipy", "noisyopt", "matplotlib"],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    python_requires=">=3",
)