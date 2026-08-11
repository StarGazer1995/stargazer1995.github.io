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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWHMVZIB%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T164503Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDc3t6icYhvV2caJB7NWETS3fmDcdT3NIksZi5guFX9ggIhAPjjA6yV0tu715V2frnfBfzo1HEnzjQUnnnMvFGa1NmYKogECLn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxX6j31eQFNhngBg9cq3AOByMAGSMbglkhqj8fmv5lJJKpht93gkQlkZYA2mPMvkXrjgas7gWte5hV0Y%2B48s0s%2FYm4gOWI3QZGRf4PyFsZLJ57jCGf%2BjMsq5rETjELkXeh0o4Z8ybL0eyZ12ZgzZN2HU%2BD%2FsZdUtvabv9xbx25nId6MZOd0tI2XOWVA4tmrga5H%2Ft6CDX9GrPSNVIhjDQDxFi1loInS8oeVGTpKyQKoAwkWr2pG%2By4%2FawmBMPF33ACcMZzHmSEvfvZTiYHF515nOCoSz0IKDI4k2zdoo0CoFmGCt07HTW9Gs9oXWsRGAj33u%2FPYYLNwNV7wEy%2BHPcQqlH2HWv6WzEwfdU0HTyiNLWkeOO9Nvrd09md3mhY8dAYIhYs7Dx%2BSbqU2ccuw0GX1C0v1Sy69bwXjBmGorsEbucTpZKSgAs%2FFMrkwy2S920ihqkNTWQapMn2tMda4%2B7nIW0cyq5ws2R13WRsscJQaEy06U2eiFnhVf4uwV3xmtDNyT%2B6HKyAJZ0hfEEAKwlsRyvcDh3WsKl7oZNHmcC%2FhsxS4t8WRS32O0WIanGfEi8B2XnRLRCbIYCRRznR3rgn2S4wUZ2LeWWQkHDo8rgWuQC46yR%2FDwXoTTk9VdtJiGCY34tjRkKC9sSqlXDC%2Fhe3TBjqkAabS3Cv9bIwWAmItio%2Fi2TTqT%2F7pGN%2Fn9v%2B%2Bk8EY8KJImeYumGPtbi%2FzP2ZNo7rB3M0uRvP0kvgoD3%2FwJKhNSioAsoApbAx7BJMXZ%2F3qKyhtWZUl2ZPKvocmEeV%2FpQ%2FpiuO5ByTuO8LESvHbwezT%2BMPqwP%2FlkcY1DrjMFqTG4tIXgRQcgGiv0kJ5G9z6T%2BUYiCAiWUU1Ohvgx6P2fsmBQz2q3o7L&X-Amz-Signature=9d9018a2f37cfc56dc3e8a680b37ab9a409faf217ef846882c97f3b975ae270c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
