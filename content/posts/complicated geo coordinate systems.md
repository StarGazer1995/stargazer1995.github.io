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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXYTS52S%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T140315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQDp9tXqtkguzTyhS9Z%2FsBvvab16M8K4oKUdMewt51y6OAIgNVBIu9hfCdYMc56L8xhebE%2Fk99Zxy3cw8xGnuhh6LIkq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDG088K1LR7BlFXjBACrcA5T1LFJiMtGBxhx6Z%2BTCsZ1vJwX%2BtTj%2BlJ7G6kWCPRWmNbI6nm3f2R%2FT%2BduNpJtgKDeji9WnJrZBa6p8GScVqlObiKyWWqz%2BpD4a8DL3rI3i4X9G%2FJWTsS2gI%2BgdgjdXHZDffGugLiSmYcwyycpfGk6KFsEzj2jPX2zFTA6mDgp8cInQ5eSreRSZ4l%2FnLlej6HazJkbhvBTa9qUKyaL31mHvsVVMJpCVDYiQdUVgJnozxYJG4WYkqqJPDOf97QpAnvRvZtCvdmlLfkFBH1z1IkjlupAaxcQczBUibQkFmTE1WnJMtf4uFrcQNa3OxaYKkjk1TRdWi2nKugtueoa47YbnXU1%2FGROWg%2FSwFfkwFLyVL14KYbgmNawCZ%2BaOvAx7sUY%2FM2kdE%2BZlLI4hIJGL8UnmzqC1%2BdKyikzVlXCfe5PtXo0we%2F8fSqWAGM2EVzXlO4c8lhOyN9TCP%2Fl1wh2f2%2B70KPj15ex%2BBCEHxIRWyIHtc7MiySZQu877e%2BViwC%2F6J4vJjtjCQfqkBHL1roicSaBcJ0jwPqqZoXx2VSQZOOYZbyGIngnLcwX3jslt9cCW65%2BkxgxFVuNRJ0YKXYg4%2BBWohBX7ubgs4Cvktc8sv8bnuyyDK5nRNUtwSrC2MJOi79EGOqUB5%2BDpy8Uq0aq9B3Y7KlDQVATik6xJWVPEPfTWidDk7tk8HitaLlt4jg6F45wJMRh7tM1eP3IpdRlZ2%2BxGBwWzF2jRcnfGBGciza0I0VTG%2BXTcOW2UP3kIvLkBGUc%2Fe6JWejbauHUwAr0vLMdvZ8bgOZ4cd1%2FUATstUL1EPb1%2Fwcbx5TAFyJIPsewaUn80PxvXvPfJVzxwS6X8ErbgK5geb2PJsDKR&X-Amz-Signature=12e812447a5b189d59c5d2aaecbf2dc953cf9059d723bec23f0e5e1e5d049ba4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
