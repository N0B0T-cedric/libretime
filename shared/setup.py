from os import chdir
from pathlib import Path

from setuptools import setup

# Change directory since setuptools uses relative paths
here = Path(__file__).parent.resolve()
chdir(here)

setup(
    name="libretime-shared",
    version="1.0.0",
    description="LibreTime Shared",
    url="http://github.com/libretime/libretime",
    author="LibreTime Contributors",
    license="AGPLv3",
    packages=["libretime_shared"],
    package_data={"": ["py.typed"]},
    install_requires=[
        "click~=8.0.4",
        "loguru==0.6.0",
        "pydantic>=1.7.4,<1.10",
        "pyyaml>=5.3.1,<6.1",
    ],
    extras_require={
        "dev": [
            "types-pyyaml",
        ],
    },
)
