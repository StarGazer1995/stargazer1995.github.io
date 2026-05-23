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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7LFIBGR%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T125627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJIMEYCIQDL7UtgvJOcm1lGSnahagkuifY%2FzCElOfszJCt7ok6YSAIhAIPn12Qa7Nd8TdMHTBJxSkjZ6TxIVxFiZ1tSxYzgKdR1Kv8DCDQQABoMNjM3NDIzMTgzODA1IgwtrEFCk%2FIdhkZe8eYq3ANmHrnqKyOOt%2FvwAnjpJFVDRAYQF%2FuikOcEqU6cqV2xa6%2F5BGHAWhirUBL72NfIaGSELE7xYNkdqnLY7WLQTkQzLU%2F%2FG1mUncbuu%2BE3oG3Iy5QtgNE3vILfzRhTrjsDF3CafYKSBxCxtVvfKrtJ4J3eUlasaOI1RwpUNI2nhjBki1rrUDm%2FvuCmWa5U%2BgBAp8Vp9XQ248cF7XVKvtPF8WRaKx0fPV1NmUfGwGYyrTefB9SHiwBP7xT4BDZzUDpfdKa8U0yJRvcUAgcLI54PHGT7wzN12DVRka4onwLGlpTEf3mI9Ui6SzE6SpJjCLPOXRwbAXOYddR1bx14v8olDQWPLneLJpcPILNAcM84ZAkWHA9SRb3WIBh%2B7pviklKpsI%2F4teY5TD2dD%2Ff7SaP%2FJoF96a3LspaNlt%2BhCGNxOEjDXGWi2B1Wx%2FaTpLl9PgaRvguKOxRnMGlajOw6PQwwsMhCbwozrLX4hxgmTv6AqJD0JR8it%2B0IL8Hes3NcRfMesIyfsx2Wa24M%2FjkwORLi85yrED%2B9Yi4GTX7xim9gVRVMFuj%2BSCMs41MjfrsCErNEQThWYqQ8w1VN4juXsCxA6Sl480eVem%2Bs4IL9wN2afHtRP6boRRWfgRRw5kC9UzCukcbQBjqkAeZ2ZWRk9BffhRlSW1VycmwXmjNmeDTIQG7H6qPF%2Fg1P8En69Oa15zxD4zgjNQ%2BJQ0ZMGjt0mPbFH0mFBwER%2FOJkMCdX7pKlrWRIcpKi5qT5lgg2W2QnK28fpwb2lUBks2b93CQ36KhBBPk4kI2Fy20diHyGof9pOGXf9%2BtGaXNMsCjET2p%2FaaiNNLRIKfNGlOHkv93eI%2BRWcGFJWQauiWUyZiQF&X-Amz-Signature=d0654b737bc4193bcf7e03d72547bb1a972d66d52e6e0d9c59043cfc2d7329bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
