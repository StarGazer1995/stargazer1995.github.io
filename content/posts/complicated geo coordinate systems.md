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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3H7WQPT%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T170544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCCsKQDQpFZYlvt7feMlPe04L56gSIVixaq2qnizhB%2BCAIgWZynVmOnN8%2FMnLl4FPpbbn6oK1%2Fm1VvE2qo39i8P%2BC4q%2FwMIeBAAGgw2Mzc0MjMxODM4MDUiDCcRhITkNot7YajmRyrcA235oNwj05Cmu8o7WsyziJo8jCfDiS6vfeIw5wG5OzKAlY%2FjhoMLoZ8aL%2FpS6Iv1UBTNTSnce%2FQgljqaxFFV71f1nvJUol5aTTr0EfjlHXtYFpqS%2F2ZXFPr409yvShnEX7SezWpSvJOQMkoADshiAZUZpBedCsZQQMuxA3muuMFNOWZxAnDeOWeMtxQGxlUhydvu%2F9TpDweZM1IoIWu7AEFjvsHldwdqoC6Jg4QMdJ5I5%2F5ned6FMfhEcFYY7ahATaHUUC78yS5cIRQLTLkBcQRw6AOVzD8mjXEiiUFJaP4zoOJ4Atae4fycpkdh8pDNkwPo3pmHiagphOYWQ4Q0FlQotTAFIRZYdITpfO8EYKza4SUIhp5ezHAja3D2iZrZSUfZU1d8WyjJZmSqHTPhLjZ0F2mun4HfELeShknUrbFCl0V8%2FTyMtyoKT9jlqtDXVaJvJW5U%2FRfpgAdLqDa0%2B%2BZzBQ8kAcpTk0uhslxRB%2BuCJry6w6DcqUO2q27qENlX%2ByDOLx9m49enpit%2Bh2pFwvaMd7Z6tXLpZXffgkz2muC00aLxVI96FN%2FmhNNqRw%2BXR8XlC%2FOdJh173KotkumWPlLLJ3%2BIXYHGP5pyO%2BDNqOy4UU83T4ZMG4Ac9ntTMIHpv9UGOqUBzglD4T96EO0KlNNPXJXfEBayVX2HLHmjb%2FO5j8WEXBgXT9jjj9yOFa%2F0djrG8SJmiWC0YiMBwN1OPZzpJJ87CUwXNJb1YM297d8Sdeqk9Ja2YEkMnzYPpO9cF%2F3rtH67EIdSq5byX2Ibp5jWrOy1xg6s3qPxZzmfhAgPyr6F3Zzw5A81kz0OZGPmvzGSzvL5YgeLij8xcY2zHJyG3bCgaNppZEY%2B&X-Amz-Signature=ec45aa1e951783085670244efff17bc88adb7a1acfd22b3e43e1a5c29f30c069&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
