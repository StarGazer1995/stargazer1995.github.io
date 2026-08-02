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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YI7CRUMF%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T111407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJIMEYCIQCYtZfuJXK%2FVjE7bOJyGncFoMDaSMESzrnBaEZKZ1aLDwIhALZ51Ggy4%2B7Uwfh1htlFLwiGSGgHD8AkrfFvA38syu4jKogECNn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxD32qQO2vEnkL5eNQq3AOlTATFs7bhu2x0rUqgpVmjgWvlj2fEntYzIzqp%2Fc%2FExkWaS84zA6uo1tSMIvOHpyMhiMC8iX8nMbOjYazvL63Zrk0It45dKSV18%2B7JJ2U0ESw7YR%2BzdjlN%2BKmAqlc0uCHWZ6qI2Xs1rwtEGYlRe6Rzxo3XqoQdAank2uqSTv0MH%2BnNtzdY8rPemPH0kAJo0wEnz51yOPykKC3s7ChUVoUwneGqzP8pljymC3%2BK4yTlRefva%2BoT50fHN4IbbmYIckeHCEk5jQ2hpiUqxZ7eRLF3icfQIoL2dnXTlM5K7lObj9dMeUp6YY3DpRHONHaHOlSBlmbcF%2BuXJ3UPUDjtD48NlWcJPADN6NehYJ8vcDVQW%2FOSlVo9nsVLptMICSIxBWS2px884M00S5uozWAtSz86g7xKSYGAoe8Fcsu0doNlP3t9uE7xcG4lMM24djF2CO2sTQA2KZ3Nqzwu3h5tU%2FF23kSJalCT2AB%2Fp7hcvC4HEMV9%2FZYsvUpQGHYjD9A6YNFdfeBAEmAj0nitMr5TRgf05lYDbhjt79CpSxRMamolaBB45ZWXRlsIAoVpYuC%2Bc1WkBpKsiEeB1rEEd20bbeye1I9uPXKm4j5GAlIG2q%2BPJOgzEBpFTEgw1pyOzjDI8LvTBjqkAeO3fa%2FyN8TDR61g8vZiVDvfaO7qbVxysJfQU4kKEldt6rPqlync7sCvqXKDDduraYpD9zbFrGRFHnr6vEOkOQp%2BPFh87EhCAnTqwzaGjX21IuknU9Wmbv9NJQEbAOVB3mQ8CJI2kz7on1%2FdT0Y6idr3cgu2ZxAxCtcbCUM2oy%2F7p6RQxdIiqc62J%2FyLLV9MBa4Wk1yPE4HcBXeM%2BVAj459p1qg2&X-Amz-Signature=9a676bd5f7f03b7ed5ce6e422d8b9823ffe0fc68a2ce43d01df2e9ff903e3fd5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
