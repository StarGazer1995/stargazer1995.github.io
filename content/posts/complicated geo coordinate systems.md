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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PKNI37N%2F20260806%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260806T134238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCOK%2FEZce4bn3%2BHnNSSZL%2FH8ZeE%2FBZnP96lJ4yssDt0bAIhAL4ajD5KZhuNPZsAu%2BCG8EiPPWZ%2BTXO7zn17MWnJaQoJKv8DCD4QABoMNjM3NDIzMTgzODA1IgzHLOrE6gQx1U7EbqYq3AOM7evLRb55aj%2Byi5n8FjFxK3dZdxT6y25TPV8rNt8Azs%2Bg9AfljvExX2Ss3UuG6AZK92%2F7Ko6uJXPrMXjecYrBW6KCyoeZbh%2F4TIS3Pc7AYGQDCTaBKU%2FzaY2HWWZ2TrJbeZn1dqw2e%2BSwxXyuaWzolVHI7hB6O7AOTY6T%2BhP%2FjTYNTZp%2FPnTtI99Y7OBIgk3E5s70dDEj1gZ8ayjT3ncFWKGCaUU6Q%2FDrDIxQ3ZH7CJAz5tb4ZH1ul5Q4EiUNxUN1NZDTInJMheePQiJeSBAkiRrRuH%2BYuqSYtwxpgaX%2BjV7dS3Udy%2B3EIidJ4OSP4OWm8IcVA8h2ishphn7DbQFg1MZZHsMh4q1n5AvvqSadf5vcp1B3aYRWDiGQzeGGmlw4bcsgk4VHcRfelES92%2B6toVzOxcsqlqMXHXPpkawGXKu%2FaHxnJ5F0NKAVZg5gNgQuL%2Fq0uvNvT%2FMbZROYgZcn6xcmuGR3ufPnozUtfQrzd8cI0tMkJinXd5xOi06SCLUwuHTCwqbwUK5o7obHx15%2FhMk8AaqqTPHXMJ8i7VquHI1FyR1jYDTOZ0i3H2OCNS8%2BtG37ySRN207ttdDC4i5wRJfAea7kT4qiTnNc76i0YEDgt5Ft4lPfXLxmoTDHidLTBjqkAYMVb91yhpXoe8VqfK3iYTHNTA8q%2FqXi1JfoafJp%2Bl1pWFj0kIEMpdVYGi9RQKHeTnqW%2Brzhf31ocAc91VJyxKbyrSb1HlKxu3HNOteTags3aD%2F%2B5ZSuDwmur2nVEUtBo9FR7wHoX5OQJ%2B7JuGAJqJaT4x8%2F0ABu15uvoYQ8%2Fz3Fzb4MphPMDUgcxT2pyT6moOeYf%2BQaE4wTOEVIDxS%2Fd7ipcNzR&X-Amz-Signature=2eb2af0c24c1aa5fefd4532c351db858422c239595516c3961509561000e0d70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
