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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JGCUY4U%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T092254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBb5aKQMrzWAa%2B%2FmSQzHZmaK4XkH%2FTZzKn1P6VR9k4N4AiB1ZokMzBmFSYsz5mR6590HeJQWVBfmYH125mytY4wPniqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnY9K3dCu8wWA3wBsKtwDcORIj0rdkPCwf319FJFPAzI4BH%2FUgywoev6VDP%2FFkDhcSJoQOeJRpgipf65fpy2q4ngN2csVu6T9a6y8gkhsEOyQ8ztydtxQiAJeuxdvUjzf%2FV4TirsjeMQ4N6XRgH8qw4Q0SZEyGBZkY8lLxwVql9x356tb6WDMvv8S806NJGsdMW2aN81pPc3NP4ztMremBgDvJSVcazFNdWRfdqT1iG5Zf%2F%2BaO1zxzu%2BEw1I0zPNg5CKG4wnhj7XrO2ugmGI6RxSd19QGpKAFsVgC4ydkiJdut7WMkl5%2BzDujaCE4yz35VqVTL1XHG25CkySsR3c%2F5kEFSAvraBWtnY2EHCVLxeHv0JaTVQ9IErhao5wYM323hlivfy2m3bEAWa6q8KQUdZNUHvrw9YYAYHMJT2Drl6MTGa%2BWtiRVokUmhpDY55uWkx0qAnJyMKE%2FcbW3O9lBmySPDWUCtKXYR83riD1qhFANztksbJYRsDzcwRr7KB3DhqqW4SxTX2yxxSNVKjwlQPzebeOpLrOsyee36dmyRGkfCjDxxeSVjw5Kc964723qGAE%2Be%2FH6pgxN2hjIvWWhtEC%2FQCDK%2B1l8qplAYbBhN66Pm%2FMvJEdT8Jzz0omYTvtiBP0L6f8xpOsR7oIwhNLD1QY6pgGHSDaJnNjz5rUfyWga%2FgtFTfpjijmvsk6f1DymBVYjMD1W%2FNMi1mT0dusqZG1GimGCZgxEdufq658M0%2BSYb5L1V6e8oz5JVpkSLYLgy7gBkCc1vUBOrwbKdj6YCl41ru%2FrUxBH2i35Mb1U7JiHy5a4lyfwrUthOuOxdivdDgHQz9x16E54nTvXu71m3x%2Fi66N6OsV%2F2B0w6roVpkIZG7xunM6BEBPj&X-Amz-Signature=a676c5bbd9da54794327898a84daee9ce584d2ad5730a165fb46f253f9b69c56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
