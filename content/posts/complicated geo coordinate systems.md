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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672ZJU3LK%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T080141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCICpS8NrfQcTtp3Vj60Jhm8cV66rD2mis1LcqUp1v%2F%2FwQAiEAlvLQG85Cyry1MDmsKIDHY66%2BI%2FXIhQYdFacv3pIdrQQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHVbqZqigNmnZls3nircA5CckvQa2Z%2B8bJsyPtozvRqZkSOiHuh4hNNmmXcldbBkUTBzg5ikrsya5cfYsPuKtHO8GoeUU1c3OW611SA%2Bw4naOnjX6NaYyyKOmH1q5U3Yv4fv7Igo6eU7xZoV%2BU5fE2EvBSoaBZuyk26%2BM%2BcMP3DiFU7I5GcqkEQj7OCK5uwviiSMrbOH%2FXax0VoUuxqpJqDz95MzZRxHDZMhuR6n5%2F1YxiL021RQV0zNJazzBV%2FGhA%2FrI4F7CYEqAHQY23sTfbi9Y8deU7iP2PMDR%2BL8Gz60tLj1DeZRiScYsJqM6BVabOL%2FCOJtiUakPALljsKM6nE4U8SFoH%2BOvW503GkBdNzk1NBCKs%2FGxaZpTYH6CUUafcNRMTwi7unRkYvzT6b09TZbvRXAzOo1cM5atYIC9xNH6oaAOWsWY40D7dBhSGLJlatg7tDI5xoF5HiN9Sd9PfKp%2F4GYIaYZuGZ7a7WjU7juqbxof0hEevYCeWdwUSCNuqqcrFCdUiWVO%2FJZ3uGm3%2BSK1TuaqksI7B3FvBpuc8EzowpjBuXXSmt616o60IdVf6Q%2Fj%2BOQln5nHZYX%2FJN0W%2FrgANApq%2FFzhrA%2FmOVBC%2Fl7TwnPf3%2BxfXQWg54BIBJnHrF0JqRjmzhAbMNWMKGqu9MGOqUBy9DbNAzqBGUEmaCMNTrd9R6BWFDBjGGP4dcXEmzKDHiso65hjyXZ9L9PxXqwXHum5n%2BeIVj%2FA3s%2FXt%2Ff2hDgfXXbFCgFTEal1xk9dpy1W67oj9Mq0Gz7ZKJJFbYCQAl1VOZ%2Bj7wRLpVE%2BKjLX%2BOf8DwTxGwLfJr4zqTxNLn3zW%2BznAbp3NS5ubqRp6zf2gKBIuUXdLBhogJrgAtbSA7B%2B8kzRGHa&X-Amz-Signature=e03946b2be15060bbb1c7cb69cc8155b9378300a47aed01f9260e148eed8e706&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
