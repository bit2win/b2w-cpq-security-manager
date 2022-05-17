import setuptools

PAKAGE_NAME = "b2w-cpq-security-manager"
PROJECT_URL = "https://github.com/bit2win/b2w-cpq-security-manager.git"
INIT_DIR = "security_manager_api"
DESCRIPTION = "CPQ Security Manager API"

VERSION = open(f"{INIT_DIR}/_version.py").readlines()[-1].split()[-1].strip("\"'")

with open("README.md", "r") as fh:
    long_description = fh.read()


def get_required_packages():

    versioned_packages = {}
    try:
        with open("modules.ver") as myfile:
            for line in myfile:
                name, var = line.partition("=")[::2]
                versioned_packages[name.strip()] = var.strip()
    except Exception:
        pass

    packages_versions = []
    required_packages = [
        "fastapi",
        "uvicorn",
        "sqlalchemy<1.4",
        "requests",
        "asyncio",
        "b2w-cpq-module-db",
        "b2w-cpq-module-exception",
        "b2w-cpq-module-cache",
        "b2w-cpq-module-utils",
        "b2w-cpq-data",
        "b2w-cpq-publish",
        "b2w-keycloak",
    ]
    for package in required_packages:
        if package in versioned_packages:
            packages_versions.append(f"{package}=={versioned_packages[package]}")
        else:
            packages_versions.append(package)
    return packages_versions


setuptools.setup(
    name=PAKAGE_NAME,
    version=VERSION,
    author="bit2win",
    author_email="bit2win@bit2win.com",
    description=DESCRIPTION,
    long_description=long_description,
    url=PROJECT_URL,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Bit2win License",
        "Operating System :: OS Independent",
    ],
    install_requires=get_required_packages(),
    tests_require=["pytest"],
)
