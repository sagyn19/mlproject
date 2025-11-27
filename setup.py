from setuptools import setup, find_packages

def get_requires(file_path: str) -> list[str]:
    requires = []
    with open(file_path, "r") as file:
        requires = file.readlines()
        requires = [req.replace("\n", "") for req in requires]

        if "-e ." in requires:
            requires.remove("-e .")

    return requires
    

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    author="Sagyn",
    install_requires=get_requires("requirements.txt"),
)