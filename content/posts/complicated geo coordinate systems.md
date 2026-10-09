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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMLPGBSM%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T032309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGoaCXVzLXdlc3QtMiJIMEYCIQCaYfK7njwbR5zV5TLhmBLK37Sawp03hEbukK5Vr2t9BgIhAJyRNaCdXIhzwFTr421wY%2BUmr6C3l5v9q6FiGHS2%2B8N5Kv8DCDMQABoMNjM3NDIzMTgzODA1IgwF4qqsJA7VWh4FMEwq3APbfcYlyn%2FLnGxjkiSsaraWD2VcvWqqzBf%2FkLtvqopzggTgZBk3f653HlcJVu5vuuquyqumsZoVrwz6Fb5yDxoEJJeKnKB6njBQN%2FmRXwyVj%2BYIlK8LYlpq%2BB%2F%2FcCvfSAkYKWyT4fNKdnqHl1JkiAY3mMfVTolkXaEXOgDTZnluW8uTT4U2gesY3RapI%2F%2Fnjn7LWgWMP8KmlSnDC9an8QqfgMyxUKAaw0h19FaeLEUNctYO0mOjzAtd7rY3OEs39%2B%2BKyx2as9C5C2i5DHhr8haqsMuW87NiztJWm1647eVCaRFtQBUmD6jsw32r1skKPLEBc1o%2FwR6sXkdmqRtU4G7sitIKo4L9GiwmmVNk0UTsKeUsSywwvkTDU9zIZpuEx4qn5sBT0LgBkSmeDEgM%2FiWmY1hIgKZU55O1Jo%2FNLm0O%2BYXBPf%2BW6%2Bedn%2B6LFLF%2BSgb0uyFJOWt93flKPIM4kcNf0qapXROLT7PHsEiwwnFuXWUD0vDbZ%2FW1NzW5MSstUtpA335ga6We2Z9OxSnpPGFL32Sc%2Bp8ASqePznKMC4dqii8h%2BBBtK32THLexdeuWea%2F1W5YWH1tYpI9OOFgJCcKoUFhTtmgUVqy820J1A4xnpkO2NiMhWmh5XLAC0zCvm6HWBjqkAQmtGcYS%2BffbEvv7lCyIAbyYNlrnSxzNIWnZZrtQZ8uTmIddEmSDT7i3c8O3mC%2Fn7ou3PZwdN1Hvhpx67Q2EKymErXMHYyXTQZoAhN26hwGTpHEddWa%2BwlWjPu9rNctNE1f%2FEpCoOd4qMG7KVLOrZ0GziFoJeCwxGAsTygUOufh0e13TAAQ%2B30e4kj6UW%2FpZLoaRFNLy7UjM6KbI09jrh9Fr3k8f&X-Amz-Signature=0c410a23081c7392719ee94f8e9abce0bb2c11a878f72018914e30fd33a3c9bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
