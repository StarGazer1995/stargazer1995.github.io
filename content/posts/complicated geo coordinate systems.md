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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663A2BQFRR%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T074325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMKTIb2v9cm36CL9C4UMXf4IX%2FMhrhCT%2BCxqx09GWmiAiAZ3FoiHWzOg1DxmjEO7d4En6%2BoHwlcBC4q14pjLxQW1yqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM81WzXievHIAsWxQAKtwDe%2BVC8wLmCwOSBM75%2Fyn5IiYiWVwqPMv0fVf0Rjn2O4gszzkk9qd9tpiHFYQ%2BSBAwOZbMCwfNJwLcfVOWdESpLo5%2FVYIGceytBClUEZVcx357DUXGH6qUPtT%2B%2FClbajToI1FP9FaUK07MMZ%2B3MqBe55g8OnRE86PfQ0cX%2FJx6wQ%2FmV8xbDgKEnW3RmfzSPOLGV1hjlf06qUHrLMw2zAPTx%2B2eBIHmEwc3zwZuIWcEf90c9JdgdBDlzYTzP5euSrK2oFDwGkYj96TgTwDKrNOZLidtTaKOcKZzBRgdtqvlhefRBAS5rV%2FGpXtlvHbgou%2FLJ%2BSUm2G9hjhgWqYzn0aZAlis1XsVwKJze1A75lrJMm%2BzyUfbT38j9j2Q%2FqR5wypb90VExjur7LCD45pYAP%2BTICqDzdPTGgbotg0%2BsII4t0UFAoRN3VFJz3r3mvgWz5gS2cmSq%2BfJO953ZxFzZMhTVariMhq46cb%2Bw2gYgQ%2BIkbnKFOY%2FsAfa5FK19BVP1DALqnN39S6FXLymf5NQbrK6pdYZ7AzkyYNXJhEO8AyrFG7Dsf7V2D795McxuakP8XQmqXplkaWrWsp1LQtvOlje%2FdergeY%2ByWvHiMApBMctaEOvv0wXRDLvSzvlFu0wne2C0gY6pgHbkvaq0fnLDvioPjvBQaK8juKFQwLL1W6v6%2BjQmL3Sj3Eq1tpXRw77NKtADnvKmXpgmIetAAE3ZZyz6BJt4FiaIStJQ8USsp8kIgoYbrBLiTMwJINBc0qWlVHx3EIJC13OTe2nRYcN4JfPjN1Ml5cE6TkeWnOUW7W3LHaJ9Am6zZ0d%2Fu%2F7X3b2n3HJcl20IF7YVBP2sXjJVWQDCjzqBVz8HwCIh0li&X-Amz-Signature=18575c6b2144bce0a863c602061eb5ae8879b2421a7992e2e5e318a7d58c2639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
