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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665LVEPP4X%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T143151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDLxuiQrZ3SzRmix0M8Exxt2gN1l2h4rvLDMXyB2VhDUwIgGMhGg%2BW8LtIFXEcwp3AclORf9udBjZ%2B0XicFQmUBQ9YqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMoZdu6VyFhregu8jCrcAxc3OHZVeJ2NUjl1dNpqhUVX681UBSUXMfPv58yxrvyHSorBxes4rn01sFfKUmJDaofRYd4z9LcxkwvoqgOlai5JGoBZy%2FUwm%2FqMyMbUOGGaeztIC4fj6WMtw6LpxEcE%2FGHOQq6RLIIgU6r2FbU4k8zQoD0HFubFPdnlOJAajgQOkn5g%2BZIakUqZS60n1pKjQ%2BVlRdy7Kp3rINtvi7EoLl13NaCH0Wh46B%2B8EdHrsP0pyx%2FRdGyEKERBP%2BwsINsgiWqTG31sWfK2TpWAFUMN1E5pYXajk9gnEvqc48LcgE9u3jPEyr7HOktV9L6tTLEqGyYVEKBCBKqvmaJBoUzC8fTBOMJjFPFdOY8t1tOBwJZsVgBbd9Ps7H3ixMEB7b7vvhVXhXzGXdPc%2BQC1lEDDCA6KWs09mD3rgkE2cuyOkOfV9sC1E98Jwq4O1LW66z5ObRtp2chnE25rdtaGhEcmQFsIeirUKILDSjh9B7jK%2F8Fz%2BsVHxw68ACV631jXWE1jZEkbGofQBcGAe2vsb8rpDATeXdSHh5staXjDLzPCKjo7uxYITkpR80ToofCJQMESZOQBsGj8%2BUHtJZWwa05OqcxXT212cEwbGFL3jjB8yx%2Fma5mlZzGhksRDnioXMIftwtYGOqUB7qfibXrYiClJGWKF9NoNqqhtN1sBHl9Fje9A%2BEZhA5gh7hnxDvwFTGN39tbHE5QiTrSXfu6Q9fRcp4PSv%2FS9fkEvDt%2BTB5vV4SBdb3rrMJolweyKbwB8oc0B9lWukeREztHVjEfeqG3Hpz9WKhwi0t3FbE3OdFNjj0X2YrmnMxN0ssFstBVL%2Bs%2B8aOv0Lcyknuree0fONnPhfSDCbzGfHENOgRMo&X-Amz-Signature=63c08d9102fc54b12e9bfab2dde78d813a5a64db85df35cd111ca88a0b0eb077&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
