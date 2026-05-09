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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WA5DQDE5%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T073115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCb1emcIZ3SLwlSNNLjxk5Uid%2FfG3JCE7UHnwdC5yyAJgIgPlL50ldDlYZJUHUhNeXLobtYhBKS1n9z7O2py0DJqlQqiAQI4P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGKVm2%2FWyw8VtIOENCrcA4u1q5Gjy%2FBiGnrrikNwLoU%2Fmw4CX6VXVXGLl6OjiL9fJ%2BsvGeNrYO1GWC1Ny0Fn1EDx4UllpCNqCDe4eBUuR20cWyNzDF0%2F629%2BB%2Ffnddx9MpuGIyO5VArWr59zRyquzq%2FW9EnUXbiTqQwqJQx6uFw10BEggsdMALiV6g6oK9D0UDdM2FKPUiE9FPwbAZHi882J35RxM8kZ3I8QmaNU53MBk6xNSHUMTuYAKW0%2BdtOtmRnmgfHCXUsA4B3YmL2yuDa31PYi%2Bbc8U%2BSf83MfjyceycON03ldnMVWYZVbSBKiTJe%2BFIRcpEgTPKpxz0sKMRkF8MrZxwBaDdktaANyoGJmqaD%2BPddVFgZvC22QZFiJeSn%2BvjwaJwkSWiLEemLu8GB1fT2Z9%2BoPlq0l%2FHjYdW1a3jeJcXKGDSxxvx2fjRb8YRY2uVM4ALI2dZeK7O%2BNL6MPuoUHG8kE0NZkUMQA2%2BLB6F%2FY3aIOYsMK00KG2BvA7x1os8Ase%2BJnY1RSznqGgQhMkzQwoAWOKsks84DjN0RkZpP38fLdsv3xGU8ZQYDK1muGhQu8Kwd4dtXtZPZlivnjJMwEeEU6LhyKt2aIeQIChqmAgwVL3%2BBRJntoQWtjt88KUKD4eGTb%2FsMlMI%2B2%2B88GOqUBZLNbBo5S3Ad4gTfMFU10072YCB249p0OElhJpnf8BcXOc8cVRoUDA3U1VOpMTOprEmXKEyvIQlumVld1IL7NRQ%2FZW4IPkJs2PIW2jJIm2DbB1Tr1qC5nPqh6116K7Zb9WIEdX8wKgbSm2oaG6GnMmYn7uBdv41GCtKnt1jy72Ot%2B122f58HMG4uDptZJytcNuOr46R6Qi4z1YaL%2BItgVdaWTpAy9&X-Amz-Signature=930c6d23c45288e2e485d357706fcce70b2bfe21a779dd85f7c0249463cb8ea4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
