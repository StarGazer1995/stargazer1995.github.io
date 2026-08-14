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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPNCQBXS%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T184555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCISVcbhb8fXGq2JgRhD5cHrhjBE6KoCAFlJyyaOF6Q%2FgIgJ%2FXsR3EQ8t%2FbGjEcdo9eVxcH5gtvfMAbwUIryrHYqS8q%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDBa%2FqgDP1JPCN61cKircA%2B2BmqqEfElm46D4W4qE2bBKVv8KypvV%2Bbings0F%2FSxxOPDie9KZAokYtSgpHPQn7eDBv5ZzD%2BbeNZpIhc7AN5%2BNqJS0S6vPknTb08Pd4PnEVjUAI5qJcN2tShoVtnmN8Pky9eA4HyhG1gPyXp93bXXFtrRzXBUn9dNDR7JAlL%2BgJ1qyDma8jqJbfpT0%2BFsgQlFEHPV8hZeyFjCsZyyXDmEQYs5GglSZ3lBxnbKxL5HYmtj9Afbp3YPFTBvck0VVuu2TG4v%2FIunT4w8Uc%2FEpiyzQmQr7ziC51Yrsa%2Bmv%2BGs5ZlyW4I4EdPCJGwz4s7W8Hmo8vDw3SK1FEAsYbFDYCngs2u4q3kSmdMsECVI0fxi29yQM7%2B3s529eEoWc8vuvx0HgZY%2FznEGZ6FMWOC7lr36KPMLaGhGmNaWf%2B%2BnXJ3sXUcsKax3sabEzJN2g%2F8WqMYmK7K1IcPNEJcOUdvEiLKwWgv2kkVCLl4JyQQPd6jLDDBifmi1LVQ5t92%2FINs5YmYO6BrcYPxG909QTshL1rdL86Pg31MeTbaqJ28C5a5%2FwRAABkZNA0SPJ1pueoq6vNKITFPYxiOXZ59gQfrIegUlycsZR7YqPFo9z52kSP7agRAssk2KuJvujLn5RMI62%2FdMGOqUBG33oRiSBgzwRCMXWzie09nRPagl2oLo1TmyS5khF77lKs%2FOsdyiJqsxs0CkxALL7HqITKlqlyP6wzsbJHva58B2lmMCxuuv8PK9aVmeM5KolMd8TFq231GzYK0PoT7GsRZupAzD54NVPE3Ms7lFClJ63Zsl0PXfHynmiXpxLPhlfFhGwy2bYB%2FVSgZA3QSa3Zliec3RFnfIn8l%2FlSWUy96kSaj2y&X-Amz-Signature=e2db3a82cf800993d2d3e2ef1c526a6f79e389c4a5f7ab03f9840241b04af2c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
