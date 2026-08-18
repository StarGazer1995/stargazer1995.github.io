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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624OIK56W%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T142307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2v1V5mRsaY3f9DPfh1vWwtcyatRb4bGgc%2FqAL71AmDwIhAL1ScRtNdNIBLAHjXKtDqZPZOaAjGoq35rJRKXPl0PExKv8DCF4QABoMNjM3NDIzMTgzODA1IgzW6VMTJ5sOOmgg0icq3ANBT0Yu5BLYgh1HNCkj891vqcfgHyWxHnruu2g%2FlKhy7ccCf53RZb3pDlhmWgjqnwOYQeQgSvl3t3Bnb4nEPvyv6HXFbCB%2FyTUL3j%2FnpnadmGbAU%2FHSEmN8TuIqI%2BEB46S3XGxRRqe%2BKSnLtr7ZTdG6WhQrJSIfDOroA3qaN5gpUzCKVJ4FnlL6VLiOZMVpBAIqX%2FVbaA8Q1wo6qsm9DQT3M%2FBeQh%2F%2B28XKIhlq63Uvy2HMb1i7pl8n6hzT9d7xjONJ8RSpwXfd%2B0WiikGT68TdzH8VmQSLUDsoIGLLb1%2Ba1vwSvMskLoMpSe8qIO3JI37MYodx%2FPHSsJqjFPyDla%2BBWy%2BUpTp4k%2BeOD7QzdudsuJnfKXIH18Fu3ZCbHJLcVIpiVhLPiwyXiQEGqVR6HMyBs8z6RmO2aV69Mi%2BD6ZJjNrOsUq%2BcQlA53gea%2FBZv90HSbTVoHg0xLNOZAhDPjCI6xhrbISCPzaYgKFwZDpwunjsytTQ2fU3LXHaq%2BOcowY41kNucn8zLBoykMAURD3%2BzMj7VPyPs55PqWsY1iw9xphLjAVI1erYP6FSNtwaYq5dHhqW6nytHwReYZMP9NRnVvxfY0jH9JjJVDeBzAqyNk9WYLKz4LJ%2F3kcJc8jDOt5HUBjqkAeaDsFlfy%2B58locfAPVTG2xRvogsrtlPujzPIJjUfJu460V2gVbmNd1wYJPXOKzcHLzRdxlILGrnXAISS7fbIIOwE0o2XbWWP2M5tNt6y2Wr26FO8mlEL8i2Czs2UjSiG8YdJE7F0fJBMG23WtvKKbXZ58ASxHmf0ca0BbX485%2BNAwEA%2B7svxrIohkVihEodnymYzbeDsapY5G00uvLFz1xStbow&X-Amz-Signature=df23bdeca34fe4812f38081975e505fcf17f56714a6a21d34a99a89d9e0737e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
