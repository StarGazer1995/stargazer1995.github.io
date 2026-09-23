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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3YVG3Q5%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T143101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID3UfZqjPZz3UwSpVzD2OF0vF4nevPSzKnq7vxkjG6qEAiEA5G6svHaUTaiQ1gIio3w12ivXphOAY4GDAocJqwLdZYEqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKUSQ9yO5ePdB1u0ircA62FoALZTrrfo2sbVQ4%2FHQH9HSXZRpMZGGg8%2FS3A9W%2F5huYwNuMNWFGS%2F0OkFQYezAafasJbrG9Iuqgm7%2BzPutBIB8BITA7IfwlLCtwMiG1FMdzSgqSb8ah97Xn0oCW6jN5ltgcBuO2XB6l29loiwP%2BgQXftHmcP6v9VkTyhChTwlLBXYs6Aa1D1YoF61mlazIioLhfWkXGf9A4%2BhQgvHwA5OjXrYFWAx3pjL4Ia6vqiIc6wEeSoRqXHSr3R143QUNm9OeqeZb3Az10467zGtXvYj8Xup83Isb8fNEfKii%2BFxD3Ub7aSLJUN0xcj8aCPGyYAagS6ExU6%2FRsjbbacVDb70FhC1bP0SclbWggGw9pdr5ZvfS0%2FW%2Fhc8lRNmOSaw53MpkAhlu9zwHNqNJejcKlF43H0kgS3cSt2vg8HJUiPO2pBCZQKxDg9ov0VOI%2Ba7xjv5Aeadn69hhNGNA0Nletob2%2F7fJW1gBfqNb92CxYBlco7paRc9yyqyt5WWd0mievbKr1sNlJlIO%2BT2Y3nuFIWYJ1af4oD3UKrBAtQreOk37AyEn5YmeF%2F5bNkYAaU8l43zYV40Rm3ouXJykkBhLNKdRHCXxORnlCcy1c5hyBLW4KUOTXe9bQjLwlTMOCFz9UGOqUBKQu1bzeEwYDE2rUELEVa7QutDOsrjrkm7%2FZTKEfuEiD8a%2F9teMTuuJdxW4WSu3OBmu91FOCwlc2x4v8s5QIPIS6Pl9JtJKl1513gR1NnGTpAEGbTzeCZT8inob4Gt3vrKZ6eXna8TznJzI8uLQeXnbzVFxgqZtqjblQzd08AlLJSqIcqexpkYQGJU%2Fi7rL%2BilSiP8ItWCPHMzpnBYbuZ5WPH53d2&X-Amz-Signature=7ca5bef68a3ee78888248ad396eacbae4c482fad4d103a4278abfe039041125f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
