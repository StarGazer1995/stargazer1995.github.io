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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOV6Z376%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T105833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIAhN7fevnk6qVhd8sURzW0r92HOdSUGQKA%2B%2Fe9uVAeyrAiEA4vMSJUkQV%2FsO4Uvojwr7qMN1DUDVGIaXmDuDgq%2BAcxsq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDGhkw1uI0tC6%2BcIA%2BircA0l2nYxXMCc3GdhzEI%2FeAjgKy239OlHgi3rEtRnFxwup5RZd6OFPaHVktx2uM%2F1fP%2FSkWALpjHydsE%2FyIclRm3Cqc2He3gyrEv%2FbTnKpMOW6%2B5sZBjEdOhV%2F44FhmY8R1UwEipK4MatfSZ5hBFIK6b8n1qepJ5giZP1N4YuwmoqTcxMJZpnItJcpnCN2JN85G09D%2B8ph77pEnUD1%2FW8YKfiGUNNakcWdSevg%2BtZVFL2jFkJ994GLu%2Fc%2BxLTaDhnhYnGn0X1ktiu4G7QF%2FcTKYX42q5n81PHIIeas6KCm9GNbth63%2F07vkdvvS2tidPHz8V7djpD5S1nyCZ9wo7tEj9Q0xiUdpksHxfJa%2BbEObZ2%2BmqcVfstvIJVq4KSNYc1u%2FbuM%2BBP0NZo0FjvKi0QWi2vc%2FaMn3sUl9rCtCl69WKHo%2FGNST97SsUC3rehfVp%2BUeASYJajA%2FBVoVML9w%2Bss7U15IwHDq6vCkAR%2FsrwZgtnOK%2FwqVTXA5Rdkes9CKd5xd7AW1RYPPjy%2BEsRPpBCy2xBaZFnMd0lXJ4adfu0ehvxGhpikR4nPwGKk2qAuRoFkoQV3a7JQHUz8jhun%2Ft7oJYuLperMupHYi%2BUGzbmj759KH311D1%2B7F4HKBXQ9MLKtu9AGOqUBim3SaV%2FCfmQehLfEF91oQfxrHUpK%2B5K6pDzJYCMSQmTyIw%2Bh20yjvAjA3ZK6oYbdmilRiFe8x0xaGTCb0i6fNz5RgAAU1cQBrp3GJO%2FUqsVW5fRdafCi1aFP3sX%2FXJFv0MihZ%2Fip4YqcY%2FA6jzx1IXZs%2BV3vdkixRQXMqUvoys2gR0Bvwl11K2fbBYpIgs1cbc%2BTu8WNQVgsFOivoSvY%2Fx0NdUJr&X-Amz-Signature=952f753aab129f0d2248287c726b14a97b6e74839b66015ac6133af1140053a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
