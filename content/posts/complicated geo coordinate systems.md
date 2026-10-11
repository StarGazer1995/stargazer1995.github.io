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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFES2BQN%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T102434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFMMaM%2FQ9AfuCYCUboSYxSht6uibij0o%2BGUYSmFv19XiAiAu91FmPQOqJM0vOTYlCGf67F632x4GpCdTroIn8wjjrSr%2FAwhqEAAaDDYzNzQyMzE4MzgwNSIMjZloPwZ25BxU3Ce0KtwDrnv8l%2FNURF3f9daRu6i2p%2B7%2BjppcBlHTSDhS%2FE7Jdflp6Z2h4lZMl8xFA%2FQXWZtjzWJyIy4HakAMqKGIcoDEYzXMOd16DZoZfMucI6q8BLuIMYMX9IfP8GKZ3Gn9hClN0qMuJJS03DB2fsTsa0BGDq7UY6gg5oHC341TS6k2id2eea02kFIZgn4z%2BU325cM9w6YOsz4QLwPQGamTViZU61b21bZPQe74auJBK85KBY1j%2FGQ8Li5wSVgYIi9yvdIQvonQEmw5zedfXuo02QViN1FO6FwkOPbVvC4OmEAYcV7doCGGnjNyy6f8CBrmLN7ZxnqudK24y2hg5dEMcrMjUH7IhRG5qTToJOwstEKz%2F%2Ba93sM%2Bql8qcu4Cp05VDHHToDS2MnnR7L%2Fc626Vp0vCm%2BlZ8vhwIf40Ey2%2BacV4tQvMKhm5N3SXEGl6WpVqH0Z5%2BjVP2MzkvQJClyS72Ost%2BWbFouEknKvT2YMJ9aH6hg%2FSliHMEy%2FQfdaTVIOLywuLKLwoZOwD8zoLdzC2Fct00RRO3LV5gb0Kh4C2DB5vsXZ0%2BSvHwR2c22p8kHGlf4Zkj6tdhJejrjTKRRVDrt46ntbNbqMCM88H3ghcWU14b2jTZT8r1whDo9hKRvIwkKWt1gY6pgH0AKVASLSiR6KDSEaUZQCIjevlO1wyYKOWW8pD0f6UVrJ2rJqV43BL7k%2FOrtq93FciYrm07F5%2Fny9NwqiyCaHz0kbQu9MUqbkitIAGaUgvPYROxwJk7HF9nu1mnN36zXRYbKdWTk9K4YHmN4JCwpTlUNwmmY0FGyArL2nfR%2BUR%2BkoXTA%2FZCy2e5%2FRP%2F%2FclnhwNyCRjWQ0OQLYF7Y4M2kHkEyuk%2BMkd&X-Amz-Signature=a02d854e0a8a36ce43456baca9ce9f3b85c60dae5c2341030410e936a11a0eae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
