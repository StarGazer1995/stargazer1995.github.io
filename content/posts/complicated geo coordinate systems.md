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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YE6HBIG%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T141239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJHMEUCIQCQ444paWIZSzZiCmD7hvYDDdXhRg81t9qk1gTJTh5BEwIgeVgnjuy0%2Fr4Syv1C%2B8PqTeZY6KZ5G9eFRPYQxQKI8DQq%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDM3OhwDoJFSMdrmlGCrcA1hV3ncQKFPZkC1Yu2MYgFkE%2F4XdDdiQcRXSsZS0VNLpBVAvXtRr%2BKPPIDNwY3eJGlC6W56mKGPa0dHWjbx6YMWNAve0Vol0qMxY%2FWnvbuiDV10e%2FJL57dKif0EP68Bnmi%2Bjw7OWBkrGJLql5Q6shhjLpQtT0ac%2BJpdW4L1YNdqhzM7L45NueUtx1t1ih0a%2BiMa5HOLA7%2BVOM7Tt3vfwQuGwYXyuPdH%2BM9MzV7p5yK9sMzH5jbyRjV0oftnqV%2FMJNybUUzXws4yovocYIU2D7LZDAYQ7%2F5id46nbZznKal3rCUnPpR4GzHZVVT%2FqIWQ7WMz4MxDezgyJ0pN0ehAjIcNnVgN%2F7LupupQIuEKKAObQ0shqjCQQpstsiYbvjcH2aXp2mCzJYAV9vurZU6FTOElXo%2Fy90UlQaqSJYdzYjv6as9hEuqedXVF0wabiIyu6KWFnbubcpn7XuYHvmn7KGl3Luz8ODPm3431SSJCcUOiJxpM1S9071N%2FzeQPbk%2FxIBCBhHfdjOkxgeqgx75M4t9%2BAeb2BwvYhwdTsaRYrUK4iQ7Tcl9hRD7c2833YWKLGLx5CaoGmFWpTE7K2I%2BleVpJHRUZAr9mWRuUi58QoUYKRmilGZKH90l%2FVXqcMMMekhtQGOqUBVZMeMrs3Hj1CInbkPCuo3HRkuST%2BfMzr%2F7p27WYeYJJYt5bX1tuUxXz6jsS7EVFDUIF4nDYKIWY%2BiBCc%2BdL8nbhOBif7mcicZUCONB%2BeDdzpt3nySJ%2Bu3tiYduJqp879ggwtn%2FMa%2BI%2Ftl5VkbX%2BtAfVGAiA%2BG2muxg5TIUsJCgy2ld1kfO7sT2tAchevG72s%2BskYoHTNpbGnIbpz0r5UfgawmDxf&X-Amz-Signature=3d11b3e23970f33c584ece8382e7dd83b709d8f39d41a6f1a40e9b5966ca56cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
