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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEC5ERAG%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T075922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFmF9QRpTokZt5rBAIwiDsReyxyVx1heXZmpRKuGlGa5AiADcBrMB0WBTvwT64VnsMdW9JfZpXcCNq0Vi6I%2Fyrx7iSr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIML5wq1on9lU4CYaasKtwDkS%2F5gHHlV6CH%2BsEDg5F7ztqu5%2BkLvWQ0xf1vknMI9zQjNBszYe9VjQbCZkQwJwBLyKh4prORhKUQplmJRHW4QB%2FhOsDQPrKAkbdrRG9mrDxL0J%2FK5qC7gaCq6ndWZ%2FseTXKT9Qw7JoEGs%2FZsKW%2BAk95VBgqqsNqZ9ulBYZbrloV%2Bvsa251JKT6XM%2BMiZ18majGsix%2BGdpMfb%2BIbyrDAV2XFyZdjz3a0e1vc%2FWkGdfKOWOuYDfXaN3eAHIRo7DyKs38OOB9PJxWUFHMrBhZmSAwpTDZNy0HO5ifad1BJofsphBaQOs55hv%2Br5r9et1Go%2BPRoNaPlBb%2FLgIJPytysfP4T1ozfiWS0obIsETtVUFG5vTbxOaCNTOwvcedHh3PSEM%2FwVKBJl2oIwExTAlg%2BaY58nnMXIi%2BslzK0%2FMP%2FJ3MhHXcug0K4IHlkgQKfiMEAhUdZ5y2lluI%2Bz15q%2BrUUa%2BZQt6fot5mOHA7YB5QGpLA%2FqQjfxDLN9a8lWYd1AUHaNrhjs1qnOIQYJhmKt7AnO5MvZDSVernJeaGMP4uWnXP2prdI70N7LYby%2FBOh2RELTpAGoHyDrNSWDaKoflTIkEDYcAuj9fJX%2F9vhCisqBeH%2FIiv1Ei6LqzRCfMn0wkeCJ0QY6pgEn41kACxKQ9m0xAJeDakxFbmm1pO%2B2rE8j1pMh1ndn0Oek2iO1aCISmwOMc2QRDWrrL597LzuWllSlYPAb0PS3nhj8nH2cLx9hw%2B2ygvjdNLG5yszHQ4%2FfOU049KpJXKjCrfpqiNeOydRf0l2oe%2Bq6gibYpC22IWGlhZ7dOUPaV1%2F2w2btC4goj%2FuHa9%2BoIkJuwcXVegFJ8yPoX0kKF9in%2FYJuOOFJ&X-Amz-Signature=a07b16a0c9408075abfd3fcccfc30ff9640713a48c6e5d488c961852f8bd5a15&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
