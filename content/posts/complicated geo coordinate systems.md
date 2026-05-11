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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNYCD4WT%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T054945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIELqlVVU0rTSoTJfq9b0b8gARiu%2FnNFSmKhvEb19cB8rAiEAvVo65nJ9FnDjumkg0Fo3FsnKrHpQswhi5EJw7w5Uz9Eq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDDBbPc%2BLl8SvXPbBbircA%2Bqe6mNZTK9FOZ7GovXFq3XfhyjuYxEhzkA%2Bxv%2BM8D4EibC6ZCxNlniIs9SpWF%2B8TpEkcNALT9uq72xTIOIDvwaPKZJH%2BOCgHOcGXhfso7Ymg%2B1TCdbflAj1aoO%2FZuTPLL4k%2BJJ9j32Jq3g470T1MaJ%2Fnbq9zPM36INEDQs12MPJgsl13Sq4LOguMmiHkEQnmjIztHsk%2Bfyv4m1wWR9k2WttZQYf253nNAbDGBF0%2FvP2eZinVUvmTSlZWtGvA7X83mlrZ%2BKDFAUaDMR9HAPVHAHBLgPMxTxEJ4ISB80yqtntFlwjLE5d9Xz2CXtEX6iZwwVxYDRAm2pMLl6UGrgsXJ0lPe2%2BgJVrpzrs5QqPZByOxUrssnV5WMXOsTlgv2BC79y5B2scFyd7jpvXgKMRh8FbgAbbZg4Gc2aicnzVJ%2F%2BqPmO%2FMxlc2gHQmptgNPO%2Bx6Gs9DHE%2FIG%2F8W%2BONrfsKG75phpJXn0W6yICKr8RTyXCBgtIwD2iZ7ruwPipTXm5tTs1%2FAVTR5KqvImdjTxYb5xllamXL34dAYmLCQ854rqcb5hfEZwHKojoAli3C4Y5bUCANDgB%2FD40uhrmyVm1ZMOCeSiPQtC8raYCNwXqjw2lJRycetpTKPcjtmJ%2FMIbbhdAGOqUBpjwczKyt%2BDs5rli9Y6%2BX6WFcBtPIHJKiFDfiaY748D0o%2FfnMcVqhaJ%2FjmSGIzSzkBPhXTZCiSs33GoRQLW7zxgaJkkRkqWsgtUrzcNKnQIOPfcKHLP%2B4uvlcShi6vYAiJAqfdEl9H9tYCNpFlyfD07rcsBTIbJxCeP8k5OJhZiNkdHMyDywM95V9QBwWMpMVXNCmS2Z3%2BEZ1qsT2PIgaojSyXuGd&X-Amz-Signature=a3ee33d753494a9f2d70de243529a59723069a00b3fa7b3d4bb43753b63dbd58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
