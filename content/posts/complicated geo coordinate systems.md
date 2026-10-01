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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626CUGFPZ%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T203839Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDfo19YiDlVOlDQReHVwulWOExsYsIibY3xmfJqbqj9ywIgK3nTsTdZIFayNYWJPDelg%2BsnQDTw2WpYppN%2B9S9SCFAqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPW60b5j4nzoZ6tJfyrcA9QPT%2FPiaonaDNnAJFK1f2NXOWRjcmBac7QI9YFXgPrjDzUn%2BpzfcBrHn5yZBExM%2FfBYHjNZBYaMWXN10AaJGJdngggwuJty%2Bn9d2zX1LOf1aN%2F4S1Su796ov1QsbxuPiezE4v1IbZ5Lp8MrUg1LxtVqYogYamSG5sFHvBXZRAjT1U24OG5KewW1vI7wR9PRrVjxnw0FrIRCg%2FKEda%2FCCiwUwnj5N3qrnZt3dbt8lsPJ2wW0fKeJI%2BizTa%2FqcNLPpcHAZOgZbKbWoaa5tUkS%2B%2FBID94iFbnAXzTrwqdyNWltsSUchljU4a%2F%2Bp7ISTG9eXMFTdXmYyRC1imrO2PiFxMiOn0jHBoA4VnsCHOGxB8A2TtOqc3%2BHTzClGMCLx4kZJ8t0JHbs8L5mTDy2hS6K8iKGKp84OMbYfwkjR3GhGew%2BNGjLuuWOxOjXEm8%2BBfebfqnpulQbkmh%2FM0WOa5GFRjUK2xV0lWach84snTjW%2BiBQtQdAlO2y7BunEgNSl3EoMgPt7VZu6jTot0P97fK%2B6MRKi7%2B0HbnEa4aWA1pEXoE0Oo%2F8%2B06vadYyR9jRWEPJAg0GsXGlXXTucvo2slZWuy54vm54vSQvR7e5qr3KSlvYEoXdEee8do%2BsXrIVMOXC%2BtUGOqUBBYQRhnUE5LAvahObGN8FPbgidjSAquyqQWf60m6OeMRvo28LsvXOlcLi0y8AsRJQ2iHnn%2F5rdx%2FuiiXK2r9vsWoDKmROB1fCELrCBPDMTUrnEuap6z7%2BKGlJgIUGP1PBh2yVsgl9ZDgEnmvWH5XDHxMl92Kux%2BvHz1Ptn1ce4h19imIGiCdnHCaUq0RrFqJVa6Myx5xs4QkKS4cQEczu5VoedSgo&X-Amz-Signature=0311ccc415e76eada8d6dd82b824dd5d7e58ec8fe8d92ae689e45d00403d6d1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
