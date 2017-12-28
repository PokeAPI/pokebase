from distutils.core import setup


def readme_text():
    with open('README.rst') as f:
        return f.read()


setup(
    name='pokebase',
    packages=['pokebase'],
    version='1.2.0',
    description='A Python wrapper for the friendly PokeAPI database',
    long_description=readme_text(),
    author='Greg Hilmes',
    author_email='99hilmes.g@gmail.com',
    url='https://github.com/GregHilmes/pokebase',
    keywords=['database', 'pokemon', 'wrapper'],
    install_requires=['requests'],
    license='BSD License',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ]
)
