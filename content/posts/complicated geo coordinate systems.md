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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPDGBD5B%2F20260724%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260724T225152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCsbQhn3VHwK601arOy3TJvWsvJpz7EtoeitMsUCkw7%2FAIhAO6uoaDI0K7zMnLuUtwC8PtICP1Zo4QoRFq3qxjJ0lr3Kv8DCA8QABoMNjM3NDIzMTgzODA1IgwRBwMOSa9UtIR8Lmwq3AP%2F1ZA%2FBhd50q5ZPmBfokptLm30N5VtmenrkH1bD%2Bn6q9Kw6wClJVlK4vKluIgVFtrGhxxBKxmn12CrfxVH%2FiqDOFqzW7lYsJ7BsJU8nn26mEpae%2BnbtBIewy7Cpg00c8Jd2MtBdTuRpbN7kiLKb%2BuPe%2FHy8ZxHrHvYbTpbtlVhlScBfIuXLMDbpnMAS2QmYzVdkdgoKVCCeZuz7SlCaanvtbsX3KrE%2BMdtJNXPA4XrNcVuTVspEaC8E2kP%2BRwFb%2F78501nwKlvO1JrxWIPR4QRFiT8Nvtoax0qMgDYgkg4XQY44yeOhIBZ8biiIqdmAkftgp3XyCphW7sc%2FL38OI8f1rRxKC53Hx08xLzU6wFRhdl2r1LrOtDDEXT%2FCSUTpOkTxZqoLQkDqduRxeancCU63g9lISG55uOKTP%2FnFJjauIOjevV3I55YxzDJY2y8MNH72qSjCERKKlD88KQE7o4Ql%2BNc%2FDG44Teh2VC3VQBer0hkWn82npUqcyncNA2WxgxwS0FRmAsi2XGJhdumNp8T8RK0xTiimLP2X8mEDf0f2slE88yTFqVmapK7EAThYeOfKkil7yuH7uz0AksOFCiUtCzVhCO6ZTChKuCON4sTgKgXvLB54UGDgoi%2BjzDyuI%2FTBjqkAWdTl9p39tKPconQJ381fkQ5cvbeUhlC8aPND5lMb4celLaQZv%2FhpmPD0Abn193nczBUW3tfl%2FElOLAfRl%2FcJkV8JHZj9drUEgJ0TOpQ2xizVp09M%2BRi6WXKM1%2BSh1G1ZAH5g8bHmvBhUmewNNVS0%2BfleY5qONQjSqyOvjDiUuCua%2Fk2KtLklrqtS7LxGSs%2Fy5IGm3Ia44rVMJDs9EFjV9J%2Bk6Hi&X-Amz-Signature=cdf25b9bfbf9770371b335271091157beea3a0ab17f4e426e50d7d43a77a11ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
