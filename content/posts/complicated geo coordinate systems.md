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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664QPYBULX%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T223436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCsmBK9PfqYu3Iwx1OTRI6J%2Fs0MTHHGPqq2OxKKA4K4hQIgBlgCuTfZ%2BMGi42Qua5rATsuEp7XuPDxqVuNZYvuC0pkq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDCOQMAxWZvNttPUl1ircA110XWIyukzNXSxJ6wN6SuSQibubmL7X%2B8uxDC13r2e6aUGuuck7TyBXZD8dVJoJ95JtwagigbvQBZaDHzwcl4t7mJBnZou71kFdBuntxh8e%2BaU%2B%2BTEOXjdRZ4CR%2Fzegiz%2F8FcjY%2Fmr3QbtAT4ptEQrTThVooQQhsXhw1T2zW3Y3IhASUErqhE8Lx6nfMN4J0CRls3aa84tiyyvq7VMElduyDJOqXwr%2FAKmHbQgzqOlJeD4fRxRUfRiF4BM5wKebwZAoxUzftxRoF15a6nMURRWZQa2SCLc7%2FR%2F49RUHCVNvnS29ny7YmAtx9oHerO9jDo27HtjNtjHso0QASkZd09XpsHBu%2B73RvCiZn8kvqVoJJmvVVpMyDUIfj7iswu85g6s0FxWJVl2p7KnObunpRkvrAJdcqRlZRPVJ2MglmG%2FSti96JSgX3oBvM4qg%2BlBFEzWV2CNHRlumLTcavGiio4%2FNkBnltdpuB2OiRPy0JQMQID9%2BbJh5Pb8krI6R27gf20R9JVpxZvXB%2Bl%2BhAUT7qndbT2OsdD5L0vhs8MEEVlWbukRNu4nvBUm0pUka8Th5KsRM%2BnSjE6rIwx7GVbrV3GAIAdtcBYHmGyRCCgIUlMcAKAAY0qzuqh2jSRp7MKWvvdQGOqUBfMqX7kZ8uPtnPfQZZlbrOlxsT5sscb%2BtLujdipltISkoXhIh%2FmA2Ruont3O2ydrAT514Zmfh0t1VpjmZ0wGaJo2NmJNXW3xJXh%2Ft89tsujSE4rWW28PUy%2BGfRrthtSrDj6%2FLRmecJFgcjASn1e9fR7DvDRx368lOAeCFH1srrBdvJI3Xq6qp6yqXHmUM1zmnz0ldC9oIpwK3HLTyE0tjU6tAFEQT&X-Amz-Signature=58282fc2cb9400352ffce9f4cd71caa42d1a841b99332e43c0928b30e62ee904&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
