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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3MGA2MU%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T205737Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFCBE%2FuzUwyRn3yugKJBDqoyC5PqeiccNCX6F%2Fd7xRV0AiEA%2BGksN90NWBv11cM%2Fbyy1SBVnp3EwJCJeyxyAqp8QabUq%2FwMIbRAAGgw2Mzc0MjMxODM4MDUiDMeizXS0%2FbYk1b4%2F0CrcA0nlih0%2Bp8YcJ%2BJ%2Fc9aiJ1o9xPhKk3m3L78HUT1SYb5b7qy8HLdPdpVTmE7%2FMDPhKPNvpH2AA%2BPDovSejiJbVoXaOQ3SL8OEUEW9QS%2FpO6fryh8kDrYT4gnFHpsWWzwPD4BpYb2WKh7t7q3nbEwR1d12GlrC4sYtCavEmUKPRTuiEvsx7%2FY9b%2BZWwfnVSe8qyZQKv%2BaouVmrdmFnaZGNYcX1MOSDYZs1aFWCYqObvO2LjA%2B0CsvnjZgk2odbovevG629arVjR7ZhXBSYOo8MkeX%2FSKEvdO4J9%2FkQrYcZhjMjoVSaEH6i58CD10VrNlNRxF%2BxVehbOeUaGgHoKkftbqpajuu0KNRf2TNXx6tlpNwbdol%2FBOTP%2BvpfGGRQZ6CSqCjUOKGhBhgml3JFEEJNIFVxsc5yK%2By%2BBKx5g%2B1SlF4jfmDePMl4bRc%2BQqL9mvXmzytgpZhoSXnx3bUWrwKPDYXBdbeVq6aI9jW%2BEYxMwdgZesTOoyf%2Fp6R0A9z4pE508dc%2FLxhCaJ82wpZs8awWmARgvBdfTf3ukRydxfTl7%2BocgQ8TpwXTGFkVcHAXeVsWQKRaf0fJgyCdZJq7JV13Af3NMXy3xxuifHgRPQGP%2BNAJl7dmsLU6ZFC6hScnMKydpNMGOqUBiaQlZdilCMFlejJuJ562zNFj9OwryY87zomjJh50Ah3mVUIb99mk51iNdsAhPZVyLUq%2BFWk1i0%2B9AOgTpBLQTTC5gtg9EZ7ZPaWeDMELcsXpcSranY9QordEZVzOJtKsiy0kV8J3BwpqiWYhMGLK%2B02Jq%2BFxxqZxFWW3XqYQ%2BVNhDuzcnEtVktHnun7GP7tAL%2BZZEFOWL6uILIywYzLBJO0R%2FB6Z&X-Amz-Signature=d5ff6f9593253227eb1df46f8bf8311f895e7c6042a7385dec0bef9431140e10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
