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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SKAP6E2E%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T151105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFp6xfP%2F%2BaXDaYW9BwV1blT9Y6EgQKIIe3A8v2hB8JEJAiAUgXHUFE3UsISDrDKVXmt1inpgVi%2FFrULmaWIEH%2BsolyqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMx40inyGRPmlVKtfeKtwDT2mursSb1zjl4Sg5t48skqO8oAHJOCnfkfbH6dgQZxoG7szCT5iTeQt3RFy7xCae4O24fmd1d9CnVzbfqeRDOj7uuWe1yJGKHrwnBkAF6y8Pgrw7kZdnTuXAGn%2FlB0oX3zIMMZpPXNAh%2Bm5QSJcDDEm8I8q0kbaAmTZhNHftbRLPEDka8pzyqWeb2T%2F2cLKZMOvahEk2iWE91UhLjgfGjtCjfkjFIKBFLrIcqNu2oxIQjWZP0qA4nv31jn%2FGDbcBsajrVx0qKUSRZqV3Fg1wIyl%2F82DrZLh4yRlk3k52tO99982rAIxrVY%2F7rthkdweEEZyKjhOqs2xQUdIx7icN4msPuCGnRdk7ZH%2F8wze6pMvQWvAlF%2BitoGUbr4%2BuHWhFftcB7Pv67M6%2F1Gb4BI3SAfywQjlWzNL7oixLx70SMp%2FImqWA4V3khj7F%2BF8qLLJrYUgRaz1luOUVlOvn4vwIn%2FfZxImCesl5wu87StJh90rEqPepYviZrPMlw%2BjcQ0U%2Be7ux%2BFFjqnGfdThcSeR5wb%2FNvw%2FDPYQzMwtaChs6FlNqCmZkBeJFi5t%2F%2BAUb%2FBFiRzXYhUww6wP4tNIbOoIvGRM6AEdc%2BxtHaKi3TJzTCgS9aEIGv1xs%2Bapi0kEw%2BNGD0gY6pgFpurS6ZYd6JR5rrGjAEy6JBcVAV6L6HFMiEhUYTQpmWUPbAxQtYbG%2FuGlkpezZSrVkPhp9ZAkWGMLwnF8YdJzh%2Bdih7e%2FAOAnU4mUi4UJBwAZ0vo6ozR%2F106CCV2Lx1kmlEG1kd59lxl4OcVKJedill%2FqS1gKxoR8pmqJzSKfpXyOx8Dpakqi76JZ1BM9AVJGFDMPsOOjoBpuEts9teRWHWzxHD0si&X-Amz-Signature=6a8b98f39c3e70ad36b7eff26cec8105a03e884d2177ee13ee1f47d75b9f5c26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
