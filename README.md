<p align="center">
  <img src="https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/fceb701e-9bc0-4b83-b23e-fde301e4b703">
</p>

# GAIA - Geospatial & Aerial Images Analyser [BETA]

[!] This program solution is not final and some details are potentially to be changed [!]

[!] More services support and functions will be added soon or later [!]

[!] Current version - 0.41b [!]

<img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/OSINT-TECHNOLOGIES/gaia?label=Last%20Release&labelColor=E98484&color=446C6C"> <img alt="GitHub" src="https://img.shields.io/github/license/OSINT-TECHNOLOGIES/gaia?label=Licensed%20with&labelColor=E98484&color=446C6C"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/OSINT-TECHNOLOGIES/gaia?label=Repo%20size&labelColor=E98484&color=446C6C">

<img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Python-yellow?logoColor=blue&labelColor=blue"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Jupyter_Notebook-orange?logoColor=blue&labelColor=grey"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-MLJAR%20Mercury-blue?logoColor=blue&labelColor=white">

<img alt="Static Badge" src="https://img.shields.io/badge/Google_EE-integrated-19830E?labelColor=0E4183&link=https%3A%2F%2Fearthengine.google.com%2F"> <img alt="Static Badge" src="https://img.shields.io/badge/OpenStreetMap-integrated-19830E?labelColor=0E4183&link=https%3A%2F%2Fearthengine.google.com%2F">


**If you want to contact the developer about GAIA - write here:** osint.technologies@gmail.com


## What is GAIA and how can I use it?

GAIA is a program created using Mercury Framework ([runmercury.com](https://github.com/mljar/mercury)), Google Earth Engine ([earthengine.google.com](https://earthengine.google.com/)) and OpenStreetMap ([openstreetmap.org](https://www.openstreetmap.org)) specially for those who works with geospatial images of Earth or interested in this subject. This program implements the idea of getting as much sources of sattelite and aerial images as it possible in one app. It allows you to get planetary images from different providers using APIs of various services and, what is important, without any coding knowledge and in a pleasant web interface

## GAIA demo screenshots

1) Fires map in South America, visualised using NASA FIRMS
![firms](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/b56e5691-e99b-407c-bdc6-fc2dd8fb157c)

2) North Gaza visualised using Sentinel-2 MSI during October 2023 conflict
![north_gaza](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/ccbd4d38-3da6-454c-ac8d-e16f4eb2b287)

3) Google Earth Engine integrated knowledge base
![knowledge_base](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/13845139-f6f4-4e44-b682-757259223209)

4) OpenStreetMap GeoJSON file processing
![osmgeojson](https://github.com/OSINT-TECHNOLOGIES/gaia/assets/77023667/4f7cd31f-71bf-4337-acfb-41ed1c630897)

## Supported imagery and map services

> **Google Earth Engine.** This service combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities. Scientists, researchers, and developers use Earth Engine to detect changes, map trends, and quantify differences on the Earth's surface. Earth Engine is now available for commercial use, and remains free for academic and research use. Support has been added with 0.3b update.

> **OpenStreetMap.** OSM is a collaborative project for world mapping using data from various sources and volunteers. In GAIA you can get, use and explore different OSM-provided maps with different additional functions. Support has been added with 0.4b update.

## How to start researching with GAIA

**The very first step on your way to start researching using GAIA is installing necessary requirements. You can install them using setup.py script**

**Your second step is integrated services connection. Instructions below will help you to properly configure and connect them to GAIA**

### Connecting Google Earth Engine

To start researching using Google Earth Engine you need to:

1) Register on Google Earth Engine using your Google account (https://code.earthengine.google.com/register) OR start GAIA using start.bat and press EE registration button
2) Register a new project with unpaid usage, choose any type of project you want and name it however you want 
3) Confirm everything you've chosen
4) Go to https://console.cloud.google.com/iam-admin/serviceaccounts/ and create service account for your project. 
5) Once service account created, click the menu for that account, then Create key > JSON. Download the JSON key file and put it in GAIA directory
6) Open GAIA in web interface and if you don't see any errors and see the map - congratulations, you've just finished Google EE connection procedure. Now you can start using GAIA with Google EE

### Connecting OpenStreetMap

Basically you don't need to do any things out of GAIA to start researching using OpenStreetMap. You need only to install new libraries from system requirements and you'll be ready to start your research using OSM.


**After all needed services are connected, you can start your research. In order to do this you need to start GAIA web-interface using start.bat script which will open welcome window in your default browser.**

## System requirements 

**Software requirements:**

1) OS Windows 10/11 
2) Python 3.10 and above (lower versions won't guarantee correct and stable work)
3) PIP package installer

**Installed Python libraries (all of them can be installed using setup.py script):**

1) DateTime==5.2
2) ee==0.2
3) earthengine-api==0.1.367
4) mercury==2.3.1
5) colorama==0.4.6
6) matplotlib==3.6.2
7) osmnx==1.7.0
8) contextily==1.4.0
9) folium==0.14.0
10) future==0.18.3
11) geemap==0.24.4
12) geocoder==1.38.1
13) ipyleaflet==0.17.3

**Network:** High-Speed Broadband Internet connection for good experience with datasets downloading
