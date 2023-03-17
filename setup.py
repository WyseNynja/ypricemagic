from os import environ
from setuptools import find_packages, setup

if environ.get("YPRICEMAGIC_LIB", "0") == "1":
    requirements_filename = "requirements.in"
else:
    requirements_filename = "requirements.txt"

with open(requirements_filename, "r") as f:
    requirements = list(map(str.strip, f.read().split("\n")))[:-1]

setup(
    name="ypricemagic",
    packages=find_packages(),
    use_scm_version={
        "root": ".",
        "relative_to": __file__,
        "local_scheme": "no-local-version",
        "version_scheme": "python-simplified-semver",
    },
    description="Use this tool to extract historical on-chain price data from an archive node. Shoutout to @bantg and @nymmrx for their awesome work on yearn-exporter that made this library possible.",
    author="BobTheBuidler",
    author_email="bobthebuidlerdefi@gmail.com",
    url="https://github.com/BobTheBuidler/ypricemagic",
    license="MIT",
    install_requires=requirements,
    setup_requires=[
        "setuptools_scm",
    ],
)
