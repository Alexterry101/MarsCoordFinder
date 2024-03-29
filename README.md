# Mars Coordinate Finder
## Contents
1. Description
2. Installation
3. Usage
4. Generating a JSON file that bounds a required location

## Description
- This package allows the user to generate equidistant latitude and longitude coordinates within a region
defined by the user.
- As most of the work done within Mars is not concerned with locations within the ocean, this package limits
the coordinates to those that are on land and ensures the equidistant locations are only over land mass.
- There are two methods within this package: 
    - The first can find equidistant coordinates within a region bounded by North, South, East and West coordinates. 
    - The second can take a JSON file that defines the boundary coordinates of given region and creates equidistant
    points within this region
    
- The result of either of these methods can be stored as a JSON for use using the createJSON method

## Installation
Use the package manager pip to install coordinate_finder
```python
pip install coordinate-finder
```
## Usage
To use this package you can reference the following commands as an example:

```python
from coordinate_finder import Marscoordfinder
coords = Marscoordfinder()

# Code to generate equidistant points within a boxed region
# land_points are points within the region on land
# equidistant_points are the number of coordinates (in this case 40) equidistant across the land in this region
# n & s are the North and South Latitudes you wish to use as the boundaries
# e & w are the East and West longitudes you wish to use as Boundaries
# fidelity is the granularity of the defined grid, a smaller fidelity will give a finer granularity
land_points, equidistant_points = coords.getNPointsInRegion(40, n=30, s=26, e=86.9, w=83.3, fidelity = 0.08)

# Code to generate equidistant points within a custom defined boundary
land_points, equidistant_points = coords.pointsInRegion(40,'BRA_Shape_Points.json')

# Code to write the calculated coordinates to a JSON file
coords.createJson(equidistant_points, 'C:/Users/smithjoh/Documents/output_coords.json')

```
## Generating a JSON file that bounds a required location
- Go to https://gadm.org/download_country_v3.html and search for the country you want a region within
- Download the shapefile for this country
- Go to https://mapshaper.org/ and upload all the files at the _0 level (this will give the country outline)
- Export the GeoJSON files which will give a JSON file of all the cooridnates of the country outlines
- This can now be used with the package