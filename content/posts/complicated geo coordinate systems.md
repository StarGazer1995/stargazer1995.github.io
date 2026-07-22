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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643VUKPBV%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T045653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJGMEQCIDpxoNh6Az0C%2FS50eHS9icgvvzvKR74Q5i6ggoIH9WQBAiAnqRg%2FE87M39nhPz2GQ1OMPFDxmkhg5DAUNMm%2FcsMQJSqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhYTwoEwauSRDWN81KtwD8r1L449TRegSQdGCyo6ypnElAN4YcdlcPbfxtmI%2FP%2FBZnk8xnTLt%2BCzAe5sjuLbgjUS%2Fom5YWyRD1rPX2N3olhlPfqt5jj%2FGb9LJweW9Up%2BUNQz88wanExobcuGTXcX6ET6a52AgVKsmLnyO1vzsL7IAsuPiUQrlMpuxBuhIIef2%2BWH%2Bk7ZVGsxbIUTz8hyAjUVEW0pw%2B2yarym8hIMrNnORB6yN1wPj%2Fp3mFQIRNleG%2F%2FSbJEPED9jWLSwiOMk98%2FHB67fwsNEbp%2B%2F35NKXxsAqnj9E36NCo5exm65%2BUe9QZ0a0IyHv5aT2PTTRWGABzfTsi%2BPSZ46LBAKAPxwOhnX6GEVcSYoe2S66%2FglLfzxlc5s2tjGefBMXVsKq4vjGf3JFB%2F2iD%2Fq5d6XCkAid67NlOw7ZAbsN%2BNQyF7DH%2FvUwSdFzSGrxGwinaJ5R3krjxsuPZZ1yhQciFOaq0eOXUfpu1EKTRjaiAOkJlJEM333sbryj2aB6Q3%2B0GS5OoDtkKb2xKtJu3KkDj0UrifL9N5D%2BAEUDNM8yCBx7tB74yaocyn4rCQNUOXpEM0%2FKjTvce%2F2VkDY8ueoUFM%2F8%2FnSLJM1TMp3gHiBLyDiKHttvO236ke0MmVwAhKrPXcEw4vqA0wY6pgExABB9pNnIhpLTI9YmZynBnd65e6fIhVUZyyoBqUEANjqXBDHpLOE44uW550J5HekrFYI4nYmvsVfHcXULnY4O%2BXWdjFOufkMpGHQicM6w%2B3K37%2FJWESPPMPtgbuqluKqAILl%2FnmDWdAo%2FDA6zOHTGc46sRZEmRgHhU1ey%2BBRbLIRTf49pDf3dcMdyY4X9CJRUMruO49AhunJuxfNht%2Bjr%2Bo6KB8WU&X-Amz-Signature=a67323fb53abd45dcab40620a56cde5d6d2d3d7d3207f76e0ee699cfae2196a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
