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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7UBQ6U6%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T141719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJGMEQCIDnpT2%2BQY%2FPswQzsclo2XUbZwUNdC%2B5FkF50ZH%2FVSK26AiB%2Bdn6PCdH0GWuVP2hmbTytJercbk5oCaG6FUtqX0iiFir%2FAwhFEAAaDDYzNzQyMzE4MzgwNSIMxhP93HvdWGJXBDswKtwDBbLPsxnYPgYZhgO%2BPhAJMKQjCCPC3BO%2Fx69kWWLKI%2Fd8DlMD%2FzQqvCuoHdAXGp3%2Bb48QcLgK3GWeRCv2DbE%2FqS%2F3swDXK0m2edD1gty7kZyOH0cY7zW74tj9qytbUUsn0oZsSdOP8bxjHYOYYwICip3A21QXzEKZPLHlszsF1B4yRz%2BHENTDOKl5DgPvqvR%2BXJJ5khHuEG4GqUZUPyqKLaZKMiLalm2fl3igpx02%2FH9AmrzU2w6mmsnfXlqZXTLDqnZ%2FDbDJk8HxiAHdp%2FlRC72eSB27PbjXrNyaappsi%2BSx5m0meHtUgtVkRrcoHDRwyUfX8PcolAv3ImXzhB5d72bMNh28IyzW28KqOAMsf2myhBv8eAfaMxDqG3SWScZ%2FasiYB5q7vqnCxRDhVn0ODyKt2Cs8tjm8PhHvqfm3bIkP1SYdkkfnK01nVYK2d7h3eVOkgP2XOGLlo2ioZu57TYvlzYWMx9cLUL2zAaDIMNbamAacgZopwYo4wCSSPBl%2BXHMtQ8UFjP8NEJft6l16p75q2rs9lSPEDzzEIrSuVizlQwZJ%2FMB3%2FZReUfH2Ot083zrVOKGgYhOM%2FEg3XOvolh8awGet7xv8mRJcKHVkTHglLR%2ByYPg6TPjpYQAwlfSL1AY6pgH4Yum9OrxZTtBv32zX5RZDe1PMlXzB0EUW1%2FuIT1eXHthvIRG7emYNPptm8EUc7A%2BzwUOXnEZGPDtLdsVBRiEa%2BSEt9BRoMM0QqQh2iWrRPApFmc6ZBmtPumtnNqzI679mQEqB9tw7aA9zW%2BqgGBaxhXVtP9HsheVLbsorO1fUssfCyzFM4SAi86T70S7%2FRHUrA9D9QYtElbbz4ZtrIrLnOhYmHopB&X-Amz-Signature=8b1647ca5beb0645bb2f051c06a16750f79e9b0c6e6ab2828c655c8b7bb22ff4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
