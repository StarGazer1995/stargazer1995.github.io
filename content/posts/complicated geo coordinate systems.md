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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZML365VT%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T221245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDV3D5edGd46yrxedTW8EAZlpZUC1G9XZx%2FcFTpZLh71AIhANmx1dU8UuK4SU6oW18guEpUGEZk54OIuzQwdpxnIOelKv8DCE4QABoMNjM3NDIzMTgzODA1IgymBQ3jJcMqnYwYTwoq3APB%2BgNp1q8HlUlEmBA0GVplL1%2FgW2%2BTXgEDglyv2UM%2F9qfKr0QrAPqKK1ZVi1AzUktF%2F9DR%2B6PC2cAovnjLyNxzmdzV4ZTCAihuCLMlyV%2BB2WY4BaP%2FSFA%2FQLRE%2Bf9KGnRZ06%2Ba8gQC9v65S2OkXyzuiVhi6imNyBiP2wvkm1pQhxTZ4OQ1kam2LU1ZzFLrj7Mf0wf3S%2B%2BOuLiTwm4I8bs1FV1em7k%2FLuihcq6xePYut%2F%2BFGBXHdrYG7rOsY2A4KY6ZJzrG%2B%2FJMhapuVKiGipsO0pW2EMrFbR6H1sNoOfxeKHSzJ7C%2FPjgA6RJhHzemMiAn%2FjE114viM3aLBBTVk8YE%2B7XB%2BSjA8e92mUaN7u9LObR2E0pl109A2gGuoHMSH3CAxxVJha2AEgvx6qYk198REWSmNjyvxYHEohpIt6kdynYH3tXjGG%2BXeH%2B17fbBQkIwOKU28WsPDZWQfcVUBks2amuqCam%2FGptqXMX6rs2G1pLXuueJC%2FUZuanYzHV9HoFFeGY0JJVs4mpkAT1oOOBA9yGomDgCpf8NJBjNhqekx%2BVQm7R0VsGawS%2B69ONhd2LnmNzRYI7dlWy9U%2F0sjzWeN0u1RmSaMiEEiMx5m976mQxKtyF%2BxE%2FSSIF2ETC9643UBjqkAa%2B31%2FgT117%2Bdb%2BhIt9WKnfE3AWtMj1f9aENUd3Pwh7drSy1MhEs7prGx9AUfYvcGvRJlD2DMfy8cKkSJQtAsnIol%2FySz%2F%2BodEansRAuLAG8e3sHZ3zkfQxIPT8W2unJ0mSDsV0MlT48cZgSUAMvb5HxbnmX7ainc%2B4E1y%2FCuRxZUenIeiHJFtl1rtydhdAv3bFEUdFkyBVTiNsJ1E7kG9ZZ1vYh&X-Amz-Signature=e4042ddcda6caec52dc9777c2d4c442348491edb5d533abe5c70f68aadd03e7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
