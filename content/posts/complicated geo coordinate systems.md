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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XP3FIIGR%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T095913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIHY3rzSFjTslmapA29Ct%2FliCTPlEtx6LhW8%2BLv%2F9OIuCAiEAt8ctzecBUx6QwNgOGDUfltWIJnNTK0oUHK346FPj4tsqiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEJXjxoQaqVsDnB39SrcAwXINgeoGnWDV%2F5RXyB13UGUhinhoxHFdaQ%2BOsKl0u%2Bd184zugCfeVNXpJPcZgBP1Ih48fuMy1okOjVMyWPRePMWUmo7FHh9T1dlgFwaVG0Fpr9o96G76ervZzsLaaoLdWYaYzJlt7KvKswQu%2FVyNmnCtQmcHLHmgEq%2FRTajMdZQc7a8M1g1OoGZ3iMZ3ge4abrP8Jc8icfLRbmubVV2Rf9V7o67jfA%2BRqpJomnssiRZWTL70KYqeHGyH50zqMJoSp4NWpC%2BLnzmSPdPSyv2Pfx6N8%2FS5EUkDBhnyjjw6Tlm7sSVsWBgJXdWGQ3yAXcwqJVb4oMiO8k77J%2FJx7zDT%2F8Xm7OBedEAD4cBK%2FjMeQcMIUYwmik6LuTF7D9Kqy5sGeA%2BTrEMu%2BZk3xjAVbRatfzf3oEXyI06Njhyp6Wzbe9UwRdBjC3P9klast%2Fosr3ePX2%2Bpnf%2FbfrJxm80OXAWm3Bl1IIpiCcLtGrEPRsztmVpt9FzUdoJFDbsMYR57nIouwnzFsh2MH0ooJa0j%2Fvop5eKX983ZVGDNYxw7HAeAhSeUmzq041Rm3YC%2B7jm6gq9axA7VrJrVRck%2FJ868l2NCI2TC8PRfX2g0Qkv8vTmz%2F4NpX3wehE8iM577z%2FJMM3yu9MGOqUBUcbHsPrW42NR4mvi85%2BUSZAvMcTmpYL%2FOpJvRGLcIcFCDdYlgfg6PVoXSvVTC4M58qffp7ZNh3jbYRmuK2PNEFgzWfiskx%2FSxld3IBgE4swC%2B0%2Fm4SSxJXIbHRYZilQhHYyHQx7C3Evbh3H1ebOX%2F36apj%2Fs2fAeUgTZPi1thexZ%2Fxn8Llxe0eaJVttuFcs6sBF573%2Few8OUP8mnsYnGOvlRUiIG&X-Amz-Signature=25e0e38472e90912946eae351848c6323857db3c6039175ed63398383ad4d222&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
