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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665GONL4GQ%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T151414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDal1TKct3cD5RctI36kYekzXG%2FgLqhsmbdFgjT5%2BxjgAIgRcgutTj7Ya1PPMiSJJKVlLQdJRfqvCCucGlpOc6hupEqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDNhgt1QfLWnSZFeVircA8vavcrrCRDcAjOTunNK8ILfVyrwfZTzvMuj9bXi0obyq0wEFaw7MnUwYXRG5IgZgUjLhgZio04ggT2pzp%2FVF83JHLgrOKewCgSFGuuRYfYd75tLASfYy1PDifENLXjOTr%2F9y06hUjLzVvvEjA94fJ3DeqcDwPWP1dgqDzAABlZm36IqYBiGnTjzsAFm4m46JK4pdviGid0%2F4WDHxoHLQ5BfV3qw0jMzpk4pivnZjZJHLxVIM9XlSDRnb3LU%2B0cvEhDXKqZQQfb33rHLTD8wSPjB83dK2jZTezy6DkeDsI33bG5oC5jCYykFDy4TlfrP4rL0MpRMFtCjMBPv%2BF6Ed0Xl2cH%2B6ITKoPDDUz9lahl27GnYHMVuM3oq8kOOAVW9kVc%2Fd3gBErtLIxXEy9%2Fd%2FPyVJJqKN8tT5ydBDpK6YhQCIZOo004n%2FPpdrj1zGvA8CmJZTo8zJdGhfti6rXKIupcFjbD5DaNT3vSKlWdjTI6dWz31GutoG7BdtWdrETE7hhuR9Zwh5Q9rF9m1pEBhllJsdyCCL8AI%2FXrvV7L%2BNVThdNj2k%2F%2FB94g0dv92yjv1j06%2B%2FCN6sXXH%2B7ReKy0f6rgRvUe3IAXdCeNAnpI8LPZGhq6cSNL3y0aEzxRgMIzd988GOqUBURs05HHDT6GbEM21MZaTrMkjSUydPzTnSwCNRJgyv6tAWmIQXz0Xx4kVQU4s8KQIU0z3JvSv%2BKvs4kF2t2aBr68MRJ90c6XbvcQP1jVrfMTMdwv0L%2FqlHJktS3altSChXVezoBdBZ4AWIPwD7TTJyazIU6SACH74YoZGEYsw0AFgURR1si5PmLRdgt8W51MiZvh%2BqjxrRFPnkvWlG0vn7AcGCNMo&X-Amz-Signature=dbb023a0039ee388a6eb0aa52c40ad79346bd40f342ebd094a36d91f31fc7dac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
