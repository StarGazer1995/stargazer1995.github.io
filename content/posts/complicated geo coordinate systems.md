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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXF7G2KA%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T192722Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBEfNx%2FXQtMrw4LzBYmdWslN6%2BUuo4c6k7vE%2FqUHC2V7AiAo9IDsoP1oPw5CrbXiY8uNvu3SLTQul%2Bx2mIjzdkRJLyr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLh%2BjZkUSvxnGC3WTKtwDyQH1kWHKEORbgZD1QEYsUo1xVOQQq7OWujPKAluv1a5ylN0zYhOJE%2FynvXWK97iFCtI4QjXqUhbFPAzLDw%2BU34nmO4e3zUmIGDDauX8WjOxOlUy3DpHmMtFJzodSfP36pTE1GiOD1%2FQEWd%2BG8r1EODZt6ta3QiqxQpNGdD3ITwnFxL8pXOzbt3NwelN00BfMy1DShn7rGPZH8vX8LB%2FAEAHhoMstsbDnKIOUWQJzDqPhbusV6SYm7Wal9KwhA8wF99jXSehxFGpVzY9nnYLBHxBj%2B1oz1KWIEvgjNf9pFecHdqHEONIXHv3c3GvNXsQSbfLyhwRYuWd8ZXi0yei92fLT5mX7I%2F%2F4IayWBncyYNmSFWjOY8lQKWPD0ayaccyIu6y%2Bq97ODvNqm77lvpuoPozlnCLBRjDg56x4IF4CzjUFmww%2FVpr51F7n8RMsZwvJZCa1zrgFb7cg951WxMCXmmAlmP%2FSOEf5jDpFb1eSurWYP4ztm0pOihhoRoUcOCIYL5gJTN7QcsF%2Byb61%2FP%2FoMLkUgAQaj%2Brs5Fg7wR%2BlrCPuFewMHhrqLyS%2F12M0qMi3WmuOm%2FgtacW%2FjdRqkyYc5noDHZ9c052LbcAJ8NpUEzWlbcivyKdVsks9P9EwxabG0QY6pgEb1E3QqLSqT7GdCJ9jkKG%2BAexWUlVWm1f0MpuH0EqML72IkBZXT6Yj7VKms6JqJS1QYpjRDncFOnbUvW5Jp03Sr11L4whoQrA1I34U9GT3ZNFJq88Cv%2B0wMB65mDJ3C0vToN3B0kdy1xQQVDhLlVG2qaM7oR0k09iZguzumDkSqT5IgQUypZc6Ss2ipb4rRKZalNsY6InKyRs4bFBktc2Xdbv69tp%2B&X-Amz-Signature=477ca10e03857417c6ecf3fc593aa5b8543a94a56a28bc86c7791d10c345514f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
