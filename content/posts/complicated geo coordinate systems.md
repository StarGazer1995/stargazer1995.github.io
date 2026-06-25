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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLY52DWH%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T103326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICEnf0LSfAx1LZbYBlk0MdK1po5NhIDpGwvFyftbXXgGAiEAk%2F%2BlK7OyuGiXvbsnNH7rzP%2B%2B0Z%2FQPWZUM719u1Sm7XQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDPy5F%2FbZCgLDneBy0CrcAxhBl5J%2BbNyOAqXOpLU%2FbLkKl7ptitUvaEtZSByFHa%2BpdZtHrbSzOD0qWp76JJ99byu6dusj4bPDWlWXi5KqakYYrjjXE1b9VMZQ0JJStx5kTxqCIdfGhWpdEfud1GDOGINglqCmy6DYGmVqMLqk7I9VKQ9Rj%2B%2BlUDBhmTSPk%2Bg147p%2FCEbU3NFqxske%2Bt72rE4yHd6yjSK9qLThf%2Fsmee3V0NAD6huViiJfGI04IoZYiGqfO6XdvImadiLcQnxXp3cAqLWKhiX%2FDG%2Bcf6N5J1reUWqxcsznH4PxUf0Jd8ASjEQWlSeIKGVEaavyvsVgx22vGXy9cj8SSvMP5d5ptnB%2Flzrgs7T5VR%2BQkCFVP%2BDbZnE69fWHqBjo7FHjaCynXuNQgKttTbcDLqnaMJl%2B5UE5tVnVGxOyPRPTlXVBNsQzG19%2FksdC2Hu1gd%2FIQbrX5KBl7qPE%2FMPAS8DE6Zy%2FWskUbY%2ByF62%2FLjNdUBHTHEIWbmbTH%2BQFbg%2BYZSCukTg5%2F%2BeHHQ5UFieWKBYXsFj5heG%2FESSMOyFoQOKPZzEXy0QS4ZOIbBCxSRSaKSwxUTxEsWNP4BoWtITpIT385%2B6SnQEWwAk35IFpWzJWVFXZefDPtcYKj0XyAMHdHbQuML%2FN89EGOqUBg1swWYsN6n6AQ3BnIohr9vHGzWi30Pnse2yfJgFic8OgVzYt8YvdcGui0fxfjEt3A8n0WVe5uBZLAFW0iNYIUKtvuyW85atfDLODlexUAa2H3ZsdB2lvTrMQ1CQ25O%2BPecX3CqAmk8Ne8X11m4Pf3EBZwE0hcCuG0bawMK272lVNBvr5kpvtdeY88Dlv8zNGxd1lkI%2F9XYgHPjc217xn%2FaKKy4vU&X-Amz-Signature=e4e2de3818e2ff4a838df06c276a5c18df8dfe044ec486b39241147b4d7e1925&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
