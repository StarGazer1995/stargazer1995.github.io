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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KUEWKZJ%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T014254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCICX%2FVa2SFuupUA7P4Xt0fnBoB3yFWKr%2BTeDWBIeN536LAiEAzSwZr8150Y5eeYTULVKWYhUYa1JbzKRNpZqKEtIrAOYq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDLFUvhkmfUIkAHAerCrcA8NdsMLSR2BLcUQ%2FE222NYgWu78yaOiEEzFnGt2NBapyec6olEhQlFDGt1MqKlszJScSFhBLTM8MZDbachJv2jYEkOVZcc%2FnKC5YQbpl5fJXXnC5FUXF35tcCerXXc6HwtISQe1%2BglbgMOGNB8JcsPsSr0HVg2O7JuF5Snjz075XIw36QQDdpw43rHM4NnyLOvOH%2Fs5Yb60AF9nA1QhUGyJRvrv6bNbb13WhrK3s1v6I0t8jVc%2BXyntaL24LGuwCC9xt7nPpKqgU3dVpWLoi2ccnixCVEH12ovxK%2FFfIIpAL%2B0%2FGwP8qQUxPoj12Pwn5491Nov7l1bQVuTC7DvxTvKNN%2BL518EEGjYHRBdBpU7O0bdAU2rU3Sofg624%2BM3YlyAeETY3jpB3u4ul9pTjOB3JtfviPmGLLYE5anxHpDms%2BzP%2F5O%2F3zdxjXC4szoH%2BLhkT0CVin7OdbqxpPnkz2V9Tx9wAdgNo%2B6NrLcrFj3owh7mUu0%2BJ%2Br8geDFKk06TJQnbxcy7203%2FIGIvtVGOcu8ZAJiX6p%2F7v%2BmTooyWCuoo8CMY9%2BG0gb%2BvQjiXiD8HBe0%2BEfSHTLUgnrgFNoNdap9S2gQpN%2FT3QFPT1%2FPGG5VBYEjV%2BHHsB%2BY4TSolNMIvB7dQGOqUBozugq%2FP%2FcAQ%2B%2Bn27jzCOH9zYxGqHybuMvINpQkdufOAXtCq91jAwo%2FRxehPYswPS8Lnd%2FYVH171aFGsFBCjC1%2BKriTvs8xnByRSWhuqr054s%2FOqzln%2F35T%2FoITQHjKdz0khkA6iLr8caDkCn1tY5spaqZ1YGY5SIzVqky0Ozk7rJ4QblR1iErlwsJ%2BCEtCplott2uBT2npdiNyu4ebUTusFM6yAG&X-Amz-Signature=209ab4c9969f380d204d6b8c12b8834be038ebb7a0998a719262ec12ca292fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
