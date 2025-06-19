# Publishing a Project/Theme to a WebGIS (GeoGirafe)

## Relevant Navigation Menu Entries
The relevant Navigation Menu entries can be found in Django Admin at the bottom:

<img src="../assets/gg_nav.png" alt="webgis navigation" style="max-width: 400px; display: block; margin: auto;">

## Webgis Workflow

```mermaid
graph TB;
  importQGIS["Import QGIS Project (if not already done)"] -. "." .-> prepareTheme
  prepareTheme["Select a Project/Theme to publish"] -. "." .-> groups
  
  groups["Organize the Groups/Layertree"] -.".".-> manageLayers
  manageLayers["manage layers"] -.".".-> wmsLayers
  manageLayers -.".".-> wmtsLayers
  wmsLayers --> webGis
  wmtsLayers --> webGis
  webGis["WebGis (GeoGirafe)"]
```


## Data integration -> Project
If you not already have imported a QGIS Project, now is the time to do so. Go to `Data integration -> Project` and press
the button `Qgis Projects`

<img src="../assets/gg_1.png" alt="select project" style="max-width: 400px; display: block; margin: auto;">

Choose which project you want to integrate and press the button `integrate` beside the project.

<img src="../assets/gg_1_1.png" alt="integrate project" style="max-width: 400px; display: block; margin: auto;">

Now you are ready to move to the next step.

## Themes
Press the button `Publish from Project`

<img src="../assets/gg_2.png" alt="theme select" style="max-width: 400px; display: block; margin: auto;">

Now  you can select a QGIS Project

<img src="../assets/gg_4.png" alt="theme publish" style="max-width: 400px; display: block; margin: auto;">

The OGC Server of the project is automatically added.

<img src="../assets/gg_5.png" alt="ogc server" style="max-width: 400px; display: block; margin: auto;">

## Groups (Layertree)
Here you can reorder the groups/layertree for publishing the `themes.json`

<img src="../assets/gg_6.png" alt="manage layertree" style="max-width: 400px; display: block; margin: auto;">

## OGC Servers
The OGC Server of the project is automatically added.

<img src="../assets/gg_5.png" alt="ogc server" style="max-width: 400px; display: block; margin: auto;">

## WMS Layers
!!! info
    Currently all layers have to be to set to public to be visible in the WebGIS

<img src="../assets/gg_7.png" alt="manage wms layers" style="max-width: 400px; display: block; margin: auto;">

Here you can manage the single wms layers.


## WMTS Layers
!!! info
    Currently all layers have to be to set to public to be visible in the WebGIS

Here you can manage the single wmts layers.

## GeoGirafe
<img src="../assets/gg_9.png" alt="manage wms layers" style="max-width: 400px; display: block; margin: auto;">

Now you can navigate to your GeoGirafe instance to view your theme, which is in dev mode found under [http://localhost:9309](http://localhost:9309)