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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTTOXGJV%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T143135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIA2RoTi9hC4bOzXxSXZROApsEhBNGT7AUFsUXAksBzPCAiEA%2F4K0oEHUwECs6W%2B3IRmiBYpDdtw8H1YPbDywxQlWHx4qiAQI7v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1qafVt%2FjDSP4r85yrcA7oncwnXm8WXM9xd8tbDVUnX7fcfL0f8zG1bENMnig%2F8bxwVZEKMrDFmHkfr9O2%2FjZr%2Fsu%2FL%2FpA5Bh1kW0iZ3d%2BUHN9fsMG%2FeJjm74QyFV04wCFMTGS7HT86nJFot97btyw4c49k%2Fv97BHeYWDhHTkw9JVFwg4znBqmIEybRxEnHGkUDa0kJNaeKrfdW%2FZ7QSGBA4Gn6uqi%2FQhG%2FCCjcDnJL7K0wpWRFnf1ujSfhCmRUGk8XKTMF%2BAkKfp%2Bs7is%2FDGarapCix656BlUXAvhAdIyBuesW2r6xYmOXfpK4DSYFx7ZfmComkT4ZuLHDrjletKB72upAurf6lH%2B9Vc%2FU137g9Ce21qIjJhABDPWN0jS72iDO1JszEYiz66x3q28f3y9octGlk9E0c6STkBYcUuI1D4hbFyVSGouqucMmpwo8zxiC6bVL7bWo5iBR1TDf%2FW965gS1%2FvKfUriFxT43HNgtphTQbh3xL6GJJgfVyPt1bY70dzO1QUVkNavfcDyxevvuvgc4Mk2DiGNymSX7ylgbf2%2FVCgwq%2BvFH1FqUB%2FMYX63%2BORZaVA1Y7WThrUjprRYFPbGidq2RyiysBIBupn3w2V85TIz0KwvhKojhdIAFpe5j8weQD94GF7NpMO%2FbttAGOqUBG92Fd5Jz%2F7MqN6FYMUOB%2BxH9MK00Qk6ToKAazLIXplBZSqxix4aFQYp5rd%2BxM%2F0c2CDKUxa16MDutQtbe%2FTv71Ok%2BosQm0Cn10kiSUz4a7zKCf1cI2kTXVteAh4OKVMeu7dJm7qPYlTKwurkmdEVjPP5GsMmzC1QDBfPaXXaoblvisfHnBg3OfqA5x0Y6W5wIsNxQ7pwv%2B7pAJF226MC%2B6LwIwzW&X-Amz-Signature=26d5e889c6ec218faf4020dc4ed1c34d5c06dd1c35ad704bab958cb4c9226db2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
