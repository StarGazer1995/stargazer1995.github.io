---
created: 2024-07-04T01:57:00+00:00
categories:
  - Blog
tags:
  - Notion
  - Problems
updated: 2024-07-04T02:13:00+00:00
date: 2024-07-04T01:57:00+00:00
title: complicated geo coordinate systems
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQLXOO3A%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T012744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIEY1jPBp4uAe94eicQP0K9jMh7l6u8%2FQ%2F14P1oevYnBqAiEA3tbmGWRYu8500JrTUCt0bbG7gG9%2FollPKuJO9IxK7mIqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLJkNIGKrrXoUutKSircA3JiZeRNj5PLsZdCHfmQSLiTpE5CGz5gmF%2FRQv%2FW63saGB7FPgeA9NfE%2B2Y29l%2F7UtGjWxBIOsi3TvchBsGGcns2qj6aucM2XTYzFDeyeF%2BWJ4cLFgXo8%2F8sRI6EvmIv3PWBrU%2FhYtRRpDr7oR4zwUzeiJMp%2F%2F2b34Ocl%2FY0mYqQ1Ku75NnsDnBrUGL45RyGXJYADyJY6xAE6PO7G2ToinbS6D1hq6%2BYpWPXQKqMr1PvGz7Q%2F0QY4w1l7m3HAnVQuZaS%2FrCNU5vvPABLhCe5tSf5%2BciEliPBwaAHP%2B2fVr9eBqfpY6gQZzPA7Jb8J%2FHWUk7rif5jNhNpYgvlNj8Pq70hcHsUMkbvgVO%2Fos%2BDUfeyMhLw8rrRVh8BI7baswNZkkXTdvXRmmyF0nLe367vlOVXV3T16pZhiR8tR%2FTCD0OImQBIMGd%2Bcnzk03%2F1I0R%2FQIdxVUP2H131rb8LB5dpFCFMPASHJKVv8DuW455IhsdN33Wd5fng%2FwMLyvpSq45DIkO4qhI4cV%2F95HlGcwAsa3LABErwRApCUX%2B%2Fd1UV9FY01cUjNl9SVxrfgSpExwfzgLhrA8kUVwVv5eAujY4HyFHlCoqnuAjMVyKfvSNfl%2FCkW0mxKybO2%2BK8Tw6LMNXQudMGOqUB4%2Bjc4P%2BlaDTVg3AZwHesiF3h9A0pnxlDH9uSxTgDa99cZA6pf9%2BROPTSztYlINrZDv36GLO0qk6U2j3mcVln6sSmmELJo9HravycYZf0V1X9YbdczViqJsGLU1SYpNaspzW%2FKNsGk%2BMy2BbxlprvEZjA8c9ZgXiNYAvVIo%2FoeWn0a4Z1wi3UywjHsbZFbuBNgiZzCEiYd%2FJxqjbHTn%2BHH1X3JU9F&X-Amz-Signature=764a7759d0c1523692c1c9eaa67511ba91539aeb81597e1c875a7ddbbd4ef6ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
id: c94cada3-a872-46ee-959a-b073902ff265
---

Transforming through coordination systems can be confused for some developers like me. But we have to know those commonly used systems and know the bridge between these words.

As an autonomous system developer, the commonly used coordination systems are: WGS84, local Cartesian, and ego. Although it is not that important to know the projection theory behind these coordinates, it is good to know how to transform between the coordinations.

## Conversion from WGS84 to Cartesian

1. We first need to choose a reference point in WGS84 as the cartesian’s origin.
2. Convert the WGS84 coordinates of the reference point to Earth-Centered, Earth-Fixed (ECEF) Cartesian coordinates.
3. Convert the WGS84 coordinates of the point you want to transform to ECEF Cartesian coordinates.
4. Translate and rotate the ECEF coordinates of the target point to the local ENU coordinate system centered at the reference point.

```python
import math
import numpy as np

# WGS84 ellipsoid constants
a = 6378137.0  # Semi-major axis in meters
f = 1 / 298.257223563  # Flattening
e2 = 2 * f - f * f  # First eccentricity squared

def wgs84_to_ecef(lat, lon, alt):
    lat_rad = math.radians(lat)
    lon_rad = math.radians(lon)

    N = a / math.sqrt(1 - e2 * math.sin(lat_rad) ** 2)

    X = (N + alt) * math.cos(lat_rad) * math.cos(lon_rad)
    Y = (N + alt) * math.cos(lat_rad) * math.sin(lon_rad)
    Z = (N * (1 - e2) + alt) * math.sin(lat_rad)

    return X, Y, Z

def ecef_to_enu(x, y, z, lat0, lon0, h0):
    lat0_rad = math.radians(lat0)
    lon0_rad = math.radians(lon0)

    X0, Y0, Z0 = wgs84_to_ecef(lat0, lon0, h0)

    dx = x - X0
    dy = y - Y0
    dz = z - Z0

    sin_lat0 = math.sin(lat0_rad)
    cos_lat0 = math.cos(lat0_rad)
    sin_lon0 = math.sin(lon0_rad)
    cos_lon0 = math.cos(lon0_rad)

    t = np.array([
        [-sin_lon0, cos_lon0, 0],
        [-sin_lat0 * cos_lon0, -sin_lat0 * sin_lon0, cos_lat0],
        [cos_lat0 * cos_lon0, cos_lat0 * sin_lon0, sin_lat0]
    ])

    enu = np.dot(t, np.array([dx, dy, dz]))

    return enu[0], enu[1], enu[2]

# Reference point (example: latitude, longitude, altitude)
ref_lat = 41.8902
ref_lon = 12.4924
ref_alt = 0

# Target point to be transformed (example: another point near the reference)
target_lat = 41.8912
target_lon = 12.4934
target_alt = 0

# Convert target point to ECEF
target_x, target_y, target_z = wgs84_to_ecef(target_lat, target_lon, target_alt)

# Convert to ENU coordinates relative to the reference point
enu_x, enu_y, enu_z = ecef_to_enu(target_x, target_y, target_z, ref_lat, ref_lon, ref_alt)

print(f"ENU coordinates: E={enu_x}, N={enu_y}, U={enu_z}")

```

## Convert local cartesian to ego position

In our system, the difference between the local cartesian to the ego coordinate system is only the rotation.

```python
import numpy as np

def local_to_ego(local_x, local_y, ego_yaw):
    # Translate coordinates to the ego vehicle's position
    translated_x = local_x
    translated_y = local_y

    # Create the rotation matrix based on the ego vehicle's yaw angle
    cos_yaw = np.cos(ego_yaw)
    sin_yaw = np.sin(ego_yaw)

    rotation_matrix = np.array([
        [cos_yaw, sin_yaw],
        [-sin_yaw, cos_yaw]
    ])

    # Rotate the translated coordinates to align with the vehicle's orientation
    local_coords = np.array([translated_x, translated_y])
    ego_coords = np.dot(rotation_matrix, local_coords)

    return ego_coords

```
