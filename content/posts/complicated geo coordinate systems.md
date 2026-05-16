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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVN53WUC%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T092024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE23gwLgwK5nNQYgZxz18ypUp7RoiAn73aCSGfhVKWQXAiA5Yyi7XbO8990Pg7YEOb1cWQhe%2FBCX2DKArXB3k03l%2FSqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuZ04vM3Tt5rZiVCfKtwDdLAVQJzKPgkykEwn0DIXyJg0BbZuNyimZ1BpVuKoQke8QsO4kCbzrLG5dQb0QEoK%2Fm51AG8pEXRcJdtqcuTBW4x%2FUlka6jAfzIZBV41WKVoZE1sqjE2nPJPNsUZy%2F38bM%2FoWfrwDWGLmeb0pCmYNBH9clW18F8CKoNZT2Q9lUECJGW3oo1%2FemPOh%2B9V5n7UG1ee1GrXJL1lyYw226843GBDUsSVIzvCX4XHIumzudfgTFe7EBLcBnLt09EAztr6Mfgm9lWnd7nYI1aHxCqTR%2FD9xpnIILue7ERedP1obSRpssv%2BkzqQtDOBNlFLeWXtlFoP1lXeIRz4WzAM7ylMU1fOATqPIzdN22sWWZ47%2Fg9CpjxJjEDePxQi1jGoStM8ccCW%2FcmCCKZRqrooW9U9sFUbys9k9wMHsuQDIkeiuRlJ2Sej8j0p7h0lWkzxdVph6gPJZqerl2hzCW1re4X7MifkFMIgXH5JXhD2EDNcRplx%2FwIB0rkJeCIiUseAYV1JXH3aTcU8i45OZ1GV0CAy4tF3hkkoaOMqbg9zCzsKNyBUOSHR7zGMUuZcGqQaqm1BGsEEHhZ5Nu9gO0uUbOOXG36en2YatJrABxNHQBIydTot08Gptp3nOX%2BZSWsgw9eug0AY6pgHpuycOS0aeFCnglZdN9Hi1RDF5uk7a7s3%2BnjS%2BI%2BSKMWhVf7O8QrYcLAI55RM8r4YcZqP55grtE87I9xWD%2BB4Dj5c09IyYhBJo%2BUYn1LzsSuFMZksKhst9D3nZErJOzjTYkol8qx6Mf%2BM0MvgI8rEA8MTZUGxAW6gav1JNjstqGC9TGPirq8kRQHrVIzrbnJtH8a6GiRmdcqZB61%2FAyW%2FUMvtQZN%2Fu&X-Amz-Signature=e08b522da547a1b56aeb746a42203c847db7e6cf0a4bbbfe0bc1323770cef931&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
