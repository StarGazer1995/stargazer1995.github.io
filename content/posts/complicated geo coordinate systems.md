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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654ZWMP3D%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T161301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDuMZKXHekkbk2wHZRI3nfcvTbCobtzW5CZ3e2d9qqoxQIhAJdK3ngu9gjhuzeEGf4QQKkbSm0S5m2sXB1UQccYxMW0KogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzzhlhsq4mtwmab%2BXcq3AMgJhPTJ6psOTqMCih277v1n6ao47gXon9J7OxwiseUK7c8B%2B09Xn4LCkwNtc4KCoib55Tb5Gaefgyk0pRgCn6s%2FKEg6jstWeN7Ue1Yg9FeMSjaPE6FVdlsgfPGEV1JjsaAGAMzY%2FQfPaQHT3abehQOMl1mwyRb8nc5A2XyGjj3jCC9qr6g1gJ5TC5nnA%2FsfqYBJroa9q%2BUhN1mAc%2Fwd9owrDTB5diu6Czq6GvspoxFlJUNNBnoy44q%2Ba7UUQbs54W6ofHDSimcyJrSOaWLztU21irYJ8akC86XlwU3Qb2h30QdF%2FxZh%2F6KSV%2F0z9YqU3%2BK%2FdN2ksM9ehc24J4yvZE2l4h0KJILGDRk0L56ChD78t95u7euwi3tAcHjL%2BMmRBA1gbvbONk%2BF5jHmV8MFV%2BaZzGsQrI8VZmsYnvlwqrwZjREZ5f08X%2BB4G81reZEQN6urHSsbzLj8G5wBZNhnmomJcM3d5o6NiwSB%2Bv%2BDMHsaseA1O8u9UW2V6GVDcKCG7JfU8D1DuO5lOEdUmXHJyC3SwgroGg%2FJYcz9Nx7BCk%2Fa8win13wK31bUprcwLn3xk5%2B%2BssNh27JV%2BLCTm5I3JUQ1eZ6SA%2F6YBE1dNazuPVzU4198xvBM7UBhAIz8jCB8rLTBjqkAQrOZwRrmB6knFyV9kMYHo15MjRfeV68gy8y8YLbo3Ec0HVCzkC5wwgP9pWIvKonrqWyEgIG5X1dEJ8s8amc6yL3oIcWuAIghR%2B8LAf5Ad%2BKGrtRlDMn8x0b0B89Zq%2FAIb09T8nznmBrTvaoSp2C3NORy%2FpprgZedAtCw%2FEjkMFxwAAE%2FRAWTjVuL9B%2BgCoogA0Fai9AlZVp1Bh%2FM2uAvZwxBcLW&X-Amz-Signature=8c1ad8d2ecb0be73be88056b435f6c25c5ff5acc18b2c283cff82972c8f86d40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
