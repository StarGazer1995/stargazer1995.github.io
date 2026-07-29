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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FN5A67I%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T170300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFK2bro8uv8s1MChSm132LgiOXjIH%2BWHwPMznkbceJiFAiBT76yrbAhZ3Hhohj6rvAb9D8gpLvW7cmz6WQsZahkc4SqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtNZWC%2BxGcncXnRR%2BKtwDsO4qyCBWe3%2BvCooZc%2FUVDcvUONSrlQJDIxkcgZ0YSek5MlwXlAbLMfu%2BriQVQQLcyZS2uw5gnyda6Ud73pDXtXfZjx4Ay5aSP0RqqPkbAHMPMN%2FMCEApmluh%2BzEP7tjCLCRBrsF7BvUH3BHY%2Bm7A%2B5vLGZIYsARrmcw%2BTujaXIf6poVtTpkUAoG2BBnW0%2FVJqTPuPZsAnJ1UNeUZ13iiHjy5ukVuTWxlgXbfhtStFOQGnvIFsa2h1nsZuywQ4rJrV7OoOX2e2EqhqcylLHm96Br5%2BB01MKZ0hEr0AEOUTTHwL5Qcpcd9AG7x%2BUL7ZlBCh1R9cRHXJlp4%2BLxQnnN8zmTxbiD2pjH4yvqKdrpNSlh8yA3nD9mqwpHdfsMThlD2wsC%2FrnO%2BaXBl%2B63vB4%2Fj1qcjt7BzKTvQxy9XTSG0AgKkQYIwJljK6CZlxEwE%2Bzp8oA5%2F6GjeTAJQLhXAmRHaKuITmDtwInbu9wR9WYL9gHBFpbmoNTehEC%2BXF3xD4HeD5%2FHN3irFf1Tl11n3cfw248885vRIAad2y4DQdceID06tJvTGUq3gMlbqXT9GCp0p%2BKr7vbFl1nTrW9XI71ynWhcPeZoMBBXHrp1TF8tYXTEXm1MdnCyOGgco4VAw9sGo0wY6pgG9IzvviVlz1RLpy22F4VPVXlzXTLaju7PwEExRX5JfLTFpmqBBIzoc7bzSz8Wxf7ypbI55phtfThx%2FQ3m71ZgyispvTfvS3ySVKNJEKKH0TV4i8ZTUtaSS5ta3LYIcSATCPeI27lSIv%2FeSvz62bO9FDlQKj4JcYChN5WH2It3eW3U9G%2Fdagk78vF9bqEEqZMJ%2BMxYV5hLxIWVOYgyuB4IG%2FmIgyzHa&X-Amz-Signature=2e72cd72700bfe7eee6d6a741abf621a14a4c4e915f722ea933555bfa8c2d10c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
