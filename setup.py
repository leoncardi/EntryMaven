from setuptools import setup

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name='EntryMaven',
    version='0.0.3',
    license='MIT License',
    author='Leonardo Cardillo',
    long_description=readme,
    long_description_content_type="text/markdown",
    keywords='entrymaven entry maven leoncardi leonardo cardillo custom customizable logger loggers logging logs log',
    description=u'Simple and efficient customizable logger for Python',
    packages=['entrymaven']
)