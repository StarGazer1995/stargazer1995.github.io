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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H5KBUFE%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T215747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJIMEYCIQCIB9DS9%2BPNHO0oe0o9pngAX02SBn6gsC5HmtxsBTLXywIhAO68N%2FDwAZstibj3trbUo%2FZneI6liTktjLnPaoH3fKRWKv8DCEYQABoMNjM3NDIzMTgzODA1Igy7i5XxES3DtCyhZdAq3AOqyyBG1ek6QZW22%2BnzIL7HBclcxpv%2BVo241AZDCzUMmViG8EUjEQoP1B4glE4gECX%2BT89X8Kk1NV0U%2ByLis8pFgLmtOlEl3%2B0n86ffJiWqjEuXP%2FKQ4aiDc15OCySzSWMN1WzrIQZtyrfzUSKTq36rZ3zYp%2BnYIc%2FPfomtD%2FroFIugFYBqcgXMrCqlTBqHMIQjYGjVUwOr68Fweu7Wc1n2h9otfYYDTTpGUu60GINMUT6BTSIBcauqUTRNPwu4aQLSWe1c7eV8%2B08jC6EoLJy0pxsFY3FAPTC54iNcd7g9ohsVQEr%2BhB9RTbGWwwAsVDn2ntUxc9PPxa2XWgjtdKSiwjlv%2FFU3IchoSAfDJvQp%2BCk5XW2YdVqlDKfaAYkTcW0ZA%2F3%2By%2B3Rhgbg3EheavmM34hndOrR7NgZOcy263jMpx%2Bjrnxmdjg7eXzxaaE8l5pAdOr%2BXTA4WPblHDRP0TS8D8NKeGfWAE5Y9XwyiSYj%2FpRKtbBoFdvNH0YlnrkDqP2oOyx0rprgJt8iMzfLkByKbrYoXmODLkZvO7BTGsTI5Aisi1KafIDn5%2BYq1zKElHsJN49vBZUZHCnl5vr8Z4K%2BpHRarzdhzppvQt0epWkZ2rB1dCA%2FcIoaQ2SmHDDLqaXWBjqkAVF2uLIsmIoPE%2BV4DJGMCwasGnfqRBpLCP42nNKv1d5SnW5iAIHQgiU%2FcAsw4qbk%2FxXyi9Ifgb7tjRatfaRixjMsCCWp28%2BldSyhxx4bilw65QbZfk%2FlPJrHd8yF66y%2FWiT5Qy7%2BR1hY9Lkg88iRgdBYaWBrGZfTDlhs%2FqtvY1YYG%2FF3O1qRCuB0WKFC89Talud6ITZl0KjVIDzC6p3hNqvUalQx&X-Amz-Signature=5f2c53f69a4ad4719bf3f3d6710369e96fa3de556e76964a5cdf24208c6a5e18&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
