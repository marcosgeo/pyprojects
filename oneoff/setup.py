import os, sys, re

# get version info from module withou importing it
version_re = re.compile("""__version___[\s]*=[\s]*['|"](.*)['|"]""")

with open("helloworld.py") as f:
    content = f.read()
    match = version_re.search(content)
    version = match.group(1)


readme = os.path.join(os.path.dirname(__file__), "README.md")
long_description = open(readme).read()


SETUP_ARGS = dict(
    name="helloworld",
    version=version,
    description=("Grabs the 'Hello World' Wikipedia page and prints its title"),
    long_description=long_description,
    url="https://github.com/marcosgeo/pyprojects/oneoff",
    author="antonio marcos",
    author_email="marcosgeo@yahoo.com",
    licence="Apache 2.0",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Intend Audience :: Developers",
        "License :: OSI Approved :: Apache 2.0",
        "Operational System :: OS Independent",
        "Programming Language :: Python :: 3.6",
    ],
    py_mudules = ["helloword",],
    install_requires = [
        "requests>=2.2"
    ],
)

if __name__ == "__main__":
    from setuptools import setup, find_packages

    SETUP_ARGS["packages"] = find_packages()
    setup(**SETUP_ARGS)
