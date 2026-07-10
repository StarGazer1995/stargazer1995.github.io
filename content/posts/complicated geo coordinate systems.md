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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWQBQGCO%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T205910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHUHOWr7ns7vb94FY7iLF011sfX1EXZgTooJVfzizYUuAiEA%2BslxATpfUmmRF%2FS6Q2lpAqWmb1zvPXTMWXftfOr9ZWoqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMKoXlxAPY0ZbKHKiyrcA%2F5GPPGeXliN0%2BoL3ns%2BuYB0%2Bh51JUJq6FBkiYhgTzPouWyrD3hAJ2FV8OcDOmeymZpNi4EGq72TH7eM64i4fq4PfCEo2BAXUKh46kjF6wtixCuYaR%2B9AHWa3coT0QH7cDfaR4bX9Qj4T%2B5IMi69cbOfYlqYcY2D%2FP2JG3jrtYl26kqKpeqw%2BmR7WufqrMwI7YMGNxQMnuvOUkmLGiAZDsP%2FmSqw9s7dChj2UqlG%2F8LBXE80khhkPUUM6jsEkV878xRsIc1AbV3Je8R1xDrt817PY1Thm3yxZe53E9GHw6AAIjukbO1T%2B3PTdzYM%2BeVPOpvKNKsJEBo18zTxbm%2B4W4hi5w3Kb0UxkAge4zEeIrq3ncojv72jFZmF%2BhgvY%2BO1p6ugTiIYjzEeaosm0JYNWYCpAQafKOOe%2FCWh%2FKOl2AgDFoX%2BX82uCW5b1q4ktZwuqyxArtep%2FnPjpg2YV16FlOCvl6LJ1j64EdKRuDZCcvSqBo6B7i8d%2FLqkWPO2CYoTQ8zHzW6em6%2FPiUZkAAt9bh2C0ntHhCj0nTxZCpum8swSPgILz5uFCwsZIDKVduYUrr%2BM46O18G7DRKQLolaRvSzbNb%2Fe9EFYrOqzjuNnGO3MVPEOimXyU7cEMooIMOqWxdIGOqUBoIj6pf5Hf4GJCZ8TiILY7k1c%2FVvz3rMs8mgyLAi6e4rBNM0bfFRNdEtVvQLTVaNT7Fl52SBVrbLxdo2Qy5R64I4ccwnP5L1COT3nsQHxt3%2BHuzRr8QJdznmzoD2b9CjT8ces56jW7fscJZQQtKkJ%2FOjW%2BPieu6cqam3td6vc9OwDhVDFvvnb4F%2Fe9C%2FJo8HJn0ywXCePJs%2Bad8piIQtixRodUw4%2B&X-Amz-Signature=aa4e7169f8d66b2dee9428f86db9f388b14970eeeb75f4d97825cf06ef6ab7fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
