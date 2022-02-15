import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="v_diffusion_pytorch",
    py_modules=["v_diffusion_pytorch"],
    version="1.0",
    description="",
    author="Katherine Crowson (crowsonkb)",
    packages=find_packages(),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    extras_require={},
)
