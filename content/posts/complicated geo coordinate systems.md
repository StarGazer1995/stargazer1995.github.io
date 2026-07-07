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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOSHC6EJ%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T225048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4EZsfqSaJ947YVxDKZroJDaQ889M8Iar8rnlmHXHW5wIgIaXpmTAvda9TduBA1byn0eBXR81S7cw%2F5lR9u8cmUjoq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBaWsG1Nwq5GutdMoCrcA7rQj6qsoR2G0MbzYgNiwGPsipmbCBEUVr%2BZljjVZJyrFXwCiN9%2BFY3k4WC%2F3NZzpAmCzgiwK%2BZVvMfo8220ygq7SuwN0AnvQyy8lTwsyUYv%2BPgDoQ2UDcYKkQqJGmchdBEuQ8VuJjG242%2FJLO%2FBb5k9LwLCGrHzyc2Ezty6qM1719ooRPcZC0wIkFCDCRgCQCi7%2F0rYtydA6lEfL4SZk8vqXuAO8hAO5pte0%2BhJdfcb4qo6hcLE55cJNVbiZXqgjZpBY512Cq%2F%2F42c%2FYa%2FfIFhySx%2F7Os3tllmxVOwHOsTwrt5h%2FQNCjt8yUuDMG1pUsWd17kko%2F4szIWuYCILcoGeDsU3MrxxLzrFFjRtT6%2F%2FdXWi7nHNAI2GV3YYKDiSjyIc5CJNUC3U7YGza5DVm5FvzdKbI5zEVNgZ6XGAcWlimWFZH0EV5g74it9lfvZHoj5rdl3R%2FMQVZhLnMmaCIhuveECm8x1uEmvl46cZ930vtaIZ1egv%2BIY7svVBoQxnOVXOqtv%2FZIuOPsG7EvaMvoEX4z3SKswG5wSs%2BYHrzi%2FNT%2F6Uo21ioSsBesbTfYvtxNZixXOoW4WDbWX5zklssaqUd4640%2FsNpnia3qsboKChy8rro4TmjhWRpMNOnMNfOtdIGOqUBJm3VuxSM%2Bo0OH%2FZ0B9rZO7d5jANsNLcyFza9Mcvux4GUcd5p%2B7UkTf73CPhww1r2QwiZ9IGyhMhB8qK1DHop2OEf%2BsFOZ7FGjA5gmeMcqbAPV7x7dauJYok1fwXYx4g5iWRPa0QZyNgTPA0v8lUOuAe899Uro3I7%2FWxJ20HhjFHXhtZISJqZfb%2FSOIxkyTMf8UfSfOJE10wFs28FHkZQkpAxvkDS&X-Amz-Signature=7d9bfe3804adcf336c20da172a54deaf0e4a32893e82540d8e22052a73e31b1d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
