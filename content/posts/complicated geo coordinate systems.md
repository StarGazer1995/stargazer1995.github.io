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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YJUOZF5%2F20260929%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260929T202016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDsKxuVA%2BaM1kIZy9IxgOD2EvHSRMSQ88QztoAc9AbdqQIgaR5QHkNepf4FlfLG3uIsE0BJG7zJ%2FbNZHK%2FRqk32qlkq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDI8dcAC%2BDqsyH2wORircA5yhyCXrn5mVT4fNSXIFukxcInaSXfTDXgQ3%2FvpplU%2Bv9aIrk3xRn0MFPUvGCyTUNT2rweHYtOLPUAfcK0UX9dGaUZJZKT9z7wMv5CH2nyvoEKh8OTJmt2K7V8oJGMFJqj1oIDql4uQwQgsNbgHunA4cp%2FbF96Erj4b02UOEIHsE1AOw1a0%2Fxx3NKnTi23ZnlUvDKzWKdShVWa1RsCcJR%2FmWOVYXQOdenn%2FFJygmXdLm9Iq4lUT9%2BMdDssf8GK%2FrzxKB9gLZnvM5YoQkSubmZNP51bupzmU0pfiizWBHsttW0nc591whd7Qa4UNhQVFZg9QepaGaLO%2FRsYGOoEFTl9%2B%2BySTFKt6d1tB4g2nH7o%2BKgrPjSquD45vCW0fZXILqxd%2F8sEwwBP82gHSg8wUitlewcx0123jTfmhn4TSYBXjgcqfm10bu49MMsrVYhNCAw%2FOaaCcQ%2F69cK05UCy9VhIThKSsgTM%2B%2BPQQtjp3zS0G32HfYnihtZlbl%2B90SFeG3JMdNNddeICTMAj9YnSCvpeH0APT0qLY7jYQFvCxnzF0w4UnYTFGUoiSekTrLSzIViyW7Bwjj4sU5pc%2B4XedtRXZjCHTAWXK9ty0x6Fyxl0Y%2FtekQKX1bS87X3ngoMK%2Bw8NUGOqUBJ%2BfQ3enFz1anTWvhFfpZ46%2BiD1GpM%2BG7zlrOGGEF53RfHuWzHenQg300QMUf51KerlQEx%2BF%2FQlueB8xHiibVt7TTFaqGovCwT3glRenntIcnvPxBCzMpdWC%2FgRIMhI8SZIJnW206mJR0f07HvpQOsg65q%2FAfshpxjqOnxy1SyRAQaYi%2B8djTYAGU08ILjDTcPJDZan12aAo2D2RDurXdtTp0u5G9&X-Amz-Signature=9cffc85222421bb97468fdea0d2a6e33cee69d563485d7237efaf1cbe5d56999&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
