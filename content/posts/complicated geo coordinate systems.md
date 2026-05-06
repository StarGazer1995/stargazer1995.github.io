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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN5RTSTK%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T080455Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyMMCB1SD6Bu1lKWwRo5XIy052wDbmug9iIscpvrBfZgIgCv1JCUz9MHzHAwriXVg1%2BVlkuS4kReivgtlosKjyhZ4qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPLKVTq4STDtAyLDuCrcA94yZS7WMSJr%2BclUq8Q87oEllbYGQR9cMpeCi9cTBzN2mlVEoIgowPpjCedelnhgF5XATmqPrVXxYmVOOMWll8ZIDsDZ6p1q14SU%2Bm7o1ma2ghLogAnakcVq7Rxt4wcaVcPTHmJjGz2375jl1j4BmBDR7VoMu7DS7d1VqBh0g9migCKM51A83dxOF31%2Fotzfdni8V0we2kAlVPFzESICJeo8VpZIGXFrMNMwt8k9lLkrIXxlGVgqNfR7QdwYCp8mUrm8A76JF5YzmNBrBnG9NdhDGJAbaNxo2eaMX%2Fk86SsWxmSSXEiQaLOS6%2BbvhmUV%2B7v3XNKl%2FPN8etaUgz%2FYExzPLJjhORFSGTVRn9Wuf2Sz02gY5X1%2BUguQJV2JSxTaJY8cil9Mf9vG5tBaT3jAWHrLn9o1oL0XNZv88%2Bo3aTXJUCL18r3PUwyVLTNMguTA7EJBvLJa9leLJ2MDt6CI1nxk15mWqwR0VJWgACbAJRHpCqQYEhlkABAnL2kRZ7%2FnnYbUMSJ5fUXVf30Dx%2FR3i2Cr6ImsBKLSZuXkMtj8YTc1bqqjJ7MujFStiv%2F4sxXPGtmdXlGYDtBQ05tJiMg5Rdk%2BPEH%2FPEnFS9R%2BMHAXRV3xwAqB1vXT6BdxKzmiMILg688GOqUBMxeFe6R2KPdICBxA1BZzyftLrCc8vpzLM4QK3MJtzlF78DMLuRjx0MPtCq56qto7EZ4glHTQzlWwGKpoa5GikR6Ixb9O0ya%2BapPaiPMTfqXbfXLhjSEhTCr%2BZKvfNInSjH3sRNXzo6IaH04wIeGhu9Sz1DrBnJf1LoEOxtpsc6xRhDBzo%2FZz8sohsJuDtBDhht5dVaO8LBwXI8M7ux%2FPC3ekXFmv&X-Amz-Signature=0342bcb714990d4cc4c0b4b2e4485dba91bb4c273419c5eece48073da2e094f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
