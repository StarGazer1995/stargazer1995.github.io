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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SD6AMU4T%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T012334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDcIMMyCQKqA2Yw9RBErHAaq0T2q7zoRwdM3dKD44V9sAiA7kezZdsj6uYMrZ1KVHbbJgP6hf1giKR47GREM9gmEbCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMikjY66PhFRXHTYJ1KtwDdW3Tvw%2BKLxRVA67Xu1W5xm2ie4CNBg5yontbX04NPiWRU2wdfPi7N2xGvKhEosMepSm2VSzerFVOHUcsIWWbjyPA3pTlSdt9mbNs0K5swzh1T4cMKlhT7MVv4VFiWAX8SHWtsOeVInYcg%2B9xSl0eylgDwh6iD5cI%2B304UQ388WHQEx2VaVuz8nXWeh%2FCxcLwpmFHFpBHJ7sSyLWgpcaX6%2FKkBU1OL0CWb6%2FaS0iGNc49JQkqCx5XgVFUaSIuNEyFLVOH0Wd1vv5Dbr3zJPXXP%2BnVXLSbcOvtP7OcbEc8rPse4a3iSj%2B76%2BRjYH1NGrEJ4gnXkAwtBn%2FWSRGCllEUGYxZ%2Fj1i0z5JY7I4b5qSUdZBVQgNG%2FxwGwbf7P6aoe1el3qPXFbVROwNMbzu8aaz1Wrh6bRCw8W5ACVaNuL%2BMd0os7gfdPXebi%2FBd7Db810L10Fmza52TIArQkwxnB%2F0H4PywhdpmEdAG%2BxdOsUo%2BI8VG6jo3AfDjHt9N%2FQIGaOQqhU7e0odidaboIFc9bdgnWxRFtGHf3fhftsqWllSwVISi717rcZcLx4Josgm2GMYMBIhI1Xjw9QZSRii08%2BCOnymZ5IRUa3ianWyAoglHPXG6sgYseC55SyV%2FdQw5Knw0gY6pgH%2Fv1gc1BIsp0gD1z3XpJ1SbeC0Iu%2Fn5mNWMnaKqip8jyuWpM%2FTEnbeFh0P1dqmiBDJFalca4x0PQjjz1wrX9kzsvxZxUIIMmiWmqcS8ShQmsHt5WA08cZ%2Ft65UwyMLuSLdpjP6HrsN92XKVDbTskdz%2BFYoLYhdMjpzlSufnfNvlbbailL4Bv4%2BWQIt1ZS13F5s6ZSuqhAZei4mhknL7fU%2BAfXOO%2Bda&X-Amz-Signature=81fdefab43728da24cbdb9a74decbdf8d9c9fe003fe0ca0485ee5811e8518e12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
