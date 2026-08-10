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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQHRDDYK%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T124037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWtRFTohlNmu%2BIpeVJTmLVI%2FQICdhi6oDyQIbIG3U2zQIhAIwjlCFC1f02xEakRpYJxyP5YdZlnI3EhfBc%2Fd1%2BM%2FeUKogECJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4Rn%2F5ByGdCxHRgfcq3APTQddWDzg27mJbyRfGJS4ur8h5mQBFbrlGZGnmoLqd5D4EmwDu94hhHgkkAEvUDxJQykAH6YRFgyBwMEpkZO3%2BjNODHdA44A%2BKfLdD4yycbRna393lM07UltovLbcVIUG7drQRCNX1Sm5qCYlmTAFGp8zT4U4bd%2BraOiAf2eLJX66BAmTmSyH6YrrYVfcLabTQiI9NJwzd8CblJ5G2iD9cJRPOK8Ln%2F5UnlLHRZIxb2Hyiwpsj0C2azdLf3AkceXWF18sP0qh8gtSm3gkJuD5gqZV32KC7T518IwW8tHZmQXgreEOLdVzGyopAvvva8NLeO0tHCU%2Bv28UyRmzJziuRN8HOUpA6uuHrJVV5NLxWcSqRFtun1tD8wvOKSYvnCFcoBLuvO%2FCOGxS%2FNRnc4dy33fF5MXrCl1ywPvoY3E7JX%2FPWjFAAlz903kOTjNwoe5YTEDUUKjnp2NQcJKb3sIhyUeqOsC0%2B1Ho8rRduSyMnDWY2YO824ww6s%2FiSbAVHy2b5Sq1ruWm46SWD4yj3cseRAuQcD8pZCTuRwcGFnNuRZza7OGr9qM6ewoWPvkagAdoKRV%2Bl%2BTQkVIp2AxlC2PB6A%2BYviqHu73KNMrQTLNnYmXyH6Qa3GFPmSCBFGzDk7ObTBjqkAZj9o7vQYyWm7yPE7EV5OYMz1%2B0L4%2Fkc6m4vt2m%2BtU4T8PZmwgzoZoTVVBc1Z%2Bsqf0QfXviML4xTDCGQnscQ8nVRasUhqSzh19oWOp%2BOzd4jcetuxQrH1TYemx3K7nLYWEldSGGcwU8IoNpmVEP5OcGsMldkTiFG6Be8e9tUE%2BMuYMPTCfq28NN8H%2BX9S8V6GaF47qFD34IHuagxfo%2FcGo1fng9S&X-Amz-Signature=6b138408305ec78f3287e856a910c5917f1298b87e5ef957836fd75a2d7bbe34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
