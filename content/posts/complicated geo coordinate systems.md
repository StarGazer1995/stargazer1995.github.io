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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662S3DMOFL%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T225630Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrZ3qCeLtsxR8Q4TPfyFChOZt9cU1nzBzvzfu7NmlvHwIhAJTLMFaSLtFIjtnkukM%2FPm7fcyUmubkdELdGDfgARGzNKv8DCE8QABoMNjM3NDIzMTgzODA1IgyBFTF67vF386PvDV0q3AMyUe%2BF5HqLAjduzMhV6zzSxF3MNUy6Ci5r3svGjx7WbPBN%2B4oyITPT17V3M4FJ%2F0M3bpKx8B%2BeVKIzC2A%2FlMGDcH03deYIrdNuzUk8sUobDWlelNtLUpUCe4AGCxU6ooGAkOON2K%2FibMJEVP37c39ei1i11rk3QB8V%2BCV7qm9Idu%2B%2BfFQ%2BjDxWM7VYe10tNkSBMpMAHNfoabtFV0Jrn%2BjVm2T%2FWb9kMIAz1jtXE6UMSmO1or5Ylh59PWOLzLsw4g7kE7u4zn%2BT8Zn2Kc%2FJ0fP9XQHZTLXkojfhxdjCMhja%2BU%2BKAcpKZ7hYPNLJDKYuNmkXDUtZCJQLcS5HgOULLUBWJq%2BeUQnQNtr%2B4d0RxxGtpCsxLP9OHxuvpaxfNbeg11Hk4TM%2Bo9cqw5KQqFlRtQQwAkUNV3nC3TGH92%2B8%2F2bNhXjLHDA%2BJeQyy70l02IhGV4%2Bic6X5sa8628BNyJww54LsS4xcyikhLhYjEbAAVNZzUN51q0w9eOfO%2FDoawh6LKj2DENRJpsyOstse4c8C9UuBLk9PpItbjH3PVzr731emiQHLc9KLJet62CbUF6L36ayS2jAtmP2CfzCF0lX0wU6yymLN3NxmbXIsEPB6lN9QJqrMeP41%2Bvga%2F%2BHijCj8pPQBjqkAW%2FQJQCtMIl%2F4e5sftmJW9f7XH4y559IPT0yUwGgiJqLYaO%2BRFtfIwwGcrXRlhdokDQXhFKsXWjOTeahXolpmGAyeUPZZmT97qMMp6SImDyLjX8H1hMhGQeanuBs5whCdjjNyBo6EJaHKCI2mRrhtpAr8O2ftacbKO%2FitLCHClKjd6FXgIAfBE%2BdxRrc0sUo7VHmu%2B2Blc7may8RJ5QVo1eBbqRP&X-Amz-Signature=24ce7afc3abd50808e91f3ec5e52d6ac0955bd56029dace0a9d87c4b63eb416d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
