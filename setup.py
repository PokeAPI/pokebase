from distutils.core import setup
setup(
    name='pokebase',
    packages=['pokebase'],
    version='1.0.0',
    description='A Python wrapper for the friendly PokeAPI database',
    author='Greg Hilmes',
    author_email='99hilmes.g@gmail.com',
    url='https://github.com/GregHilmes/pokebase',
    download_url='https://github.com/GregHilmes/pokebase/archive/1.0.0.tar.gz',
    keywords=['database', 'pokemon', 'wrapper'],
    install_requires=['requests'],
    license='BSD License',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ]
)
