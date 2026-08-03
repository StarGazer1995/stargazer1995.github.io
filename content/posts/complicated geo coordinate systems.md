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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XWEFC2AE%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T191614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDMaCXVzLXdlc3QtMiJIMEYCIQCjplHgQHK%2FOvsi6pEDtZfuXZ4R3p8yYSaQXjFNiEY65gIhALWLt%2BcRAaYgGzVP3EvqQ5wtGlZvMqg29mffIgy3kWDAKogECPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyE7YKgBWVLkHLI0eQq3AN6tDhijmbDgBroXUknn5d%2FFAeH1mJnpenbzTxWhcdbcLXs77y6%2FUzmYNPdMrDXayWa2vmbc%2F%2BNKv%2BjNdANzmcFMT2kyEYKvveuUlBV2XK5P637svaPTbXlMJO9OIM%2FM%2BhDjxSz%2B%2BmuD4N8aOLmdZUb4NlBTg02NyI3rKZnAZgTtVXwoeu7Cd%2F%2FuckTGgBRNRpSNqupKapcng3ioB0aa5ZQ9LFkcUQCgXmjUulJBSlofnep7jSeZ2ppINE1qh9l%2Focnn%2B9UfDVBAFf2QR1vav3yVrR35o5bgBbLUFhfIt5JnFMJA%2Fi%2FwGvQgHIMNXZDxsmo1tnYoxCFPQ8cMQ2FT092K00IgfpS7fZrx3tT%2FW1F%2Bnp0Wcbi7y36%2FSv3NzWzTYmhYkJHJ7YsYvAR0Imv7n%2Bbz5dI7Yvle1DoZv01gtrfeuFnlATv%2BoWCSar0VF4%2F9bk9h%2B%2F1w7BoDoNxB%2FVLBZH8uznLH4rHx4viPPVNZex7MUGwrl865%2B8pm1sE%2ButGQjHd3lr9w9RMNnNXj5Wmsl%2BAtDGKsYCSZa6NE20RyHljw8AAcEJNhd4%2FBPNPdgDVX3C8%2BQNS2BdFd0RNzrL6z%2FmgIkLNyYIhWTOQylkxVSShacPyvIUwWc1urDQX%2FjD3xsPTBjqkAQ2TCF9B2pmCUwRJvyE5cEnclwLLCA4q7cCzcKTQOuxFFx8%2BU%2FnnbsB6jCMigqUoOiE79AgvRi%2B2tx7EJV%2BB%2FeznFb%2BFkErNGuLyehABIZlkLlv5s%2FZngK3JvWhR8lBBS9RmcqehJZC92dcaQ2O6%2Feckir000obkXEaw5jmiyWdiD7BsCuqHNJIyMwzZjQa5b21TlSnmwPqWSgdFPitsRiHAA%2FbL&X-Amz-Signature=b6a4490f01b8ce0176bbc661132e8a7134a378b84b6638998348e8972dd926f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
