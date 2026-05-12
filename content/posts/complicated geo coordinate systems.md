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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XYTIURA%2F20260512%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260512T192733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIF5KBNolPdKdUHeXrr3wc4avLdae%2BG%2BhDtFh%2ByKDzzlIAiBt%2FRpuw%2BpMs95oAv5x4TC2h7zTvdAgOkaOsHhSCxFFtir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMjysbYu9kPfpIBqHSKtwDphkkIifRPOfTNQeMWlxm6PHcowBAhiY73AfjnOwlvQKimVjK0shJY4FDePo%2B4%2FdWokBj7roMC6f0rNOQE97ZtkicRFunQJq6BfKyYnhRivFI44DzOCAG7e7ac6qDdKNRGcQxO5MJUN1oREMNKyGz38npyWvRQW4We%2Bn2hu9fKDiYbkVcI4Yzte75%2FOW980k0Zfai%2BJz99Kg%2Brsd0mvzJ4uVljNNhPcWVcSQviwOEmUNtIEQ%2FbwM9qYBKbCqvNXqXeE3o3IRagB%2BcxcZgNLMXy3CZtHZK35ohALea70X0ylv1MQIGUqOaa9ODZGCf0Qum4K85kFuoLCLyH7wFY8r6H9b5mC4i%2BBB5bQmgUOdh7%2FNb3Xhp1YgQkiDtjlz%2Bs9UhSC7utz9iMO44jgmPX7xaIYVKzg1cmcM3YsWx%2F%2F9cdkrAxNelSVKM77YW%2FN9XaVhHWNTbyAtXZXMYmZOUvuL0GttwI9NQVPo%2FD6BxMbcF%2FNR1OZM2BL9sWc7FAd6FAaiYgtJ0rWQznCA5bxjyvsPswOL9HD24834gYvxT4X1rboP1y9YRLtTayRUhsJC%2F0rw2KBN%2BmHL1gZTrWSgvZatvZokzeeEdy6%2FK6J%2B7gb5J6OyQitxSD81GccIftP4w7%2B6N0AY6pgF7NwPpbgZLJYGpS47xrxSl5Jbg2MDUg9aQnU8qcoV1osHkigUAKE43buw8XF%2Bif4EuWy4PXc3j48Ca%2F1EUlJ1EahJsbzHR3otfedsaHp7nzCZekdWJiB3sNv7wfN1OOFon3zOYlGQQ2p4zDDrSdSRqUTANxVs6R%2BsYoe32E5DRodKGgElGEMq8N8Q%2FsrWMO8AXvYno6SKz2bZ%2B%2FE6rR32twSQXD3J5&X-Amz-Signature=3d6a44743b6f5bfc1fa356d3650d872ec6a2d60f8f7c3fab6aceccc9caca538a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
