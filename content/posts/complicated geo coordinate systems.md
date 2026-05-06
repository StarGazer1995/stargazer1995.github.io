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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QY4HRUHE%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T114417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs3xJzd4wq%2FhiHJ67%2Fl7106zPid23Nu7Qg4%2BRd4J8jEgIhAOj0nk6r7V%2FWxQeqnd%2FqmWcyCVRlydRv3NcwoeeeyLmkKogECJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw4pdB7yKW9MswPxh0q3APVSc%2F9fHctxqDZed8O9vr5CV%2BaNRDgzUcavLcJ4PgxzZvRIc4%2Bn9wH7OEtexBwcrRzzRy74OKS5rCDO%2BvPlAsmiljMvfjgRFMnwZpwJMJ8yFRqGPZWLd4mF6ODSdtzB3pNsY5YuhhmSg3Wep0iwZjyavYd3EaK%2FMNWTy6g77gjJSue0AKEgBurKvPc4vAMMW2pzOaK%2BQfEWL%2B0HWtruNXGqg7lCcLnIWBh0N9r%2BHKIaePoqkBeQhP6Fnl8%2BN3e9zfyytSzjTb4YC0txMHptdsiD%2FCEf0Q6OqweA97rQUvtnC1NuRPvPxZDQb%2BaLAcEmWyajYRzoaIf425pebJakWKL3J03NEFJbhTagYEl%2BfdpW8zQDN%2Bd9Ii4lK9p8N6tAEhs%2Fq%2FMe%2BYzafB4k8DYdP9bAbq6a3yWe4g2VNKEH9mw9PEBeAG054pf%2FG%2Fk%2FCsZ%2BU%2BApLEvHt%2Bjfn%2BuqQpH8QuH3wcDwOp9mmZ%2BeAIj8O%2BKlg6MN8bbD4z7kAIA2CODgRGYbEqWCuOsO6dCeG7MvlqmSQoi85vmrH5QvXWTdqI655kS984%2FKnt7ErK%2Bo2fiUB%2FuJKQ4%2BKkf8sPay1bfYzyhKal1TLphgP0vhiUL8V%2Fi%2Bt4D0Bf%2BHiPD8GaPUzCjxezPBjqkAdCvXseiej%2Fqgayhy5cgcul6A5n0rQB%2BxrYVVox1xEJNDxu4k8QtK7tw7KolKxSblrIFY%2BWr3ioQXGNJqQMBq2%2B1Z52XiOGEeY6ojDeidGX41CmVyeu2B6xn13ZCBBzaZUD3SBZZPgBc3lDKLrgVBjiWiDAS24h8qcJFxd%2FCzk2t4ApTlcXmzTwst%2FnfxZqCH8vvvA3yFO2JKehyktbh%2FTificiP&X-Amz-Signature=7a8e0e46f7eb401f9b5bdccc365dd0cad84ab29f2f46eb5b50b2418b63ec1dc5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
