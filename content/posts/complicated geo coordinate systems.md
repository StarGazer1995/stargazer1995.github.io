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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BYRUNKQ%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T015126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBxiUQfkN7%2Bu4i3T5%2FCurIR6wvHOolbtK%2BHk5jGfEP3VAiEAlT0%2Bxs6OUVfJ%2BYIiKz%2BwGPTFD4cxdhLaE%2F7UwqC3nn4qiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHVgeyuxL7C8%2FHQrSrcA3M3mDxyYFXgCd5bATZcQY68qmghxloPS66j%2BzoQmSxttolIgqHCdewCqOClYK1gBI6hh2WoMRaJgvUpaAqN7vimKYwzsnpfW6HshlKyXCY6dN7sC8QrjEYVJ4obAA3pmH6vKIkcBFsuIsFwNYawHWIZ9OlvbDiyxuqJ2FilqvhYBMLY%2FA5cEg%2BPDHcn%2FN5BGJd0vtYwFVgmeVG1XKyZNVVyCCJVHvazw19Tub%2FkZTpjC2yi%2FNS%2BrcRJLYG3QFNEEsF1yDDuZ6z5wQjbC1IZj2V51SJarKm2c9gXb0mRhDISmY2T9%2ByQeFfoRWYln1rGWRJn5ccDnzeCgxrBo2nnGfgP8qMf9r3Us6%2Fzfs%2FX%2FSP8C887XQpQvQSHaVpeu%2FZreBib7%2BYU8kPU9SMNfEtVmBd09wmfVFM8fyktmYkpy0V1XCx7OQtjBJAm%2FYv4XaiWS8vsViippYDkw%2FTMPRdFDIkViEcspOpf6nvOPcSjuaqMb%2FMEjdpYj6q3J2ZXpC51VgAxsssiC%2BNWUYEscprtFAKdtKIPvf1MxVfX4C8Y7lzcWixatvq9YYHJVk7Nh%2Bn2S44eiOP8daMZVEv0etWuY3%2F%2FbF%2BpKjHbaeAaohgj81k0SiqCNbX9Mm8nuttcML%2Fy9M8GOqUBLqY6RdQDjfEkT2l9ZcAyALOa1v2Goo7zPa27xsfyurmqZSz1y5TryuqMd8k43woYt7CIS0jdkQL0EkmtUmQpkTR56e%2F7ghTUZoRPf66HpdU0gpSlWQzfuWncwp05kv9Fc6VwAOIP6MupXgK4x5jNTrYLTNZNY12OClzdyb9uQCJsXvuJf7tX7EOl2l4bLvn3OdCYP0%2BIT261QPxR5olmQONTcNLE&X-Amz-Signature=0f1e83020520489098ed90d73b59c9e43f47a6d1c962dca7972bca71eedf53dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
