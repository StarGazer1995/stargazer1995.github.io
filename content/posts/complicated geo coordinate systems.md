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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7XYO3ZJ%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T200855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDD5venGusz991f3UicJgOaEbcu2cwzx54a3kNKPSKb%2FAIhAMTZhT%2Fp%2BuF4CwB95h%2B1IZ8xPnVLX%2BCL5VmdAf7KGbrLKv8DCAUQABoMNjM3NDIzMTgzODA1IgxmfcSOVNEP1MUpYsEq3ANFrCJjymTjwbijZt7djJTJrShkBGN%2BhlsYp9cHwuL6SdS%2BGlWAcc%2FXJtwE%2BMlC4tA%2FD34HtqlZRyrJlNsJGxum28MYxsrZLwwMdkJtOUOo1oa63CFFRsTtO2wKq0q90F0RfUWkFKPoaEaOiRWhTGghI7suniQtPBHpnR%2FYLvzOM2O42SywHunEUy5GIQrmW70as7%2B8xhtTyN9xkBRkG%2Fu5ikALsRT0tJBOxguqZjliRhSnGdUMTEm5xQhapNef4%2F8L%2FyX2lXc8wc8wVDAW5bJQm21YtKq2twNUAYTdZxZKgPY8OOfovMYpx%2FWN%2FgGkDk41rTWHBXE7lTTwLx0nABXANy%2B45SALGOUDvls2RSPPs11szIfbDx9WU1kCY33aKrY6RhU5RUDMVK5rQmATM8N%2FR2kjaSe7fJB70%2F6wycKr2SmREn62AmfSh7LJsSRzohdOQTXixtOrDNvw8VM8FtNQRd0zO6%2BdduMy%2FvQipy1XgmtgEBBTa7bXTmGqoNjZ4Cg3EJwlpE1%2F46RJPGPTXZwYQZuYTTDbJwZSkepHIueqXNcF6MrnZU4z1Z%2F9fUgLyfR%2Fo2n4qIrPUR5luMSTCnslvMP6bhPZEWfPIcVcP9aLAsmNlya77qXXkOUYRDDbqqzRBjqkAWf%2Br0UEpjkV%2BH21LfuvAgf7i3G9KGW8Ge9R4nyl5RMxj8iiKKg%2BCk9tpWbXtiEH2zR%2FoTJajiw4NzigFbcTkvVU6VcinQpZ4kA%2BuP2%2F5A0v7P76EQDW99RQjFHP42IHJH3NNGaIZ9udwPjEIizt8mftpthodt6VdX6BUzyWzjMcj%2FIlaVO9Y0OBcapD%2Bh9oiw7C0fRn8wZwznWe%2FRUq1eVoPbFl&X-Amz-Signature=4f00c7c86ed30df8dc6cf53e54e141c6e9ce7bb25e4e808d6434941f1a220d05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
