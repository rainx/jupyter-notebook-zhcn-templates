from setuptools import setup, find_packages
setup(
    name = "jupyter-notebook-zhcn-templates",
    version = "4.2.3",
    packages = find_packages(),
    package_data= {
        '' : ['*.js', '*.html']
    },
    install_requires = [
            'notebook==4.2.3'
        ]
)
