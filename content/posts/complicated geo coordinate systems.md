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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUWPDSV2%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T204412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwAXjt7JA3W1JXh%2FfnSsm1ASE9TAXDda6W6W5%2B17I%2FPgIhAJBIDDFewboooU4ixOHUsVsV%2BZKU48Y2g77D3vxz3xqyKv8DCE0QABoMNjM3NDIzMTgzODA1IgyVZFcfw0Ka6b%2FNgRcq3AO7%2Fdtx2xg%2BW31rck%2FXg76Agiqx%2BA%2By0gXdQ3jGzWJQX8ozcioynC60VrDE3ebmIbhnMkAIWHirkjIzT3TozbTTxffINZ9375Wgis3ZYIdAvUfrni8BBAoO67bIpMddkKNXAmAzSdoNAK4GdWhNEam%2FyCL%2BczJHCYeZ6P%2FMBmupFHcjMQ05DfOfL%2FYHN%2BfKX7YXBC6Vsft67bNt0ls6VwFd8DuS9CZxOmct2fa9fX5Dy5KbwQ5WwKoecReHRPWjXxn%2Fi39TDZKJRPfy2TvZE0bIYLvPD6SAX4bH5BxW%2BDe%2BkQApycTC6otILZyvculPUsFfEh3H9ft%2BC19%2B0o8WrdLsqAe%2BAfUAMwLsoID8%2BjktaUKuBdq6hJVdb2uvjrin2izTypoFoQIEuOolszvH%2FFRR5A7ZQ4f3hNLCCCTph2M3xiLOyafSxdfzWNoskhAfkwMTrHvTSr6eSHHCJiuv%2Fn2ILMNhs%2BKmxyOHteMRf082KUxd%2B9MEu2GdFWafQ0M3%2FQsdR9lXdC%2FWO3Yi46Qwoutl3sVYXqvYiZpO1KGQw66fRhtazlwgtPj145yCB7ZAKss1XIDVJF4F1HsQJb2QHhXuOhssTQz5Jg5NrqBM4byPqNiOhaxLBUBswqPw%2BjCg4uTSBjqkAUvf50RB3eMqVnbGmQ0iwz5SBAsFQ7TMzTWxK9t5apCqpuL1Iz%2FDO6O1jzmSDJwxcg7Ttqity51jWGw2HXJ98FHP4yZNQDINkCe97%2BW%2BXR0iHKGVsECbjK6DFf2hFh0D26Nlss3B1BU509RCBlIjANw7dNGU8u2oA3yCu91aOqjf4TRzbJUBr2syj%2F0XZJCNTB9C%2BEWBxkAhOUj4Cbr3drHcX7c8&X-Amz-Signature=52812a56a396a2316cf4c0f80777d4d667c4c30ef2f07d51ab6db0dbf5fded38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
