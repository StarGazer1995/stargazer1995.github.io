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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIXH4TGK%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T204250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICILaSOizk2vjmZv5mGHLkTfCJiaUwTULALPS9H%2BAx1%2BAiAo3jEkLolXC4UM0XbWQo%2BkfpF2v4%2BxBDWoXSd2cwtqaCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMA7lVxTsUDhm2%2B1yOKtwDnq59qAlzuS7FbFZxE3TdUpxXfcHlgsK1T7AgNZB9o15b2730W8RQs%2BBs9zc%2BKJkiyivEMYt9QlfGcWiBQEEYlKNrmoBi2BxuNk3lzr0eCJ1%2BoxLJ1cvATka2%2FxwXhjfxYBZo%2BP6pjRiXFH0vI0vFqd2HeWga67xXIwVDJypyuKiq3yvYYv5k7xt6qje4RMscGyggWbgT6HPTJFN5JjrDwP7dFdSysEyp0cXWVhzXgKBR8ZAriQVy4O%2FaRg%2BlZAW7afTlUBahtw8WQD2fbqsJxurUNskY4fT4p2%2B%2FSrdIM9o5Qkugj5Ej5EnPIXvEvp%2Bzl6%2BjHDjBH0WEGoTq5WJoocrpTe6irIQh9IwHyAFmgzyTweRtJaTxdliC8NFDsadmQ4K5I6oto10l1uG503uuAdSkmC77dco1UymsYvf9Ks5vV%2FiTeLlCJOHOxk%2BCvjMY1g8cmPOf%2BmC4R6hs6f%2FmMa0qr8GureFLDaIGcSfH3%2Bm2a%2B2I7kA%2BgmolRRiW3A3Z3WgB5Am4uZbl9DCBldzJ6b8Hp4Ai4VKDkbmSNxLCs8AWq5yYFDf8C%2Fm11Qwjsuys56xY9wdngdhoJTBSd4T7NIw2LL2Cb%2F%2FZpCNkPaJJ088otSUOe7A1xkxX41swwrnN0AY6pgF8OrsrL9bDOEEsNGfQ9v9qnBz6XJoJPuk9AsGnBqFDkCs8NsnSjNXdOO6vtAqxPgT4c2hdDhOIlfTwJoNEZkPhsQUEI4mo5lQdclkrD5K%2B9ROoU%2B4v5pW5D4%2FMhOPysb1tSJe8nTdG5yKTvs4eE6eaCqKcYGgr%2Faa6pHxUUyJv%2FTYrixgheueYb64wagodtDLqkHlrC8RlIZMwMtlvXgB1RhdOdud0&X-Amz-Signature=53fc572b7ae6b5eec1428734319db1b594e277be580774246b3b881ae66ca8df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
