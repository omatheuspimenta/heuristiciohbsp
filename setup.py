from setuptools import setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='heuristiciohbsp',
    version='1.0.0',
    url='https://github.com/omatheuspimenta/heuristiciohbsp',
    license='MIT License',
    author='Matheus Pimenta',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='matheus.pimenta@outlook.com',
    keywords='Heuristic_IOHBSP',
    description=u'Heuristic Methods for Minimizing Cut Bars and Using Leftovers from the One-dimensional Cutting Process',
    packages=['heuristiciohbsp'],)
