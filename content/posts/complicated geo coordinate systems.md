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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQMGBJB5%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T124559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID7vAWbj3OU6%2Fxz7RMiR21X2hZNPnzG1v%2B7IiBH2pP8fAiEAyD8yQwCm7RFc8cslt0CdkpQ4dOdTynAkM8hpXAmO8o4qiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG5%2FVSjJNmTUkbV11SrcAxoeOClrla%2BmahCU6qZCwwFmFEEdqr7SmTztdrtdRP1Sj9Kb0kMckqSI4R7Y3aioOjP%2BSigZf3aaxmqlP5fuzT0r2qTdLo%2Fh8ntUatQEWdTS7iYiYCUcN7AHcfFmEJ0%2Bj%2FNolxFakowjBLCvYfJjcWTXk5E7wgKG9bokO%2BBVAE6oMbC%2Bfz2kBLIDF8l2bxUPZR2j%2BwoHaXrVMJgrqsgGliCO%2Fxs41jhvI%2BhzrHTvox7zOdiZ9lQa0N3DA32cFiIMDja5tA6F5JU2NLJQ5KYOY4dQQW4S9pR0T2nVtANI7HUpjUmbdVYd1Xchq%2FSEpDP8QZUsQYrGrAQSRwJWXf%2FdixofVkGEmScvaWnV5gZB%2BthHA3qVWHOOIDrrOXaj1%2BgtRX1mgeKvQxWDFnv74f1%2Fp6QTxWNRpb8pfD4JQ7oLbTU%2B52m5vGfq4tTK6%2F3%2FKaWMvqUIKpPlfp6D9Z7cZjISwdhGwhCLJCZTEV%2FK828xoNA0uE%2BKvB45%2BjrNMVZHuZJSR9RVaNLMF51TKAFV4yr4aynT6uLyxOcz7fzgVUNEsj9q6VwJlZHsn4Y3AD2x4cT6oHWDw1FdrgfdDNmEmNJVYEAP%2B8d6R7sa3jd9FJrSA88FWHHFWNDwHHS69wEUMJPDz9EGOqUBZklcpjEXR52ulYvJZ8CX52t3DMo645KB1bfivowZ8V1AusJBKZbc77tm2cPKf78za9KFsDccVUZndAlXUVMhvyFbByTTic9q8metI1aLV7oEg3ZUODLfnKFsl5sEu8lzU40DDr%2BT8zlWP%2BvxbEfX1yBjRHDLhHDjuBZsTMmwvuTCDUIJ%2BISbnidPDQsD4UwyQY4yTQxduh48aoyEY0s36FXu6WH4&X-Amz-Signature=fb0b5abc114306facf3c9e1424a16bfd78fcf2b1c2261998593118caf4049432&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
