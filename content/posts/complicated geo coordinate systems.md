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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OA5JTZR%2F20261009%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261009T173947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIEEPtUMSfiuPSpd9JMDuzyJjsBky65cEB7X94N%2FI5sDbAiEApFMFLZli6J%2BPAyz8IqGg6vkMNKiSSRe9Z1EcuTedR2Yq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDMIj%2FcpoGdp%2BZAAuvyrcAzJuq2uXvFgfdKhTedqh9dOb2%2FS34L93pPIJCuvXjvlklZljub46jK7Iy5r55ZPHMXPaVeGIfDV78kfsaYoJoRfMJdQuXS80QydE6wn6abFa1D3q4ZbgBR2RoEpk8ROLUSdNf0PpDT4WxkLNJe7F1So3fuwJGovrAShFgHFidJUbgutjVazPP6WqAfyEA4bqQz9S2CaNlPA0n0I8B7cWWqA4EpkK5%2BMYMgFK8w1O%2FnKhjNwnI1Nc5EoHG4MpKFFEm6KrxyuaQiD41bA32cdRZeMDAPeREcvv98UQvOSn7T6phnjA5o5GKeykYqVgYy%2FQRPNLryo0P0BXYuAn%2BzmHl%2B9zQUnrLE2FWubOihe8BwdTK%2BQje01OJ%2F3FzoCnuIBYNEyQUml54EaxF3ds021ctyIMUNo12FJj%2BLHu9vpBaGul46P8ya%2BKzZpv5j3suHdNQZ1e2J%2BzyJ5UlmXIMRkugYcheCwaw6aJ2MYX6XkLk8CxQpGk3xkD6x8Bt%2FUWezuTZXBGiUYAPOXVQbmCZlMip29rJ8qsCbA5VdRM51%2FGHyo3h8E3hLn2N4MhoI0oIxHLovPznXPeghvGR45i5MIFHpriLiWPyxjWlLcDKFTdEwZ0rS4xt4pnpFm3bQgKMIWypNYGOqUBEP7owkvsANjN9UvyiU0dtZaE7Oj%2BfslKfyQyUmcDPi3og9wQfW1L1cc9OXROtk2LdwC6O3KWAhB8IUl8H9Kr6V7sgv2YUTChRjmYoDXWusJzFGtLBUUa%2BJTYTnnn4FeRenpyDaiNWnqWgMxm2K33n%2Flw6NTJcMRAx4l926oLrBumzqlWwOp6G9yD8tcbwSbj2jHBd6OETJNtcJsCrXWBZiAfcQhe&X-Amz-Signature=49b28ad66d681c8c771d8376cc311681096a0e3857656fc91e7747353572e0a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
