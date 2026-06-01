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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MM3MEDF%2F20260601%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260601T091015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQDYCLB9gSuAJiTHAjUGso0XDP1gwNYnjVXHaYLKgGYN%2FQIgc0AJQeMYnMHKacvU2HfbrNlvcAPBBAfbhiF4RqVAAGcq%2FwMIBxAAGgw2Mzc0MjMxODM4MDUiDLwVH7g6AKUA5LkFqyrcA%2F2%2FPMojIEKMi5kxro261QyPcb5NIq%2BaqW2%2F7Op59OBN0Xr5zE3N5bf5lrtSVNjg5N8vMo4DzR1hkn72lsQFkP40y%2F%2BigVdFUCH5K3J2P%2BqHuQqV77fGIcGcNEK1%2BxCSJXNq%2FnBJDdjBXRKxh80FQhIaEZjgu6sHiiFoGUOCDopjP2KdajzE5Z4msU5K%2FolHpA4%2FTXQR%2Be4ja9cABio8MuWIAvamLvAYXCZcyc%2BrICu%2BStq%2FpzF3P7ZCl5poN9wteDGZ4mo4%2BSXWTb2qwyC0%2BN%2BmfPF%2Bg6kqvOcBBTSkfkoo86E3mueP2rCSKT%2FfjpVLzLK17nYKfC5HQ7HPW0BHwBQzEzBWtob0EwzTf3GSoBG45XKbeirPrqW8RIWzWR7zl2YrMgdMSAw%2B6EpvRY41vhJ%2BV8kD8QKl5P9J8KRWnbe5NRAla%2B%2FqXCeY6aBFKVsleM7engfvTo%2Fzz1l5SPq%2FCl%2F4XnB6C8Kw0P1L5uZ%2FlK%2Bag8ck9bKZ3IF%2FZkUP6h1BJn9ryVzEeIRSOOl4pACuqKEqapOjhrMSumD1fDkzbxFHt4myBMPFvI5iZXS7knDfeMA2dpmlEJtrC1CeVawmN08GamsWqKjlZxHiG3pLi8ZuJWre5R%2BTXdDolYNbMPjC9NAGOqUBecBU%2FEjp1RqEi%2BGWuRN1YZfxWOwPl6HOUoo0y7BNEVZJv6X05crhFrTzW1gxKTlU6B0Lw%2B%2FyaUX6VKegU9IXDrERkOgsihd63Kj1%2BkEGfiKbKDa165p72dvYlK7eUOJLNizjQ6S45Rvf%2BUoW0yDfqhbi9ydGkLiIjyCCd872NFpGpeqljcoCkrElMHf2upyStUfiENoo4GiO5UZSsmnUFZLAy7NK&X-Amz-Signature=ce38b66acd4bda8ea3eccb798311e62549a1f12eb203c0e54762c3ffe8072e62&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
