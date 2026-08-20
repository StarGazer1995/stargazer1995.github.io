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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4VOIWGM%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T003214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVlRgH%2BheyGxjDQ31ohXqc6TN2ntIuKY2p6Wi%2Fb8pOAAIgMVyU9RUtjlLHqQy%2FWrIo6PLSZ3vzj5HBI66R3BTkbW4qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDlvCMn6gUvciputEyrcAzKghZVd00HxH5Q%2BEhYx5SkLXwbuLC8wdo8GHTf%2BtlogpUdfvAUBL3NZvDiae9iUR30T4xTw1CrZK4ugZFp8IJPROromgr%2FBzxLtzxq2rJvxfUYte7kIDZvim00wjLrMkCtQXxsTkHkTV6jhkdzMjYDwqWGxEhEeTC9ePEyZQhs%2FM4lEEgAwn4tl9%2Ft3Y532hPGYK1MNgbXocbY06YwkNEDTuNaS5%2BdkAurP082wA69Hnyg9cd3ZE60W2qyBi58iU1O7LIpcbx822U3IF%2FH8IHWb4m5OahJ2OfmCH4owf9tfONHADrZpTuvTHb%2BpBtz9EA0MMrLCRMYo5sjEBskoZdOrGv0fH7Vd0ZSXkVYVnwqNYpQCYA0PrGY4BxbkDW1lgJXNtleKufScueZYWwWgLDixG4JGARfIpkqqFrFlCrWSg1X17waSsds8ke4Lhcj9ZU61Oq0vCA4rt4WdpLFGT6R%2BclXImjZded2ddz5gJQ4I%2FOxLV8BYJ1nhKFyYaEtVT5qjWBs1If7yEhH89lwCnQTd36dd0dMcrn3iqaFLQA5VnTOGlSs2GY4TyaMjx%2Bpc6BMPVhtSmRL92pphv%2F%2BQQNTPoJ9N1hmOLd5gV1azfiDgSxcAZivnGDv66HxFMIzsmNQGOqUBiTjlo8GF%2FqutLCKI9ptI8VcBDhX5%2FSZXFCiklJhYav%2B6mo6UOM0tR5LDNprcN6DF7B1ttxeOfdF4AgVViASJNVYhJG%2FzUxgU3tcQv5V3QAbVHHApRhP%2F1NX5doRj87S6BK9iwV1XXkkwzeAQAoGjco%2Fg%2Bj%2Bn%2FWz4f%2B%2ByIWRzzRpMgogZcv%2BhcP1rFSnV9VQJZkMLMAO0ChXRYw307n9TINkC0Qrl&X-Amz-Signature=a7c9ee627b2ee59537da4c5d98343730557fed6e7baa4a28f046377b2a402268&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
