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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYVHIBNY%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T074159Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIH7krrn7XnF%2FRju7HkZJyHKBOKOEyAKrUy1cy2QlZ8fdAiEAiV%2FCNwrbTOxzicGCcc13CMd%2BqA7h8jtyrLyfwj9F%2BLAqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEvN7mpe6AkL%2Fvk8ayrcA8I5XotcT0J1Ns%2Bc2Ma3HISsJQw%2F63AfbfR1s%2B0ZpRuDKTjX1yLq6m6U9bl65KSJRwFTZzFW8oT0qzJtRdYoz%2Blqrs997jUAIwXicYFIXd5ngZPeScoBYnbdoL4I1uZsqqF2JPrYqLh9i6p%2FzPTGJNlBEk%2BL5YjNRfFHQ2zgV8%2F9NOkrI%2Fts%2FSwg35O1cvJoHhE5Bqi%2BIEq8lUE8ndumG%2BefjIwTlQJIH3DXOoP3kKJ%2BRNf3Lwyq5cfrto97ovt9UdfaHturDRCRJaQ%2Bo0VDeCfYtvgaPVRxZsk90v5HX%2FHxAA9tVo2lhUW%2B38JHpSlrKs3%2F3%2FApmLEAp74ijY1Elc0%2BEjrnIZj89Yg6Tr2l5qz%2BU9Q8mDPsX4%2B3u3U0XVFVQiZ0UvahKbwrfisp1kYhirCgn%2Bv71aKpq%2B7hpXAp%2B%2FgmppOwVwVw2J%2FKfBAs60I37uJUXARTUM5vNt8qY%2F2b5bWvuizWtcXCd4%2BqP3%2BYGhz9M10%2FUNMo9HVNdhEmRKsfmhEuLmcwL1%2FaRDj77UElZrK5mS117LT8SOryCb%2F3UqOlalfNwaXoiP6q%2F8uX%2BKR4TiKYwXz426r5tul0FmYWvzrBC%2FOuXxtgc%2FkJ5rrGQ%2BDehk9ayEBISDG8BL1aMIfx2NEGOqUBwLG8FbD94T5vJ%2BXtsx79n1uxyy5BpGbiVwG1LNy9aEOZwbzuVGKNxORHOj10IEj6ikN9%2FDVfCzMWmnx4kbKhbNTuadA9uLrHRvhBGoZvz5o3pd6%2Fl8B%2F%2Bw9SOwGbTwamR3hsauj%2FhA8kEKggRu%2F2xutiOVqEfy0h1sHSTVMXgHCS5MBsPZk7IXScI3mux88oT9F5tcIyeckNDI6hsvv%2FVd9EJOT3&X-Amz-Signature=e74e29f3bf1072549aebbece44d670b3fdd578275d5c089a35cf87b06568d049&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
