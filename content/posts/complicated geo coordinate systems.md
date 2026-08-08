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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y24DJ5DA%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T122234Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDxxOpYA0vo3qqzaVwRwi8s8P%2BDVxmk633DvcACHcuCZAIgDPpI5A5A3%2BYeVk14S5KS3a%2FnG1NKmBkZOwHiHsN%2Bxxoq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDAaW5I1XOCg0zPXv7ircA%2FJX3yttqBe6FLsBoW5nMx%2FNYBCAsywrgE1lcNxEmDRrC0aJ2hkEQalpBPyqCCaxOdOC3T9D9lAaolA21r%2B4f8ki0vuU7UPFwDq%2F8SeCaGfJ2uydwGld%2BKvkI%2BJPqCSKx8%2BTW%2FdsQ6fUl4u2BHziAayooKD97WpV0DOHnILw6gQwT1GHhZoDT67YeTN1Yj3cjFKkVYOO2PvYR6x02lnbiX2SWHF0%2BGBUpT%2Bzo40BWCc4wSPeyYAFLMovYKaX7cL8jWGKWdeYKbW6MIa7SeZGzTJJ1AhrdJREGdFIAbTCXnoUYkzjVWv36XJQpJTBOJXzm8C5nfz3x%2BndUvyLYNox5P2%2F1Ju9GF9iH09K0L4EFgd0C7PiH4Mkc4RbQANY0zGVAOBOH%2BOqW2ebKKY3RBj1Os8YaxcjxuP3xJB7eztR1INF0MNIulYpIotR9bHKl1VRKlxdwDst7eVaDrgvytZV5mkdEKMN1Mnn4FXKnAf9g40t1XVJIgzsnKfFamAIsDqD0L58CK6yJI7K9s4C07dnMuXhsbkU%2Bs5GyHVi5dJyFFMB4xZ8Fl4b6SmRVpp0H18OGzErLdhvDWLAyMnDhSArER9XHpUwKg6NQhxhRmOM1DTjLKy%2BUnCF52zcuNZbMOLU29MGOqUBINRoCN2jQaPkEJX45%2FWlUnc1kSqm%2F5fim3tDF9MKSEI%2FPwR0jGGoTnJUNXqCzueo2LVtb95ElR0xquN6t2Fe0nDd1ewI9VM3QJvTWuroquEh%2B3Y29%2B0xylTYp8DLHDskBPv%2BoU2TYoFxK%2Fvvg7bxLUemXG%2FkiBoGBIzcqeOEWZjj9NNyqbsN206VcYvK%2Bb%2BbYdLnBAcyWChE3DhAlvL7VmeJKXeq&X-Amz-Signature=29bde8cc80c5aaba16c2e439fe02229640d6c162079581e0e667f93c36158707&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
