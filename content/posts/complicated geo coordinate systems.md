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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFAIQEAZ%2F20260902%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260902T172953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYixq28RgDagYFVBvf457Jt5XaUauUuOTG7veSEuxcgAiApZJvMJRh%2BuD0%2BBylKnrV4foLG9XJUUlBT4OzfBrD10iqIBAjI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeIms%2F%2FdD7ATYeL1VKtwDH4Fh1JBQPQdTXbEQMsXHVJ%2F2ninqaKThyiEwdPOAqp0yCvf8PIgauHjz1bfUpAEkldcndjSMhHcOboGP18TGS%2BjDsTLMotJ9Kef22n%2BGsdou25VLhHjMhGd1s1jUUE7dLyul9gtyXAKSXnneW6tyPypw8CKOGSxzXYtwQKs1r3RyDZG2uo7TyqaBBU3WBhSA8PLCc92gbNh0SJ%2BtcGHF7aiMgwpmqTX0GJmCEb9HVxR5uTDB25kwrj18RmkeqzuuNjCfT7PuhShdJr6veDrenRzYTiDvaIZTFw6ErRZ8J03zkNeQwCiBVZ6n3O%2BwM7D36MSRn7xiX8JHvW0E9ScV7BmRMfGE1HtSv1CX7c9TpTsqECGkoCQQfmtRCE0TrdMnS%2FYmMPmEmzDo6MYuOOO%2FZeuV1BHR%2Fr6Iq7tIioXKsAO0T9A0BBawRs1agGfCjdl1lQf%2FrTiRV68P%2BnWUTciqKygYVll%2Ba8CXmYYViKzExZGNtO9PkO1dLpmmmNGvO1sHNyg4tP75h7OARp6jOcZ9i7l79%2FnRr6J5sMlbMlblT5Mz1aJRGrvT6V9O%2FW20Llr%2FCUBSXj2ykiwgUa%2FxMKS4z5wEf7J4721VIoLjkFQoBAKkifyuVOJOFzYInLgwyfPg1AY6pgG1CkgQ17axF7jbQUfUgzZWw7t7rHyA5zoeqCwtSQuX8QPUI8jq55e0hA9PxFwZa9gf1KVthZEfh2pJUsjUE0RI2wnw%2BI8FwOKZcUDc3wRy2jOo%2FXQVpQzAC9LejhOUjYRtG%2Bh0UnzO4u%2FeWsIXmvN65ZrSnooTuAHdI%2F0PSYd22Dn9CjAKNQuwBIs3iW%2BowDehCM9i%2B1J%2BwgAYcviTXzb4NJP79mEE&X-Amz-Signature=d117640756957a0ae2a035b14c7908bbf0946b6b12150b942e43d1dd6e68911e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
