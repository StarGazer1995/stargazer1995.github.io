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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y4QXOGHQ%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T223738Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQDHfxvjbJUPzuTG7EV4Ojziyvbdfx%2FbQJlBJUeqQsREfwIhAJOmEyOGMiluWJn94bjeDJWI%2FCrZunY93B16%2BPwEAWNBKogECO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyMgvQdssrpJw8oCPQq3APdTTkrpmXdsNLdS%2BkYfuDJOaGn9%2Bn8G9%2B3Bl0OK%2F7u5TffCrOigPtAuel552tsZNHFwYig7o1b9RDjLPUMn3%2F9GIif1x0Ek2DpEqG9EqweZOWufDQhrovsa%2Fr9J0YQ9swMlnIpK%2F5%2FO5NkNuvyEaBau0cDIyH9FtYLaX8U6Hv9832MrB2w5njpjMjT81unVG5zKgJ2NgdwpYffLDaEYEDQAuxr2HxZpGS4ALhOJHfHM04UG7BhjnFfyOw%2BcI7XfdvcfPhWUpwEwahj6eTABrqeamFeSTzCHQfMltdz5BnhDOvN%2FYMfel7tYnRFYOz2CR%2BOjuNI2gJfcdv9eg3C2nYRUoBNHwstrZWsfurbQa%2FLmqYcZkab4MxYKvbKMN433UyX5MgyXJkN9ljNcaAZMscEmxlwsRzuYsRpofncAtH5lObGmfqZzax%2Bjo%2Bvvub7BlQxUxh4PH4zJZHu86iMiMJOtHJseXU%2BEwiKACOPCeHnsgzIMa9fNpKWaPIMUDA35Cb9mDH%2FyYo38mwDMX0nRPMluKNHR0bbCpwz%2FS0lHxKG8IP064fe4M5hw%2BWcN4mHodjJRRe5bijCRsLmpsEDkv4NwptA5hwYYSh9TxxOh9j%2BozsN5zAy9PvYQkahAjDy9M%2FSBjqkAUqVUs116Mcml9A0oXpE9N431ybYzNHfD1pGaMaj85J1pD%2BYhNJ97f46U4NWAnWOawidn1bRn50vXRz4wj4a2O%2BJnNDTs6ByACCU%2BqVLlfetSyeOppMtdcVQlIaIk4Tu7A8RdIqeMriGDJgBp4W2KCK438wcLKaftp4tOwnCCmeHZhOA1qo%2BWjbAbeGxtPMATm56GxTqH63ux40nPGqpiSBI4aOE&X-Amz-Signature=2e8f7348ec6f1c52f0e2a1a31be32c2112950c6f0e08f7914df7dbd88ceaf1b2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
