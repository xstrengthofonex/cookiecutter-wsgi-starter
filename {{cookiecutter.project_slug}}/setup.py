from setuptools import setup, find_packages

requires = [
    "waitress",
    "webob",
]

tests_require = [
    "chromedriver_installer",
    "selenium",
    "WebTest",
]

setup(
    name="{{cookiecutter.project_slug}}",
    version="{{cookiecutter.version}}",
    description="{{cookiecutter.description}}",
    author="{{cookiecutter.author_name}}",
    author_email="{{cookiecutter.author_email}}",
    url="{{cookiecutter.url}}",
    packages=find_packages(),
    extras_require={
        'testing': tests_require},
    install_requires=requires,
    entry_points={}
)
