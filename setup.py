from setuptools import setup, find_packages

setup(
    name='neuronum',
    version = '2026.10.1',
    author='Neuronum Cybernetics',
    author_email='welcome@neuronum.net',
    description='Python client for the Neuronum AI Network',
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://neuronum.net",
    project_urls={
        "GitHub": "https://github.com/neuronumnet/neuronum-sdk-python",
        "Documentation": "https://neuronum.net/docs",
    },
    packages=find_packages(include=["neuronum"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'aiohttp',
        'click',
        'questionary',
        'requests',
        'cryptography',
        'mnemonic',
        'fastmcp',
    ],
    entry_points={
        "console_scripts": [
            "neuronum=neuronum.cli:cli",
            "neuronum-mcp=neuronum.mcp:main",
        ]
    },
    python_requires='>=3.10,<3.15',
)
