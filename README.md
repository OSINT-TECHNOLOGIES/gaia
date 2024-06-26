<p align="center">
  <img src="https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/fceb701e-9bc0-4b83-b23e-fde301e4b703">
</p>

<!-- TOC --><a name="gaia-geospatial-aerial-images-analyser-beta"></a>
# GAIA - Geospatial & Aerial Images Analyser [BETA]

> [!NOTE]
> Please note that this program solution is currently in BETA stage and some details are potentially to be changed, more functionality may be added soon or later.
>
> Current version: 0.64b

> [!TIP]
> You can find some useful info about GAIA aspects in wiki: https://github.com/OSINT-TECHNOLOGIES/gaia/wiki

> [!TIP]
> You can contact GAIA developer by sending message on the following e-mail: osint.technologies@gmail.com

<img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/OSINT-TECHNOLOGIES/gaia?label=Last%20Release&labelColor=E98484&color=446C6C"> <img alt="GitHub" src="https://img.shields.io/github/license/OSINT-TECHNOLOGIES/gaia?label=Licensed%20with&labelColor=E98484&color=446C6C"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/OSINT-TECHNOLOGIES/gaia?label=Repo%20size&labelColor=E98484&color=446C6C">

<img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Python-yellow?logoColor=blue&labelColor=blue"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Jupyter_Notebook-orange?logoColor=blue&labelColor=grey"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-MLJAR%20Mercury-blue?logoColor=blue&labelColor=white">

<img alt="Static Badge" src="https://img.shields.io/badge/Google_EE-integrated-19830E?labelColor=0E4183&link=https%3A%2F%2Fearthengine.google.com%2F"> <img alt="Static Badge" src="https://img.shields.io/badge/OpenStreetMap-integrated-19830E?labelColor=0E4183&link=https%3A%2F%2Fearthengine.google.com%2F">

<!-- TOC start (generated with https://github.com/derlin/bitdowntoc) -->
**README Table of Contents:**

- [GAIA - Geospatial & Aerial Images Analyser [BETA]](#gaia-geospatial-aerial-images-analyser-beta)
   * [What is GAIA and how can I use it?](#what-is-gaia-and-how-can-i-use-it)
   * [GAIA demo screenshots](#gaia-demo-screenshots)
   * [Supported imagery and map services](#supported-imagery-and-map-services)
   * [How to start researching with GAIA](#how-to-start-researching-with-gaia)
      + [Connecting Google Earth Engine](#connecting-google-earth-engine)
      + [Connecting OpenStreetMap](#connecting-openstreetmap)
   * [System requirements ](#system-requirements)

<!-- TOC end -->

<!-- TOC --><a name="what-is-gaia-and-how-can-i-use-it"></a>
## What is GAIA and how can I use it?

GAIA is a program created using Mercury Framework ([runmercury.com](https://github.com/mljar/mercury)), Google Earth Engine ([earthengine.google.com](https://earthengine.google.com/)) and OpenStreetMap ([openstreetmap.org](https://www.openstreetmap.org)) specially for those who works with geospatial images of Earth or interested in this subject. This program implements the idea of getting as much sources of sattelite and aerial images as it possible in one app. It allows you to get planetary images from different providers using APIs of various services and, what is important, without any coding knowledge and in a pleasant web interface

<!-- TOC --><a name="gaia-demo-screenshots"></a>
## GAIA demo screenshots

1) Fires map in South America, visualised using NASA FIRMS
![firms](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/b56e5691-e99b-407c-bdc6-fc2dd8fb157c)

2) North Gaza visualised using Sentinel-2 MSI during October 2023 conflict
![north_gaza](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/ccbd4d38-3da6-454c-ac8d-e16f4eb2b287)

3) Google Earth Engine integrated knowledge base
![knowledge_base](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/13845139-f6f4-4e44-b682-757259223209)

4) OpenStreetMap GeoJSON file processing
![osmgeojson](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/4f7cd31f-71bf-4337-acfb-41ed1c630897)

<!-- TOC --><a name="supported-imagery-and-map-services"></a>
## Supported imagery and map services

> **Google Earth Engine.** This service combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities. Scientists, researchers, and developers use Earth Engine to detect changes, map trends, and quantify differences on the Earth's surface. Earth Engine is now available for commercial use, and remains free for academic and research use. Support has been added with 0.3b update.

> **OpenStreetMap.** OSM is a collaborative project for world mapping using data from various sources and volunteers. In GAIA you can get, use and explore different OSM-provided maps with different additional functions. Support has been added with 0.4b update.

<!-- TOC --><a name="how-to-start-researching-with-gaia"></a>
## How to start researching with GAIA

**The very first step on your way to start researching using GAIA is installing necessary requirements. You can install them using setup.py script**

**Your second step is integrated services connection. Instructions below will help you to properly configure and connect them to GAIA**

<!-- TOC --><a name="connecting-google-earth-engine"></a>
### Connecting Google Earth Engine

To start researching using Google Earth Engine you need to:

1) Register on Google Earth Engine using your Google account (https://code.earthengine.google.com/register) OR start GAIA using start.bat and press EE registration button
2) Register a new project with unpaid usage, choose any type of project you want and name it however you want 
3) Confirm everything you've chosen
4) Go to https://console.cloud.google.com/iam-admin/serviceaccounts/ and create service account for your project. 
5) Once service account created, click the menu for that account, then Create key > JSON. Download the JSON key file and put it in GAIA directory
6) Open GAIA in web interface and if you don't see any errors and see the map - congratulations, you've just finished Google EE connection procedure. Now you can start using GAIA with Google EE

<!-- TOC --><a name="connecting-openstreetmap"></a>
### Connecting OpenStreetMap

Basically you don't need to do any things out of GAIA to start researching using OpenStreetMap. You need only to install new libraries from system requirements and you'll be ready to start your research using OSM.


**After all needed services are connected, you can start your research. In order to do this you need to start GAIA web-interface using start.bat script which will open welcome window in your default browser.**

<!-- TOC --><a name="system-requirements"></a>
## System requirements 

**Software requirements:**

1) OS Windows 10/11 
2) Python 3.10 and above (lower versions won't guarantee correct and stable work)
3) PIP package installer

**Installed Python libraries (all of them can be installed using setup.py script):**

1) ee==0.2
2) earthengine-api==0.1.392
3) mercury==2.3.7
4) colorama==0.4.6
5) osmnx==1.7.0
6) contextily==1.4.0
7) folium==0.16.0
8) future==0.18.3
9) eefolium==0.2.0
10) ipyleaflet==0.18.2

*Network:** High-Speed Broadband Internet connection for good experience with datasets downloading
