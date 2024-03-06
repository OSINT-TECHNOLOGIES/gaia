from setuptools import setup, find_packages

setup(
    name='GAIA',
    version='0.61b',
    author='OSINT-TECHNOLOGIES',
    author_email='osint.technologies@gmail.com',
    description='Geospatial & Aerial Images Analyser',
    url='https://github.com/OSINT-TECHNOLOGIES/gaia',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'ee==0.2',
        'earthengine-api==0.1.392',
        'mercury==2.3.7',
        'colorama==0.4.6',
        'matplotlib==3.6.2',
        'osmnx==1.7.0',
        'contextily==1.4.0',
        'folium==0.16.0',
        'future==0.18.3',
        'eefolium==0.2.0',
        'ipyleaflet==0.18.2'
    ],
)
