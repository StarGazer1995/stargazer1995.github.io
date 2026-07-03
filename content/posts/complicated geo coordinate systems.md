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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZSRHH75E%2F20260703%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260703T014629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIAUuOBixGfs45q%2Bqws6WJvFBIXG4iDGFf20EB57f8nj8AiEA0Lo1OkCEzkc2aigtd7Ma6TBkME2nfHo4D8v2W5vfGdoq%2FwMIABAAGgw2Mzc0MjMxODM4MDUiDEuV0o4XBlQVzw1k7ircA7uxiJpN%2Fbb8zKF7FoceGFDwWhGBlxn2f26BsV%2BQvDd1IRON5%2F0WY8VmmQNIMU6m48wp8p9pmqH%2FgBLx88Mdcy0CQkAqJC3lKdzNIy01SvZaa7TygRvWnHzoKNt1ThFqSS0NckXvMnYaUhVOSHYqj08Xow5zHXOKeS6GFESCV9ik4NEIcfK5loUb7zL5G7XChJTSiXzvs%2BT9pP7q5ksQAMzWXQ%2B0y5P98HlvR2iTQRG5O7TT1M89LMMbd6H9BnKhs8GBiUe%2FNaIxVpRJjMiVTjtVrGmZKNlTPQgvYdBGrOw8PQwLUEzV8a5xUXrOENuK7r6gukWEnuQ2wOBkGUcmvzkAaO5FQYL5kL5K9g47rt%2FBmVhpiIcZ7OpVta2g6vzkKXehQ8eZVlAkm2EYodKfGahpluqu4chCQmuKtau8gR%2FB6T8LNee485TzXeQGYHSye4vjyLX86iCr5LYTKTakQozIvX4Wl5LavnMoZjCBubdUscsBT4JddX5qGYx1guSUo2ZEM0N9O30gu8UKz7Hr9wzRFSGTqAQJvwIhwzvmPstamS98tu77D1TZySGDg3uLXBQF8ELkAkNugmOQSkF7RH4VbLq9U5P3tgjytpr80r7bt%2F6GfVq4oHPdgNLlMInSm9IGOqUB1qwY1LnZNQ2sXy1N2F8KnAl3D6ONarAL7cVmfOMRkerp0wZGX4fKrx4kQP3MuW1pTx9NfJNc0I2w551hr8EWXDnfIy6LRN6qHgImnl7WjzHmo2wgShBORxlz9JbtyvqqR12OimFys%2Bb9T4UrtXoq1BmjHHqK3di8FVa8pYLvXY0LL2Zi2cxd%2FQQCCnhQHLq3lIJV6U0MD6LjoJt0vuvQ3gNlCDGR&X-Amz-Signature=42016192c4ebf421f02b4f5f131efe7a41ffec0494be7a821d9962737a40899c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
