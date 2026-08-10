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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR6WCNC6%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T034304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEaqm2QcN5NLLnRuYI%2FKLcSaftkM%2FbMuh4Nzzu%2FWs54MAiAHcMtQ5wXjLZyn7QMpTzMBfiQHPTh1dtfgvRjXWJJShCqIBAiT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvMBlIJnPFAGMM46cKtwDQltB6WAT4iJS%2BS2nRyKKL5KVYoBdp7dEGRlITr%2Bol8GI%2BfHAJ%2BiHfbjAKgUJJDCZwRZ7UgVn2rtXnjP7wb7kCTlp2znLndpoV6XpK0OKgLPeGPXtrsR84s6ddCLlFPrWjYBSWoYB5My0PwHSWKhHf2FlxDug%2BXxK12b09qbcxIYMzeL%2B0VxATtHwsuh%2FITm2vhvRVYBHXwpENipCife05WFrC0jsEhFAnJEIvpBbslFv%2B2XCY9iNYDWEx20XvNiMrhcJyB8outZ9Hicsb3VLgoU9CCYT8xeu8fa0jvRglW4fwYpGJunFk5VH62KNHskKP1CqKabTkWSuHqVclkOPnuLBprk4Yqbh6zf0nDIOegtiApuww89vu7DE9ZoibhQ1zad97G0AIADrGNzCiYPaPuWlL27WK8xql%2FMlJB7qM8Zx5BAJYbgrX%2F2OJezLoQ%2FkKpDUu96HHRXRfIdeCgpAbe1pRkngLhBkvsekRncTpiSd%2BTU%2BmSw2q8%2FResqChqGHYZpsfKzuu7%2FJgDriTExM799AODJ4I9TbP98UWAAX%2FexSwBLpe0kxiGoblFAu%2BXpudKzPr5apuXSgMGiI34XmGhaWQGqBqmCtTWwpzuvOFTkaFpY0dZEiR1F3maUwweLk0wY6pgFF2FPfsBlRntS7ikWVkVVYCFI0%2BSPA4%2FrDcCULtT5G0xTSdfyoZzRCxWZtGS9qUzh3WvoXQrIi9addTkEN%2Bvco0oZ9UysLnEj2PJXfbYgmECBxbiZDnMSz7J08EciKkEnP6RlYtDnb%2BqM7l3ziUrdjEVTArPiT%2FoMJG%2BlGyss6wsmNX6IMrvGSx9Ovv97kdcI%2B8v4%2B0UWFH7OTInT3KfKmArjaUX5B&X-Amz-Signature=ff90a6cb2607bf8119e8eb95ec708b9c6cf070830d92621958a7323e2350e917&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
