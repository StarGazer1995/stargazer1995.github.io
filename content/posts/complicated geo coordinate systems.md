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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S2PXN3JM%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T084735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIBA340fEUt9kfz4hYwSRbOrbSSAUBl%2FyGlsBozbmIIMyAiEA68nxNKWj0Eb%2FGmzAw1v%2FeANaBJc5lTrTxjijxKEZVKgq%2FwMINRAAGgw2Mzc0MjMxODM4MDUiDLtJbs9Oac3RC6UeLyrcAxQjLrrC05gHf1jDkKwJCL8GMLYyAg1n4Xztrxoc1r0Irln5BfcOX6sCKk0l48AJSy8JRCZnAGcd0GttptAdym5%2BGqpXum2xdBlzn3P7Br6xJth%2Fh4SO2nvLvG6kT6tqkzZDEzeGo9uhakbb12ZSlFvdPb12WcZKkGmM3t0aS0XeGM3O1Ri%2FxHxe2%2BdEvPrTXkgx0yicOMGa%2FcbPyIO5as8oBxBKTGwlzy0oC%2FfSXKiwPM5LdJlFHLhJ31OWcRFUFmFrcRX%2F7Yso8EXHWkrFQtsKMwPbGGjNbqdHAZS6RyGFA1M%2BrJ%2FS3HWZiJMW9W0Hq6bEzIaaTresThilLVeC1LLziXSHy%2BmPDbkaQVY0MqUdDFCn4HQ0EQJDx%2Ff%2BAKUaYwOpbwILB5TPMyKSS4XlB81Ew7Cs2DWSUAl%2FhzhqGV0QU3N%2BTLvIJNNMjGXKKSHIUjZ5wjimVKEsx8aKrqH5O%2BV9iWkjf897jqvrEaJAnCdk1%2FggXzSY%2F0C0DSLFT49pM2FEKcuQUWSYxnhGtf2uZbr2m7zHnmV2ysPUn9JvseNKCCqcx0LsZ7w%2F23qxyFr3I728TEGYlV6JnkReP6bnXdFccMRpJ3Va4S8VtCUU%2Br4cE4JTTG6blA8D%2Be5wMOfC%2FtAGOqUBKlyM7qVans8Ju63aFLKk1QnpEL6fhhT0ZXEF7CEltNOoaVIOAwM%2Fj2hAoSgZk84iY%2FoaBcqr1d4viupQuxo2%2FinMvyftmGYpyN85mRDZsWoSC3UcjU4uv9Vrga2ktJ%2FmN%2FZfR0w0KH3WmnQwimlX94qIJ%2BzctHysGR5aiR5YJ%2FjayMF%2BV39ADYf544l%2FDo0PggL0LI0Y4YCmXSywxpH%2B98dH60tI&X-Amz-Signature=d1f870e512e7dd724484caf217ff9c27b26895b67d79aa80014630598f647d16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
