import sys
import subprocess

from setuptools import find_packages, setup
from setuptools.command.install import install


class CheckJavaAndInstall(install):
    def check_java_installed(self):
        try:
            subprocess.run(["java", "-version"], check=True)
            print("Java is installed and detected.")
        except subprocess.CalledProcessError:
            print("Java is not installed or not available in PATH.")
            sys.exit(1)

    def run(self):
        self.check_java_installed()
        install.run(self)


with open("README.md") as f:
    readme = f.read()

setup(
    name="unluac",
    version="1.0.1",
    author="TooLazyToCreate",
    url="https://github.com/TooLazyToCreate/unluac_py",
    description="python bindings for the unluac tool",
    long_description=readme,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(exclude=("test",)),
    package_data={
        "unluac": ["jar/*.jar"]
    }, cmdclass={
        'install': CheckJavaAndInstall,
    },
    python_requires=">=3.8",
)