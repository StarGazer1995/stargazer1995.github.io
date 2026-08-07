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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652ZN2VW5%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T222425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIH2PfP76pSMtCUPuEmxvLjkzE4Bj2O636Vlmu4ofZWvHAiBi1dHn64u2atHGksB7s5LTQxt127P2905XxEOZT7SGnSr%2FAwhfEAAaDDYzNzQyMzE4MzgwNSIM4Lw6TRcgsNzI72jLKtwD9%2Br3Cm2N23X%2B%2BUmkF5uZiJEkKc83F%2BM3a1adWb29WMDG3pE%2Fov%2BjQ%2BL8PtSmxhembFYZG7GTUgzZqi8u89gNu0zxr1JBmZHBX90QSnBs5MakJw%2F6D99BNVRnB6R11j84pB8A436QD6ZFTfwrRVtWJjHHsb8vijJrnsLmf7InU3aL87GymkU84oPbLJhuN9NXpcTjaIAexWNDSl7KEC2S0SwDHqEPx%2BA3AF94wdUU6h4lOY6F6oKvXQiHA5AOelz2Jvxh3XOyvnDdbeL1JknInEMPydkNRl108eH%2F894NBgcW4DqTuRLqs83iS7LnrJJKxFMgyA5%2FG0t%2BNT26HYOiqgComHYigwxJeCJKckCBMY%2Bjts%2Ba41nnPwXYz9DJJuZKtZmBQVbalm68X2XifWrYSzuSNtVbfEIDYn4ngTTP2c%2FQVtlclla61r8ZcmS%2FWqg%2B0jap3qMW%2F%2B1ZStJ8tg5Z%2BCQlvCrKdqiIHZ9j1oltddZMaxh8CMW%2F8b%2FlWq889ahkt3nCh3ws5dwHfgc2y4JOlz22rAKLvPZhM1%2FDEJkVv6GoxXu1tEfkrgwFbmRg7wHl2M5DNjVHJJH8X68VjyelcXZEYJTUbOC10tQ7mP04D6Pgh2YXDOYM1mOvMAcwjrLZ0wY6pgFfOI9uxWHjekG9E3KCgCweDjMoNiUfBIiCxTOcIbCzB5pCCcKpaeS37hH8ewpEGbiuxqgvfY9G%2FTHXr5bt2JEnWYUuU49bZKGQ%2BXIcfewrx6sz%2B%2Bh%2FGTgoSE8XS7HzTsXSbbwO8ZvENH%2F9T69ze7Fg0R0HryOQt6JLICSv3FWp5%2FakJ9x4yYR6ENbzhcCw94UjPuuY5PUXIeNsblO%2BCukLxfWGbFYP&X-Amz-Signature=db1e5a462afca6a5ae33f7219eeedac57d83c05b0f374cd3d4e4953ad5cf1ea1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
