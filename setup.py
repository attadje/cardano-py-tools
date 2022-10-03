from setuptools import setup, find_packages

try:
    with open('PYPI_README.md') as f:
        LONG_DESCRIPTION = f.read()
except Exception as e:
    LONG_DESCRIPTION=""
    
    
VERSION = '0.1b0' 
DESCRIPTION = 'A python module to vizualize a signed transaction generate with the cardano-cli'
LONG_DESCRIPTION = LONG_DESCRIPTION

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="cardano_tx", 
        packages=['cardano_tx'],
        include_package_data=True,
        version=VERSION,
        author="Atta Djessy",
        author_email="djessyatta@live.fr",
        url = 'https://github.com/djessy-atta/cardano-tx-tools',
        download_url = 'https://github.com/attadje/cardano-tx-tools/archive/refs/tags/v0.1-beta.1.tar.gz',
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        install_requires=['cbor2', 'pydot', 'graphviz'],
        keywords=['CARDANO', 'VIZUALISATION'],
        license='MIT',
        tests_require=['pytest>=6.2.5', 'pytest-runner>=5.3.1', 'tqdm>=4.62.2'],
        test_suite='test',
        classifiers= [
            "Development Status :: 3 - Alpha",
            'Development Status :: 3 - Alpha',  
            'Intended Audience :: Developers',      
            'Topic :: Software Development :: Build Tools',
            'License :: OSI Approved :: MIT License', 
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.8', 
        ]
)