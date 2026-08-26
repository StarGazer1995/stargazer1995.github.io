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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XUYSMWKI%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T025626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIBuS4xLt9XCQlpdjkUlL8mnYWH1aO6OO%2FL0EUxjkMK9LAiA66wlDLZj0vnrDBCFu6X6X%2BtpINLeRvmRw0Seh0vKXqyr%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMsparTz08Iy4k3trVKtwDJrSQjVSw96rxAQ%2FlNqpa9gQsNr8FEg2eFD%2F%2F4n3LnnV8%2BeA6V5%2FZtQl7ETcNpmMUwULXL9T8le9IINiJSAWCXNwTo0M3wSFkstx9ly4OZ5B92j6p2giKVaHvHUBefq7PJcTZRmvG4z2zo8ykKrEiqxFEesaJrYsmnSK8kcuhfywiVFfw0HRp%2FJJnchFcrocR5S1PkDK6krtt%2FiqaZl%2FjCYCJ4C41cb1vOtj3cnTiu3R%2BvT9%2BIMOa80kT0P4BWZyHd7zdYj5uRplgBghbaq%2FMWUcK04da9pq%2FrunL2cVxv7j9RQiNUN36Dk2%2Bt%2Bg1XmvfWXtb0iq3UxUgc7tScjvvr5sOeSEsWQxXDSHxYI%2FkejVkYXF2jG7XsqIUK5g%2FcxT1ijMz%2F%2FG%2FOPnXSpw5CJeWw802JkLsIRpY3ZpXV1PGEVlyQroh8RCHbFcTkQo%2B1CWjht4J5aQA8eE95gYJkgpfE2I0VDTZDOjMKYTjzg%2BDNiOF55gQ868vEsxd8DlD%2Bg6SB56KghlGteSuu5RJ1wtumvygxZLeECSOmQ1V%2BWPJ8eLJMbE8Nadmgpp3WU6gJ7A%2BfHp8piXEJhlY7SZZiXEm%2FWNLHt9M0mdkX4RR5IoTuI1%2B19GmmVV49Iy%2BkUUwnZa51AY6pgG2ij19TR6G9fbxRlh2JSdw0gChnt7HjTPEOi1rhnT%2Ff281%2FxB%2BAzkjFFVXOfjt%2FXNHZ7%2FuCZ5sdWAchlYJdxCBuWDXp6dfN77C%2FUtLnuVN9SgC4eNkrvS8Pwany4J1Y2nY49wdBf5ogHAGeYgzDPOYi%2F53hrPDgZkKip%2BO4Ems6qf88xr2qSmdeW%2BK3rWnmPDDgWS%2BmGqF5HbWO%2FWVl58y%2F8%2FKd8ko&X-Amz-Signature=655ece4db05cccdabc598bf15b53ace4d196b5b8c22bad9e8144d0f040d2645c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
