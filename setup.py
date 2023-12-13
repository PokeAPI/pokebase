import setuptools


def readme_text():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    name='pokebase',
    packages=['pokebase'],
    version='1.3.1',
    description='A Python wrapper for the friendly PokeAPI database',
    long_description=readme_text(),
    author='Greg Hilmes',
    author_email='99hilmes.g@gmail.com',
    url='https://github.com/PokeAPI/pokebase',
    keywords=['database', 'pokemon', 'wrapper'],
    install_requires=['requests'],
    license='BSD License',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ]
)
