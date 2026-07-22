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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEPXB4UV%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T080602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIFaBCBS53MRQZfYk12oBo0UVxf3yBYt4jp75ZpKJNUomAiEA%2BXjQjqkhjVmzm9yu8K5nKsAGGMxAlUg3GL%2FT8pXLyewqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOjxzzQZ%2Buqn%2F5eIVyrcA96PfRuJf02X0Y83SADTBjZ66c6DWfEEPvR6n4p6Z8esUw8Nja4I9UUTUH%2B665j6JtStERS5h4GquQI7XzGt9tWNGbCHE8sNA19Al2ecPSexlF4kbivBJ3jls%2FwtIX4TlU61hx%2BwdRjx%2FKZdhNZq3teavhXDgb69xjfvdxAnI6QCTJ71APdLboB5N3Pf0u4RhfC2vSzWslgHzBt81IIB13mFoNo0d8vjVJaOI0EGqcqkYqemXqmhh%2FRXAZwAuALlJWXdfEZqYATObO7WPn5iDI%2BoB0TTbddQbKBCvtFKnJqzdifuplhT%2Fw%2FWZB3Ubswhph%2B6yd1Y85C0YVbfZiw7Fh0DC5McNYuhyewnZSvtqVpMX4C5N68cfeXjRJtcmiYBsdHQMRcsGReKGv3MEKdcrXrg41G5cv4IcZGZLTOsEgzxOztx%2Fwqkhh6pcf99kxOquTaVSekb94XBXHukFlbOjiDt%2Bv8k7uYRnjgjRrwAgfgGmbd5CEsd9fSamX%2FbxDgIPldOHNB%2FExKLN0CSDU83N%2BKqo3OKsT4seu%2Bfn3B5OTFCOf89OB72Om06j%2BNU3b8sRTX7Y2ue1KGzaEVupMSbY%2FWhB6WGOSVeoV0iePHAzuRoPrHNcDX7IkzGdSsgMNTXgdMGOqUBpPiN5S%2F0gl8FxMpCybgxaobHMV5F0LB5nqTWyivwIHtGYgUn%2F8iJWGUxgnG%2B%2Bv5llUsU2YBcZWhp102lVkTCFFsnYv5AXbIGjRrD%2FclhJ%2BfD8zHvbhVbve18BicmvujBBJdBDqfrVr4ae0tGbmY4Kc0NDUhaBOvmjd8GAkjL%2BokIksRbSoKMXv9tVnsFczGfftqyqSLGcAcDasbBJQx8NoJQ5PU0&X-Amz-Signature=c3690301382fb6e7f1c9f5e3017318ebf946bcd958edaf64c820407a8f4fbd74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
