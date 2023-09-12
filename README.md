<p align="center">
      <img src="https://i.ibb.co/sH2gqVD/logo.png" width="726">
</p>

# GAIA - Geospatial & Aerial Images Analyser [BETA]

[!] This program solution is not final and some details are potentially to be changed [!]

[!] More services support and functions will be added soon or later [!]

[!] Current version - 0.32b [!]

<img alt="GitHub (Pre-)Release Date" src="https://img.shields.io/github/release-date-pre/OSINT-TECHNOLOGIES/gaia?label=Last%20Release&labelColor=E98484&color=446C6C"> <img alt="GitHub" src="https://img.shields.io/github/license/OSINT-TECHNOLOGIES/gaia?label=Licensed%20with&labelColor=E98484&color=446C6C"> <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/OSINT-TECHNOLOGIES/gaia?label=Repo%20size&labelColor=E98484&color=446C6C">

<img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Python-yellow?logoColor=blue&labelColor=blue"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-Jupyter_Notebook-orange?logoColor=blue&labelColor=grey"> <img alt="Static Badge" src="https://img.shields.io/badge/Created_with-MLJAR%20Mercury-blue?logoColor=blue&labelColor=white">

<img alt="Static Badge" src="https://img.shields.io/badge/Google_EE-integrated-19830E?labelColor=0E4183&link=https%3A%2F%2Fearthengine.google.com%2F">

**If you want to contact the developer about GAIA - write here:** osint.technologies@gmail.com


## What is GAIA and how can I use it?

GAIA is a program created using Mercury Framework (runmercury.com) and Google Earth Engine (earthengine.google.com) special for those who works with geospatial images of Earth or interested in this subject. This program implements the idea of getting as much sources of sattelite and aerial images as it possible in one app. It allows you to get planetary images from different providers using APIs of various services and, what is important, without any coding knowledge and in a pleasant web interface

## GAIA demo screenshots

1) Fires map in certain time period, visualised using NASA FIRMS
<p align="left">
      <img src="https://i.ibb.co/0r7L70F/firms-example.png">
</p>

2) Landsat 9 SWIR image of Europe
<p align="left">
      <img src="https://i.ibb.co/K5mQ19m/landsat9swir-example.png">
</p>

3) All available datasets, dashboard demonstration
<p align="left">
      <img src="https://i.ibb.co/vVW6hYK/datasets-example.png">
</p>

## Supported imagery services

> **Google Earth Engine.** This service combines a multi-petabyte catalog of satellite imagery and geospatial datasets with planetary-scale analysis capabilities. Scientists, researchers, and developers use Earth Engine to detect changes, map trends, and quantify differences on the Earth's surface. Earth Engine is now available for commercial use, and remains free for academic and research use. Support has been added with 0.3b update.

## How to start researching with GAIA

**The very first step on your way to start researching using GAIA is integrated services connection. Instructions below will help you to properly configure and connect them to GAIA.**

### Connecting Google Earth Engine

To start researching using Google Earth Engine you need to:

1) Register on Google Earth Engine using your Google account (https://code.earthengine.google.com/register) OR start GAIA using start.bat and press EE registration button
2) Register a new project with unpaid usage, choose any type of project you want and name it however you want 
3) Confirm everything you've chosen
4) Go to https://console.cloud.google.com/iam-admin/serviceaccounts/ and create service account for your project. 
5) Once service account created, click the menu for that account, then Create key > JSON. Download the JSON key file and put it in GAIA directory
6) Open GAIA in web interface and if you don't see any errors and see the map - congratulations, you've just finished Google EE connection procedure. Now you can start using GAIA with Google EE

**After all needed services are connected, you can start your research. In order to do this you need to start GAIA web-interface using start.bat script which will open welcome window in your default browser.**

## System requirements 

**Software requirements:**

1) OS Windows 10/11 
2) Python 3.10 and above (lower versions won't guarantee correct and stable work)
3) PIP package installer

**Installed Python libraries (all of them can be installed using requirements_mng.bat script):**

1) mercury
2) ee
3) geemap
4) datetime
5) colorama
6) gcloud
7) earthengine-api
8) notebook

**Network:** High-Speed Broadband Internet connection for good experience with datasets downloading
