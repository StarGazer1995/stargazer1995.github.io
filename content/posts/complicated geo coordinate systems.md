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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UNFS5WX%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T223542Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGUaCXVzLXdlc3QtMiJHMEUCIQDkPhBTvpUwMRcMoAUksJjfSNuRoYqoIHU8SqW1Lye5nQIgTquZuChMWM3HlK7BsYo%2FEsAccTfkr1WABP5%2Fb%2B25hxIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDNa33W389SI2V8LjRSrcA2B8a66xhHnrgLUpw1TXU%2BcOK%2F004Hjhji7a6roztDRu6fzzlX3ACVVPXCWwYu8BqOUY%2FQ89UPmYKiTo%2B50pvBfqqBKkPD5CY2oDta44E2gtbqjRgbyCAeXhXjSRUYSs1TAqDTQxZ6wpg9YmafgWDczSK9pGOEtHjxljQXNhKtJ5%2FnmTx0FSKO9Q93wnzXba4iJWb7BxceHFrxckkwXQbGtUlTDJ5DNROo7o%2Byad2L5sQWNddTqYA%2F0NEzlGUf7udRAmEpOewXnChgOLj5maxyFo6f6zVjS9K%2Fpc3urtbtLupGCmUSf2TVl8dXVQWdQaLQwrdhgyxmV82bgXtv3m2dnT3Wn%2Bp41cm%2BFZCY%2FfsKmGvZDk27PJtx5BQvdg3qvf0koya0NJfH8R0aDtBWnGjSP0iWqcCW73MqJE%2FB%2FnAOCrIdhxD5af66mubQQNRrNkZDXbnbtkLGHE3nBHb7ftFewzTUTM%2FfXS%2BcVAwEs3sIk8f84Z7jr94s83MiHEmikI73DbIhA%2FzMDDUqa5BOmYa4F7BkgZv0g6IltwR9z7bAW1FWAjINi5jt8Y1gi%2B5EPkowkww6S24%2FSkt%2FDTy0F6s%2FMw8QtqqKFqOkNEOBbzFW9VRehOMIMpxst9v5qTMIWBoNYGOqUBWnL3o0giQDswGx2dwk9yaRu9dGDk1MczC24D8XKrzb%2FFXnNyS1KpSZmVVSo6eM85Wrq04eAiyQRHIIKkljmTxYY8b0J9rN5fh6fLtPccJSXdl%2B3oF984GmbyEuVGQAAP7jnSRt8PSnmOQK5MjWdbVdptQj53LkGeuxNll5m4l8BD953AjNr0woG9qJH6wTg2FzvYPy%2BtTtC1lD9nne7SIIfAxfXJ&X-Amz-Signature=b762405746aaafff19a121cb9cc7bc564a543614d6e10057a22f51ffa8755ce5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
