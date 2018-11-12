# osm2pgrouting4qgis

A front-end GUI for easy use of [osm2pgrouting](https://github.com/pgRouting/osm2pgrouting) from inside of
[QGIS](https://qgis.org/en/site/). All of the parameters to control its behaviour are available in a simple & intuitive
menu for when you don't feel like mucking about in the command line, as well as a few extra features for
streamlining the process of generating pgRouting-compatible networks directly from OSM with nothing more than a few
clicks.

## Features

#### Quick selection of study area

You can use a previously-downloaded `.osm` file, but if you don't have one handy, simply use the current QGIS canvas
extent, or the extent of another layer or dataset (coming soon).

#### Existing or new databases

The resulting routable network tables can be created in an existing database, but if a suitable one doesn't exist yet,
you can specify the credentials to automatically generate one. The database will be automatically set up with PostGIS
and pgRouting (provided you have the binaries installed), and a connection to it will be made in QGIS.

#### Alternate REST endpoints

The source `.osm` data, if selected to be downloaded, will be requested from the default
[OSM REST endpoint](https://wiki.openstreetmap.org/wiki/API). However, if you want to use a different one (maybe some
super-duper secret private endpoint), you can specify it in the plugin dialog.

#### Alternate osm2pgrouting executables

If you are developing for osm2pgrouting, you can explicitly specify executable to use, which could be useful for
quickly comparing differences in the outputs of a new branch.

#### All osm2pgrouting parameters

Every osm2pgrouting parameter is able to be changed, with immediate deactivation of parameters which become irrelevant
due to previous parameter settings.

## Installation

Once deemed finished, this plugin will be hosted on the official QGIS plugin repository, so that it can be installed
right from QGIS. For now, however, the contents of this repository must be placed at this location:

`QGIS/QGIS3/profiles/default/python/plugins/osm2pgrouting4qgis`

Where `QGIS` is the main QGIS installation directory, which is found at these locations, depending on operation system:

* `C:\Users\USER\AppData\Roaming\QGIS` (Windows)
* `/home/USER/.local/share/QGIS` (Linux)
* `Library/Application Support/QGIS/QGIS3` (Mac)

## Credits

* Main Author: Isaac Boates ([Github](https://github.com/iboates))
* pgRouting & osm2pgrouting developed by the [pgRouting Organisation](https://github.com/pgRouting)
* Plugin developed using the [Plugin Builder](https://github.com/g-sherman/Qgis-Plugin-Builder)
