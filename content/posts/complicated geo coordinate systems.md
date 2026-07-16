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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663BMUCSWD%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T185357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQC93Y1v4aldNUc9WTKo8k49LS93rT3f3rEDU5iyIetlyQIhAMYrjbjcZmyYflmayNeX9cnt%2FYyigD0J7RiutA4huQcGKv8DCEcQABoMNjM3NDIzMTgzODA1Igzdv42tg74qD2qrS5Uq3ANobD6ZF0%2B%2Fkev%2BYguLw1fNVyusK8KQBgA%2BsZnZGwlDThR8gzPQIzFy1Mx1QaIlnHIm3StlDItSX8KQEPNDm2NlxMWo1r1yShUPzFhBiVdAzkX2P1iJ0Y2GnefLqRF0Lkp%2BrudBmsWY7Ym7iPTMqJAsAsBdFbokR9CiEzr%2BF1fcxUkjFZcto0%2FCnA%2F6UjUoRfajA1bufhYQIkhkHxgkh3h6dexcb%2BKrPQU4dnE0Ly8u5FpkjykC3vUaTKGX80z8LRgX6aqWk5BW%2B1zOkSE3VWSDCTIJuAfPRiW5bkcgF1calTFUbt7IqbphRd6Jos4JS6u1pQBbRmyuw4%2F38PLikZt1yzdpL9bjzn%2B0579vF%2FeINjUX1ZAp%2B06FQWN1LCpJWJyxZhHLPJENVEBbvOPm3qiipXT3nZgJ2zb6l5HaZgvrc7POp5iCb0xFBLVRXMlg29%2BwuSJk2kSy3Lcr%2BpoVj6n16e%2FalcZwqTl2qzWO0%2F9L54CT3pbRf2J8p%2BQf4Twf%2FV1%2B%2Byh5h1TqpOp7GV6l54kp6ZpZaq663ZOYy2i1Tp07LdK48rXYTmtvsZIOCm6%2Bx150J7rAl3tdVrnoOQYi2kZBHWKxT%2F9ClQcSby8VjTsnlOS0LJVDne815LqCpDDRwOPSBjqkAZzhRZIEoojCopG6xBxqiWRvyCl5Q1PHbatMFfzhZqdSlF69S%2Fmq0gat2aroZVYkn%2F%2FQKubZL%2FIKUxLIAwYCR4mH13M92hLfTDgOmXLLPhsDSOu4eqsWkeNGS5icbcjBoY8Sl2PN7LJ3%2BTEGK67xaK8utdEgpgzAVNkb9n%2BLdugdb4g2l9NwwuLEc%2BM9yaEBLgHhovQPP4aYG2CG6ekz2CT8mkj%2B&X-Amz-Signature=6e98d0c113a6b8128dcbac3c53668f03583a8f0d7a10a3f2789d18505499ebcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
