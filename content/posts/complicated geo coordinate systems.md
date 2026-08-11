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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWJ65Y4I%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T084256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGyUaIwIAcIvPhx3D1mSKkPQisCDB8LHiC73esacYr0tAiEA5qmQZvmfOIAEeGctV6Vz6os9wKwexLJebHc3DAWDgysqiAQIsP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBCyw1vCtG%2FRbXkK4SrcAzzxY6HU0OV9uCKlw%2F0ES64plz097ivP7pG4ODQCJWgYPCIQKpEBE0F6C0ZOIILDYpJ8aD0lKlk7zvxsn9gSbIfPi%2B3W6c%2Fhl8KqPj6oSir0zu47z77b7w6LX57SkeoB4J16MCfjYrdJqaA%2FJ%2B1vPN1UIXuXHbQqbDrSBOlbgxi3TS%2B4N2SxrJor7Rd3xQtgUGtO60LiOEyR5H5eTaFpVMLHbzqXxi%2BCmDfeHL7SjfTqJBoKeIDzJEnSKep6uJKQsd0%2FaL5CRyzEi0IozZevezJ%2BoilhtdRijMhG9vJmuAFgq2NBGfBfKefbbCDzJsO0lVk8PC1L%2FrXNsd868VCXK8Lf1Mt%2FGdWWx6aoGteEIK1G1aJouC9xxhid2kbh9HdvpvDp8D4QsbLIkupVxqQK%2BugZhVHzIVVajcSyc00p5K4IdmcXDnQ1NxIQROeTt50MaqB0rCIQpu4jg9Deh6YaXNRWj%2FvZ%2B2XJoDmH1cw0pc4D6tc%2FWwZ6gRa%2BZQFJJxBLi1%2BpHQFv410su7YAScNAzkjgiIkmjBNQzkiA%2BbUz720pJbAXxWiEsowieo4hxLA52I1aqcgQFsdURHYh%2BBeHNT3ZqZit6tJkxQeZAqTiOpN3NOrveq%2FnJMI3JU%2FmMP6R69MGOqUBkV7msFE1pmDaGJcNPsc3uYxsED7KEZdhDxYXaReTyHQvx1WYniqKo7QVXvG5sLHu18gjteUIbwgSSdEtBRRwbDcjH%2Fq0MkgqKrcfcX4gzxMJNtew3U33r0fn8%2FmTa%2F7lULgauUO9CxWitJ3rxzhybyMtSh9AYXZxTvCpn6jux6e663Heu8SuQidJHrWroCpF%2B%2FnpUR%2BraNgUPzBLiXSjFdQmrZjj&X-Amz-Signature=c165c1666bf9adde840fd75ea44a1e3d8ec90854694d9a0be572f5625aecf224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
