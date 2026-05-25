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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZT7G5DT%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T020704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCdC11won4dPbPTfxHPmwImDlLjoZk6E6UtB52CYa%2Fu5wIgQA14gdJ2Aig4AGE7zc4yK4%2FP%2FKjSlS%2Fp7FZPK7UtQ0Eq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDMUU7eFboUeOs%2FLFTCrcA%2FJd0q2qzLp58PYQnuCZBfJ4iRInatgZZ%2BOHJbVTYag5E5myzlC3nc8iHIfNOUtLXmjhLKQaKHX1tBaz9HN1wNVbc3FiG9rPpU4VgiBz3T42fr%2FsZV%2FuzSsKNMQFAuAMEJ3Gq9NPbnVoOn73Q8CK4ltYzFQ8crCrbv1wnxGtfdLqD9JRrHFicjwTjBjLWxB0UwDpU5M%2BZlah4Tbi5gj4lUWvTmf8RH0Yp0c8LuaKeGxX7qPp2NAIMpbk5Dn62M%2F%2BUubT62SWYH8DTNBahElK3Md4gTa4jmDXIbvo30KFf%2FAYmnp8nPrmVAhuAm%2B4pjBkgPpx7fPVv3KQF%2BC%2BvNkEBoVgtk1WPgjqm2AQwTuspg%2FeaPkSSFl%2FxPrK%2FoNBho7FTs28isl2OuDKwWkV7LImx%2FsnFiGsZKRO0%2FU5GPI%2BdXgxAOA6Pe0NM9DH8xMfds8w%2FkOMj7Sw8Wo%2BucdaAY%2FR2g48JbgMwSgbuZa%2B2g7rnAzH5E9gP5yjrEUezuxHiPyW6C%2BPDtjT2h%2FdcIn5ArtSxXUo2545sHqMtmrzM9fUPj37rIwtzTrGlmw4Y93f1HXsweelIjcbHD3pQd7kncZGpA7E7qHLtLrpGRR3h23LcwQBNjvM9oMYyFVbDzyoMImzztAGOqUBBmBolfEeKmu9SvsoAe4r3STfQ5ALV%2BYA7wQ65E7ldXktbltPRi8%2ByLM%2FvsKero9ZaG5yBCdfA6g%2B%2BkBFJISyQTRi6JSV2xaW8NSfytb%2BIdJqnW5YrGvnM1fXompKl7eg8HBGUeFuS9yWHiALcUyEHcL32djDdTEJqfkRgSp4%2BTaAEM%2B7%2BP8Cv%2F4ArlyS53UCMCFe8r%2BiIRO5VBa659aklngdYQHl&X-Amz-Signature=063447e0d7c2766bbffba1b723f00f529964e6940a46a952d724083f11e70183&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
