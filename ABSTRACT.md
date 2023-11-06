The authors established a **PV** (PhotoVoltaic) dataset using satellite and aerial images with spatial resolutions of 0.8, 0.3, and 0.1 m, which focus on concentrated PVs, distributed ground PVs, and fine-grained rooftop PVs, respectively. The dataset contains 3716 samples of PVs installed on shrubland, grassland, cropland, saline–alkali land, and water surfaces, as well as flat concrete, steel tile, and brick roofs. The dataset is used to examine the model performance of different deep networks on PV segmentation.

![Fig](https://i.ibb.co/BVG6HQn/242.png)

<span style="font-size: smaller; font-style: italic;">Map of the study area and data sources. (a) The location of Jiangsu Province; (b) spatial distribution of all sampling areas; (c) Gaofen-2 satellite image with a spatial resolution of 0.8 m; (d) image from aerial photography with a spatial resolution of 0.3 m; and (e) image from unmanned aerial vehicle with a spatial resolution of 0.1 m. The yellow boxes in panels (c–e) represent the same rooftop PVs.</span>

All PV samples are collected in Jiangsu Province, China, covering a total area of 107 200 km² (Fig. above <i>a</i>). Located in the lower reaches of the Yangtze River and Huaihe River, the province is very flat, averaging only 12.3 m above sea level. The land terrain is mostly made up of lowlands and flat plains, with hills and mountains in the southwest and north (Fig. above <i>b</i>). 

Due to the shortage of land resources, most of the installed PVs in Jiangsu Province are distributed in areas where land competition is not fierce (e.g., sparse shrubs, low-density grasslands, reservoirs, ponds, saline–alkali lands, and rooftops), which makes it convenient to collect various PVs with different backgrounds.

The sizes of distributed PVs typically vary from a few panels to several hectares depending on the area of available background land. It is difficult to identify all these PVs from a single data source; hence, the authors used satellite and aerial images with different spatial resolutions to collect PV samples at various scales. Gaofen-2 and Beijing-2 satellite images are used to prepare samples of large-scale PVs. Gaofen-2 is part of the CHEOS (China High-Resolution Earth Observation System) family and is capable of acquiring images with a ground sampling distance (GSD) of 0.81 m in panchromatic and 3.24 m in multispectral bands. The Beijing-2 satellite constellation consists of three satellites and can provide images with a GSD of 0.80 m in the panchromatic band and 3.2 m in the blue, green, red, and near-infrared bands. Aerial imagery with a GSD of 0.3 m is used to collect samples of distributed ground PVs. The aerial photography was conducted by the Provincial Geomatics Center of Jiangsu in 2018, covering the whole of Jiangsu Province. UAV images are used to collect rooftop PV samples. The UAV flight was carried out in Hai’an County (yellow box in Fig. above <i>b</i>), where the development of rooftop PVs is relatively advanced. Ground control point (GCP) data obtained by continuous operating reference stations were used for georeferencing. The final orthophotos have a GSD of 0.1 m and a location accuracy of approximately 0.02 m. Figure above <i>(c,d)</i> illustrates the appearance of two rooftop PVs in different images. In the Gaofen-2 image, the PVs take up only a dozen pixels that are mixed with surrounding rooftops (Fig. above <i>c</i>). It is difficult to distinguish the PVs from the background, let alone get their exact position and size. In contrast, PV detection becomes slightly easier in the aerial photograph, but obtaining accurate PV boundaries is still difficult. In the UAV image, authors can clearly recognize the PVs, obtain their boundaries, and even count how many panels each PV is composed of.

| Dataset | Category                  | Spatial resolution | Code | Size        | No. |
|---------|---------------------------|--------------------|------|-------------|-----|
| PV08    | PV08_Rooftop              | ∼ 0.8 m            | 11   | 1024 × 1024 | 90  |
|         | PV08_Ground               | ∼ 0.8 m            | 12   | 1024 × 1024 | 673 |
| PV03    | PV03_Rooftop              | ∼ 0.3 m            | 111  | 1024 × 1024 | 236 |
|         | PV03_Ground_Shrubwood     | ∼ 0.3 m            | 121  | 1024 × 1024 | 119 |
|         | PV03_Ground_Grassland     | ∼ 0.3 m            | 122  | 1024 × 1024 | 117 |
|         | PV03_Ground_Cropland      | ∼ 0.3 m            | 123  | 1024 × 1024 | 859 |
|         | PV03_Ground_SalineAlkali  | ∼ 0.3 m            | 124  | 1024 × 1024 | 352 |
|         | PV03_Ground_WaterSurface  | ∼ 0.3 m            | 125  | 1024 × 1024 | 625 |
| PV01    | PV01_Rooftop_FlatConcrete | ∼ 0.1 m            | 211  | 256 × 256   | 413 |
|         | PV01_Rooftop_SteelTile    | ∼ 0.1 m            | 212  | 256 × 256   | 94  |
|         | PV01_Rooftop_Brick        | ∼ 0.1 m            | 213  | 256 × 256   | 138 |

<span style="font-size: smaller; font-style: italic;">Organizational structure of the PV dataset.</span>

The PV dataset includes three groups of PV samples collected at different spatial resolutions, namely <i>PV08</i> from Gaofen-2 and Beijing-2 imagery, <i>PV03</i> from aerial photography, and <i>PV01</i> from UAV orthophotos. <i>PV08</i> contains rooftop and ground PV samples. Ground samples in <i>PV03</i> are divided into five categories according to their background land use type: shrubland, grassland, cropland, saline–alkali land, and water surface. Rooftop samples in <i>PV01</i> are divided into three categories according to their background roof type: flat concrete, steel tile, and brick.
