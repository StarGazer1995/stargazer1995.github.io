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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEWXBUHD%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T115324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDxjDidDKAFe3%2Fxn9v7ufqH526QehAfq39MGeINReUlhgIhAPMoRx5JRV8dI4nv0w7GJ8dQM%2BJirz%2B2A%2FrtCPG5VcKNKv8DCHwQABoMNjM3NDIzMTgzODA1Igy9URzXuv8u1hwv65sq3APBTcF27QTeuN%2B%2FQtE9c760LLDePyzP7Fg%2Bp7%2F2VTAtV%2Fh3TdMXABxpemnOkQ0jzQ35%2F1y7GSdqgVA3Gd%2FIoVB2AdKMxOkMi6xcj2bi1XOxoBJOuNQTj2u742vH%2B8AupPMEczD66AMCq7wGn6tWuDYC%2F0cdtOmop5sZ%2BmQyC%2Bpm7lpKauOAiyvSEP7DT7xbn69iDBjV%2FoJlfyxbGtrPOYbG%2FYj2UUvsHHliEmwA%2FF1lHMM1vQ9f3n6O1VRWoKaEBCnxSxei55PRn0sg9cW7QsKl%2BjcEgiaZmlZig2TAvd7lCBJM9XJoQBEyfzOtO%2F044QRASJ1aTaeYENoqEFbkEY5W64IK80i7yNR08Z1jxiuR57GYkbDJ84pM8qy1PV7ET%2BwCnPkZGuC9BMr7LGAiaMu%2Bqal1BXzEuRsCuRLMmQfuGp8ShRkWu5C%2FAZSPhOzqL7nYLX6Wgq4Va%2Fc21K24slzyYct5Uy9fNrP%2BSCOr5PpXbvEDRLl6s%2Fc4Cyxzm7jwOI9mwS%2BEYymQyDyePCDk6fH0ZPCaga1aZT2qQw9yrkQkhFvIcGZ8yrRJ9BlhECsu0KDXuSffCLUmhWuYWPXl9rwPmGB4ENryyfvA3nTpCUtgWYxjXTXSL%2BaYcr6HbjDBtqfTBjqkAf%2FQunXIg%2FD0b%2BhzGSUAwTAgmmVJsM4HN9P86UvRRwwHA%2BGYpJtJo1v%2BHUtvARpQOkXz7SCd%2BmSARE17%2FiR8kmiAOvcf87J9n63l8nl1VfXxTAdU8wxgqrqirR9MOFdF%2FzOv%2FQaHtmCG9eCr5F9Ov51lX6li8YeEi9u1LBKUFVGkmJkLu7%2Bl6S4dCfF0%2FjWNYNt8rQn4xfIubyjlVv%2BGAVItayhf&X-Amz-Signature=d465c6e480db8ab072bc62807e721c144a17eba004a06ad7ebf248187f1f5f3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
