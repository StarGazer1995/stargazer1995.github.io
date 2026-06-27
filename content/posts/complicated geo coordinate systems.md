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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SJJJLFT%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T082459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICwq8d1BEkDs5z7ItKNq%2B5W2Dug3OehFYYIJ%2BP1iEvCIAiEA%2BdWwhODynwIsaL3MJAqmYpkqduoPSm%2FKbbroT7a7w2Aq%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDJVgya7tgI1D7OUQuircA8GER0nhr9rTughbsulfhwi4IOsieMJtIqGTj4oWjtGYfI6O%2F0xXFs5dlRjhxI1wbFo4ueIWha40hVmzc1AFtGxfJym3jcgR6D05myUqUBzWusPs5SXU%2FCxiUD7I%2BwVJUVLiXlLQLnBWLFcj73mkNpjeHF9VEH40VLPOojB3qjnmZQZbkqBgk9FxsVwAlDmPfmmVG4sKBk7aIIsskE9DvTUvCH5QHJpCynd7P61TWSOUrdQ5kOzgi9t4SwvaasEEcjE%2FRPEKTTXmSvEXhhsq30Zyda0HCbCqeRyjEv4P%2F9x6o%2Fz9%2FTSvxIoNny3gopfEv9HUaa1GrlcMP7ber88uFq1DNEZsRBpgWK4rA%2BgadhUB4pWg%2BNn3HHSByN6So6FU%2F4gUycXpzmPfPU9Fb8vWfEzfdOCMdO%2FI%2FZnQ%2FryYq2XaypxAuxj1ZRwc2Cv49DrC27oYlVMtWLSOx%2BZ9MqNkGBDe7R6L3HsjgbgSiuqB0VGOcsONNEZV%2F53XEBeHfHCNzFwqkxe%2Bf%2F5pUPeUhZHlosMUOQs1bHKN%2B6UYt2QFGCYFCYY11F1NnAO1f6UCSD0hEmSE7TeCsb6ixoJ8qSjT2CHRKOumReHLMqriHh6GX426llEES%2BKu6tQ%2BkGc6MNn7%2FdEGOqUBL%2F0h11wDCfDfffGbN51dCoomnnkYEOfXag0VnF2efHWJ4wlSvXPYjUvnVkAd5ypzdP8V1ynswy1Q6Y%2BH02wXTQF%2Fc3nDMebA%2FcB%2FffuS2n8Avwj1bVx207u6d6N8WRpyeKYOCHNjZWM4QUh9remQwpoPR7EbR%2BZWam0LNOC%2BC7mtW%2F1tq3No4729zENxhKOfcm2lsaV1zFo0sXohm7kJ3zmoZUoT&X-Amz-Signature=16006b922338c7eb67e720f30572427e4da6ed9c1c1067bfed1647d7c29c3faa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
