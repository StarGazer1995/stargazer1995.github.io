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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKXLORXP%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T031626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB8GCQjhNissLqmvPJTVRkq08x7%2Fz9KNESRbeea6hFqoAiEAutDjCrVDQhXOw6v0X%2BIPFqh27%2BHIukoQatrDyKFXZhoq%2FwMIZBAAGgw2Mzc0MjMxODM4MDUiDHW%2BcHuCxbj83w%2BWqSrcA%2BcI5qA%2BROPcP4tywf%2FhuBVM09cljTTGVASmVEaTnB3K7iOrSkV%2Bf3yKlGEA%2F9tdI%2FNa63Qqmj3xNbjBWx6cM%2F0sfhxmZN0paAN5eMI3e8HQSFM46glj8x7ig%2F%2F9vb8xEzwnBFjV9zYV0n3xL%2B%2BFAcIGfbifVKqBJ0I%2B1zCSg%2F%2B%2B%2BWbcp53J7MqWmTIVcInmMDTKBzhK7yzOaoIsYklgXPRtH590zRF%2BBPoM3AZGtCBQWSoUNGwtO5T182O7RlPTZqlJ9kAvh0Zw4orm%2Fj8noJf4CjvL5RwZ37I%2B60e8TaLI32Tgw81WwIDZFZ%2BlbnTZvxcRlCVwYe48YW1vyDp5J%2FueLcqj88G3gCDU8Nl1ixM1foBodpBhEDDDWELBhCDd43j%2ForhOK0j3e0ollz5fP4NuaxPRBjWO%2FfrUMSz7tpOdLAZ2R0ZrpQzBfh0XzK2dN3Bc52aGiyOHn5p20L9pB9YHu5uOjZbKshVrJsyLoUsCrpszVklHzj8LCJFbopY9NUXFIiGdDBeLzRvvKru46NhyoOMrdg1Zi3mg8WSNNADWA%2FiXisglfIJCAKRWUKQWRuGZ83tu9wN5WvpcYDUpeFHoNFtWWl4YhmJcTMNXSaYmpR5ISlJtA4tkGRwhMJmv2tMGOqUBBRu4XIRVwSqFPTI3JAHbrkZBdG6EnIyS7PnftgqpH51wIgtLA5I%2B9f63Qm9YTu%2Bujg0hdWL%2FdEO3VJSkWjWwXhtJOELrrgHf1U4mqFSRn1Tm%2FjcVI5lELdnZjSV3425gEZQeazIJpwMvhPb%2FaL5pWLlkt7VrcjfRg3CyHvxMfLm93VmeqHZhCXpuJuJmn674%2Fd82Qfv6fmlSh95Z%2Fntb2M4b2NHk&X-Amz-Signature=243e1d7eae023992056760d8babc63d720ceeba5bf358bb2e0d26a5878a2c6fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
