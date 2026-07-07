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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AMYRLOH%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T193134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEU5Nq1wQuJ14jPeBA9JaEapqU9TUjMglX8BRVgUKAMAiEAnhNv08BPyFVHvuRFbLzdOE2vL922XQewuCzS3rwN2qwq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDLp%2Bio1xgRYpZSJqgCrcA%2FnanYequu40GlR%2BPY1CVRnUdsKIkdMVyknZ7cVIJLihowKZDrfGUjLexoNwLRPLj6PHhjf7yfHu3t4ulij4V179kSE2U57eLQkz6o3bPnwz6Q0CdJrW4EIVwZ7B7Q0VhGkrftuDHMWmWq6%2BYdfExwWKHf6RdmMtwQizwoZ7W2PagdOF0GV9dTRLCfIRkss%2FgXqQgFE8o4sQttDsF0NB2qefbZzDO7OOO9WWUpgatPkYi3s4qe2UVvJgJlbBoej4mF%2F3a7i4qfHgjfRdexSAeKkJ8syPEvcGdEGuR1V%2FWlLAb1EE8OUKnmdgLj52Hm8PnBd%2BeejnKw1PktVP%2BL75PG6U9wWgsN86ghlIrMZI1eFcxT5edSy1771GcLOlz5Rb%2FDI6kNfxurtt6n3TIGSXpbv4BJ3M9CisRUl2RxU0l33LppDwuhjje5KoQmEy17TF3ekkEFt%2BDOXHth5pJsIk%2F0EkqoqyWrLQ5jdWuvzeFVu1qJHYyzg%2FIPF08%2B0VMuon7XPSpw%2FZ29gj4380xXFLtChPxsKeXZfZVr8uMbP%2FilcBT8oyCP6bYYsYl5BVI7yRz5c4Q7AlTEsPFr6lAvvwskaOeJH2fB0PpRYzXy%2BQ5jB%2Fy9nUzIP0gGQgumJWMLiatdIGOqUBIog%2BsahpVD4nY1MqP0ZqtydVpNldl62Rp88xsXx4VJWlFxYEm8gU14Pi94Z2Y0X4amkTrIngF1YO5mEwLhEx7yyI2VoeGMZJ1vVf0XTJLadBmby2WNh8%2FPWW3sCZTPyRuSpM%2BKKEXwTQUkVzVlBsyMSF7m8ALxY2fdFHfrc9%2B%2BaRkdmx8JVdzvLcgUkRruCSxKuJpw36dP%2BiTLNsug0pJ6N5sFg4&X-Amz-Signature=d6c6d1617d06b73bba970fc4306df46521bb2656e39aab5f06cbc8c93678e4cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
