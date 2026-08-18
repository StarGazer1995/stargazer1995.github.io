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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXPEXX7Q%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHWCVf3DhmKqK8eWyx2jDdO3UKigROBxdP3Bm5dSofjdAiAWOgqeL%2B%2FRO1Wq8RUXWs%2FdR1oGrDgd%2BDQZctkyc3%2BN%2BSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIM6g9xZ%2BpIZLjoBVKYKtwDpFOSWWwFs%2FDYUzC6Y%2BPrSZO2CLEWqjXbPJG6cQ2LHil5qnYxNuVeYb7ezgmgr4yD40cduoYC6Mx7EHF6AxoLLsy6YhaV0IHxR0l8xhNG5Fp6LpsjmkwOBN52ieVpiK6Tb41GIptvsO7swB81xvvSbYRsV8hLBuoQq842D2LqVggCHsYaGn4qXkOerImm4HDwwidmzyW5xg5eoxn4TNhswasDANlft3of8sw%2FYjF%2B5owkz2brCDYZHgU8debpxPycYwHyfp5HyHYI8QSze7ArweH42dym%2BuHFBBcTxKHG%2BT3%2Bl%2B7nmQnmAnGFudaIUxzXivDGS2X%2Fmgv7dJo0vPNmOWk6pH6e8idHWjKtEBwHxR7kSU87IS8nFJ7e3SSg5jceLVIg93bTcPpFIIfIibpuNIQc6xa1Pv6A89DOd9cF%2B%2BKkIYA5%2F6JZ1HF2NiBD9eNugzyC5JqqE1KW0nnoNf81QMQtYnl4ifGrshusH2HBLFpwds7rwLw8sXQ7xN4MhgFn%2FCLiJL38bHV7mfT6rHkMyUTZcOzuMyEj31eC8NEtXLXdSANzXPu6i905Ng3fDke8bCbOd87Mu8g6DxTNF%2Fc9XqmFJAgUh7iCHKebxiwdYe6C4ySs%2F6hjp3oeCEkwsr6S1AY6pgHfKQEVQexKn%2FGtyFnz1m1y1FOfRV8KWOCG95Gs%2FOkkv%2F6lZMoFMkCBzjzMerXH0rxFn9was%2F5lpPf6WkM1j3q7QXdKtg%2FgG%2BhN%2FJRxyByVAUU1pb%2B6%2BCrCsuFDdWq2%2FTuD%2FrdCQQG3T45Hh7fDbPvO3WTCL9B1vJouqV7nUDz34ctvPl0jbdU5q9r22qgTVOWU84ws5YhsKTrzvHfnVnTW71ZbCBvu&X-Amz-Signature=2fb21d78e38f780442c6ef9143bb24ed827cf94e7b1ee6cf6c790a45e60050a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
