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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663URH7E7Z%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T192619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFMaCXVzLXdlc3QtMiJHMEUCIHWnkxfvxbgPCqwpo%2FEv4q3dGlnW4A80Z1d1bXlnjlhxAiEAiI7E4XAyrsiqgw%2FCLT0w6TxGhrkAmiGF9R8Rtb0DQFwq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDAHboOd08hC9OjkZaCrcA50mSADC%2F7ZyV83YxE8PYe6uzKyjCx6ZCiN23PP%2BDZm9eA8G8GQFnaIUcIHQ19wUVmBvMO7pgkApqpN3GB6zBBAksnfb68RFzjBEzxnQuxFqmpLHEGtWN8HZVXN%2FAJo54WEtmzsCQ64kQLDlEO8XRlymZjGyA%2FbTRWdvC3dVxhGTrAT%2B3R0DPyXL5U8bQtom4uLzvMWztcNtq2dQbxeOWQHbCM30rwYwlpyekfBrymDzjf0mHn%2Befg7OSYZKzM4WC7E%2FahOzsTYzi9f3cPCV494r58aCD5tIjM5vYtHgIqqR0JX5Tv95nRs8tXjwiq3cUUUF7r2ans%2F%2FGNdrA%2FkEf5YzdYMq%2BmtPIQKtmMT1VRJRp6WLJNaA%2BOzUNrrmMqslVSprSv00u%2B%2FX9XiktFLkQAtHM4qdaoR9Q9TxrhmLK%2B9n8TdNJ11FUsiHkTuT3OID4b4eX20p%2BxVMmnlU79c27gs%2Firk%2BHqjtE0CzJjpec5%2Bu%2BVY0z%2Ft1lDVuEMxRQAZm4i%2B13ifXN28uvaiLYqB7yzbUkiIwKCPe%2BymagvlHeXp5ik%2FYJp5Cg0Zf4GDvKJMOtQtMI%2Fq2yrGuLnYUwL45m04OgaawPDoVjsrb67C6b%2B%2FWCleDrSjP%2Fo5cUwxHMOS%2BiNAGOqUB1lw8rcV9tk%2FbWG%2BsDt3IKcHrJ8W022jsqCVIdyfLaRsCOVLEgVW7Ns37VM4bpTj5%2FtQvSVyKP3ZW4jmnE5LBwkP2nlcj3bIeBAIlDUNap88UXioSaqysZSBlwXAcoAVYiUSm9GDGt07d0i%2FbdFHTgpcICpQ45EsA0Flw1ObqmQXjs%2BNQol9PNz%2BQuOuvhMeTTMvf9M3HlEMZk8gWjtXuRaaof74z&X-Amz-Signature=0f3998f2adef33b3b412b01c29c154f11ee437c9cb9c4099b80542008a9df5c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
