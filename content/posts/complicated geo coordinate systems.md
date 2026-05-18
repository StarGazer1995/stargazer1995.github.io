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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2HWJ4WY%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T113708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD0Ypunv2sPDHF1Mv%2BV%2BFPiNPV4unv5AP29I0IYW38fmwIhAK8Fd8kl%2FTgqcDmVyKX3SN4ZbAQ2d%2BxQS3%2B5uOpNCH1LKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy9FeI02xAHR6Gw4sQq3AMcbt6%2BKqu3W1IlFXGfszpS16ySWwZihf7%2BtGpKJGMnfxNgWNtrwAg%2F4ZnccSNjyWHFktN9JX4XAWcgsfd7a5PyP%2BsQCGrjEZhT5TI8w6UKsjxYcWSJeE41r8%2B4WEBF7ZfN%2BChXDNyDUBv%2Bs5CvWq6N7gq5mP6haPrKlT8QvofCnkoUpM90IYjFd80awfXnK5o4vo5b33lK72WfwhXr%2FP5rb94mUWuxMhb%2FjYv6g8smRcKS6tVgJS0%2FG1X8INw3oidQ3J9p828Meg4FE8G4Z5cL5wPXLuF1D3fRac%2BExlIeiR0JFUf0w2%2BMoCWf2bxx9zUN5jnrDr8iKYx%2BuDaj1Am7jMQeUTPPsJn4VRJxLbH%2FT5XXlpg1Wk1PoRJvxIYFXm6yN9%2FOD0rK%2B5bGJrwurG6VFA3qFM3IIpcM%2BipSKs%2FrexirEhvqN7jhK4ZdMA6sK0n3NIUFZul7aA9NWHKH9zM8a%2BVKgWDgdMHsGGJ5qjd6IoTLoGKFMivNOc705n7XYShjvAUWqWI41lCitE36InpyzRnc5E0A9eFiRcsNmXVJRQYi3F6r%2BcNVdRvkPjduUkfC4UkKaNB4pm0J8sphDDjfbeaNkJQXyPtaD156AUa3YdhzyiL6iqgZEP192zDr6KvQBjqkAeURKCaWrcdt%2Bmw6oDnqYVMag5sOnK0iGgwp%2FZeB70e8epY%2BoayR5Pvt2cR91Z0wKomhS6zRc0SXYsRoesyrWAQZorC4I9AnWHlmWTjshxYQOwzPuPT4YY2TZqMj7CH%2BqfgKznoJJzD%2FL0OECr%2BDvqOLuENBu8pCC2qyZC2jwQ9MDYIbmcCoemu2YEzhoPL30ojmw6u13ne4aecBUl8uDOMJLe4d&X-Amz-Signature=bf5a4588fce212b4e86826ce448afcd92579bdf148343a89c2c40393cf4a0ef2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
