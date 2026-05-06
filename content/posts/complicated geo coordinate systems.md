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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663K4BPLCK%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T172639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD6M4nhgJXHa9ygCH3WJtloTSJfC%2BumlAi%2BVIEm%2B3FCdAIgSaAVVfHcbjK9FZG6FKmOr22n%2FS3DHb6Chzy7UGyjEv0qiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHlqxd5uzCEyEI6BWSrcA7uZyeNVdihdkwnQ9YQU3b0sjExnnQr1EcE6Sr%2BwHPhFBK0FBgmYvimxVB%2FGJrF0Aww9exPeoCauuaRz1quUnzpMhTJlHgK3ecNiHisY3KjKHm8pzHdlWIVN3mhByLySRPsmB1y4gKD%2FU9N2rEFI3L9XRoTZRTgdFeZc4qlvuodhKoL%2B5Sedsr9e5xrUlpkYTaZTT1jXMII4TRKJy8YUhLD7Zymyw4SM1AOANSdI3dpYsjOLPa3Z5hGFQJcb8vyrt4MsL%2BoDHpKEIdmGJ5HLaWT9Ghw6fPJYX%2BmjNxsQrX0h3FkxYcD5TKIWvRSumP7q4H6LIyp2uOzicMUlVMMUU77NyY9gjYTbdE8%2BVZ4oyTlLDfKG%2FN%2BSk9iwKH9BV6HHUrBQ2hAt3rvuFGUEPPvACjfK2d6DRnNqzbxCXz7CQgA0cBYQmZLLeQ2o9%2F1W6e1b3TPVEfn599z1CYXe%2Bt9oy335u3gQQNReSnUqzvHoILX7RI5Ar1ZUkMEk1WMCqzqktdwWXlz3mX9pcfjgSH8wM2foPH4duL9lRbMETrncsWOQmyYXoQtZlX27oZgtmPwH%2BMuUz3LqeSUbpItqQDwg3mYiSIkICY42cPWhQdEu2VIxF0b5T8W6YGrGv%2BIIMMLW7c8GOqUBDMU3mDcT442WcHulYhqzbavnqOguNLQkng8zAFBcFYIf%2BrORPIdqvOQUojyRF1SmonWc%2BA5ayBcfmfGgSlIpPItIel33SdSM%2BCwoR%2FXBSu%2FuzwvMt4pGbF0nip3iiLCCFP78jhVtIn%2B8oW4NApIQ07pj%2B%2F496%2BdxRAGnNXVWVCXGujOkhXhAzMgcdGFREcyy28e%2FriI4BiExwAHVpAtpPoOVtZGr&X-Amz-Signature=0f2bb5dc7995e236713cd42aa6ebb6311785a9d54a23f6a26c9ca8d65fb67159&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
