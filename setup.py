from distutils.core import setup
setup(
    name='pokebase',
    packages=['pokebase'],
    version='1.0',
    description='A Python wrapper for the friendly PokeAPI database',
    author='Greg Hilmes',
    author_email='99hilmes.g@gmail.com',
    url='https://github.com/GregHilmes/pokebase',
    download_url='https://github.com/GregHilmes/pokebase/archive/1.0.tar.gz',
    keywords=['database', 'pokemon', 'wrapper'],
    install_requires=['requests'],
)
