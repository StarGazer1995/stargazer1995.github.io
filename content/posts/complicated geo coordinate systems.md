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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QUNWTFX%2F20260702%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260702T132648Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJHMEUCIEWWT8v8Enf%2BQxWINheKrjjRoPlIisNhYj0NVi3PLkjOAiEA95rT%2FXYc1439a1lT3F5%2F1RmQwfAbZ5ZyYp0pcVjUIVkqiAQI9v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGT%2FRf%2BTQs5umjF3IircAxnw3x7%2BL0%2Fir9AakxqeaKy7U5DN%2FOWeBzFluEFX7xWn5DJ1sm66LuErnLu%2BWV2BmPRtUS6sijtU%2B910sD6Xaxucakwu5Q%2Bcy%2BVueeZ5Kn1f6EFz8dmRdDq93c1eRnP0p9q8MDkEctSg9Aw%2FH91PBT83Lv3R8YRFeXQ2TfNT8C%2FiXrqO9XOdhrGVEcVwGByoKn7SG9utT8KnFa7A0VIstv%2BiDzBgQoHwivOgDkFHH0a8X6RqspXM8jmtsXBvrXZo8N6cU4Q83k7DION90zxK30%2BXMOiLQyn%2B1OQhWn9FpsR2s8KfVAimX06HJbs5%2FBWl9w30XBnNzrWfsCYkIOv1wc3Y6I4Yor6OJ1vj7IJG5ne4lHSfpYXhdHKzyQhFZPNHnAQ9aqQ98CGDahyKri5wVip6z7TCchRfXHls49VJP%2B01A9zEgGvk8xBqw3Ut3i9KpcG1VTiaDKzSfMkqRX2H4qB9XzMAANJgpOqUadz51TCVVeA7dvBEUJy8R0Vm6hc5l9xZILCpZN5Yo91d7zIUtsiwxdFvPlaSBpqB%2Fjijh615Z7RHO67IfImup6j58fvA1vMQjM0DjFw0nVnXa0jrOjRDMjino45jfVxOISG%2BZc0iQKj31HfYwNK%2FvRArMOTHmdIGOqUB%2FT9UV%2FctApOSmjEqABZ3Ze9nAz%2BOf3LolpBSu%2FkZ%2BCP8XNKyu9MuyhSofTBL0xwgcRskKzHlcTXf0eLC6k6JHJ6wTQmcw3gvRs5sTBcpHRReg1o7K%2B4lQm1xOuIeZ7HL4BAZZG1F0TBLtJQ84zitsWueNlweoP2dAFKIOWNna%2FeiYp%2BoRSEKrIkQ7QHybGxXj2vJFqpnfeeTHd9ccSkj%2Bkkp3E%2FG&X-Amz-Signature=ff323d88b7e0dc2336accf5d362d6946adc85b1fbb797623d605c37ba17620d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
