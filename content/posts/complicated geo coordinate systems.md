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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SSDBGYWE%2F20261014%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261014T144623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCM%2FknMXjoItKWtoXG95dddFFGYAPg6%2FYMrQi4RY8MI%2BwIgRcZlXR4XeiRazEzyQmPPfgq55hvIorStHRGNmrf10FsqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDMuIlQSQCyDsEClfyrcAwoUgFYslCXYRzYFe2P4uJEUbFgtg8OaB7FABZXPCY%2FVZ2bLUP0Gxzagv2dGo1%2BPZcE2s2kaK5LITJI3mMWv8ow4GoIiebP04BZRn5BFaPpaNdARrB%2Budfn4east%2BseTGPtOsfC3Ru%2B18XleLn5w8JzPl4R6Vzsmqohob54cbE0ChfsTVRNVw0WaomHCggcO9EF%2F8xoxJuELfcfhtRs3a9J5twmcg3aXG3mVw562%2B2BAuiTKwcUbBoIL6UL5C2mi2MMMxDiRH0kmoViU%2F4WktRR7sneH3JWebPWo6q6GJEU7RDeMP8UP0b%2FV6V%2ByoyGEWEAArhGEpfL9PSbmTWF9yuJiw0Tpi5YN6VmjB71dvTPKDox1WQPiPPZpy10yfiM3Vpk8JQ5l0anV64B46yKXu9pj3XWtAPt4Tvxq6PvG62CjSsw5aGzKJSzhNIREjFjaV3pviBFbYApuntyMX0ptQnJHGEjWkMNoJd7Fvc8akkgiM0W%2FWOOid%2Bx7Sga5qiV%2FjM7UkrqQrsYg2G5TYsweF1mUsCb895m8v3VlYDlcEjZDJLJoqgKZT%2FjhkX0wxJ6WIFphOWfbkEHTek8nBOKERRGpT%2F8VterWy75JT8Axaj1xdZTSoGTXUQvI1oYvMOjqvdYGOqUBOwFp2ODx2bunKlmFpPBAJjOrvwkaUt6ph8ilXqRiiTcbLmh21DhK%2FoW0eUPBDMt1i%2FswkGnZJpfdvuOWejnQXsYf4AfVtqLno2RwCr3EHb51PZtIPzlWk65M8S1VR%2BtcDCayFCObjSTtSkGP6Ua%2Bwddlh5ZlStY%2Bruy8qK7Naw6NmaL%2FnaKYANtP%2FJWizQuYX52LWHtnltSf5UdK%2BvujE0EBh9Mb&X-Amz-Signature=0b2f4be29e4a71811f5b77cf279b1b307877e3fb779a83bc3020799d452ce804&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
