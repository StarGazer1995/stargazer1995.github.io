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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJESJB5H%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T015315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICwIJulhlHiTrHE0ASUpbDCgd14nxXneu5XGu4COySSLAiEAt9EvTEXFPSEvL%2BziC%2B3seBBlyOE1HKRd6ip16pPN2OYq%2FwMIXhAAGgw2Mzc0MjMxODM4MDUiDBPCZ7tEYCM3sb3GxSrcAzO9jj9%2FBHZmKgCzzzTH7UgVoexh%2B4WyCfB5OvEE8NzjNioHYKhjSEoDhtWf9V8%2B26iMjmo2ziV9Mpro7ipw24zuxvZvFLHHn%2BD4Snf%2Fev6%2FtYcWvLamhQmdd%2FC1j%2B0tt%2FzAH0HhMIBQxT0z0BHnA9T3NFmWRZZs4jGikkxpZDaWGSBIV6KHOE7Hv6tOqBlfO1%2BQbN%2FFpF4%2F1V9xCJWrGsit97WcaPPqQ4Ee%2BYtHD0hfIFXqHT6OIrSaTRqKFB9gnnYqP7yTUmUpCr%2BzyxownzLgmYI7NBz7RFl9vXpCjbeex2GFUP0HVTEDyy1HsDTsX%2BRXqH5eSnnT9j8QDapVgvLunZYmmDYi3uDwKaZVBfDxfVMuujFgcItiujVqicGyf1WSsYGEz3587QtFdHaLneMCG8nKhwQqtty03c5xa98XCFdnVXxPR6ub%2FUQSuffVMcqJ39%2FBplAMZzAdjMjUTHyPPU1KwBnk%2Bw6wxK0FVmxQ4c10k3J39Yi334dpRsA6PL0Dy9GiGGKVvYQ2xcDM%2FP0jHDq%2FghK1NfqUBy5MXB3YaLU80mD69W2dwigx%2FtkgH51D7WR1Hio4qvj8%2BykM3JqSkSzr5qMiuYU%2BZqDmgw3M20CzZslfbVVLgi%2BOMKCvsNIGOqUBcfWQ8Ok1pPP1rN4MULCVtFuKWKUjf2y2d%2Bgm2n9hTYmmTUUOOJPVzVEkm0%2BDrArZiKe7oGdCuRtz5DMKUyl75RcOMGQmtorgzDoZo%2B83%2FooX9S2xxI77Hq8n9%2BidJ7FYyR0jM6kkn2xyJhO0OeRR97mulwoR%2FWBDtsQ5PayHEXuT0CCfec%2BYNc5eMmm8D8Iz004luEyB7rn4MWnzIyDkXHJNdsrm&X-Amz-Signature=2a405a7bd07b42d953a05cec84a2a3059358371e681c2e0ec0b4be8174b1778c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
