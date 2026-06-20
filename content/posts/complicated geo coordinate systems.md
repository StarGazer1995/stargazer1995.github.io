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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VCINRXT%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T020651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIHgv8DKCYIa7I9bbDMdn%2BtBs8uWCQcxWKgxhR7d2mQLvAiA%2Bov3IESThqyblJXJrTYFw%2BJLJOuyLryPQSOXE8T%2BD5yqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMW7FWBq6HACP9ZcrpKtwD9T%2BFVW7FQHz90Qsum%2B3XjVX4hnrsNyqL2KnDxLQ8nfp9Gspgy226UqhquxttNUlEDIqRiGFluV5YSppgpbRmxPixsThgehSAFl67NDR%2FGSfEx%2F5B48rLwtGGZK9fK4YoKJRf146S98YiFvF6JCBdo00QAcQSVpATb09nuBNczwJWVBwG2SCEkP8uYe1V0Jc31Z%2F66JoYQ5xiEPdcgGLpZBHysbgtSAAw2OP34cKZyW2lbPq7AxZkZJ954gkXQJ%2Bxfl9IZtlr6voDk6GMQzJEWlPN6%2BadK%2B3Z97pEkZA8VKiN9uSUjh4mdoknBUpFJ%2Bvw7Z1iCKe1PA%2BiokGxSDPVUj8LCHZoUgutz0%2FQ%2Bo8kocPc%2BboSFsgjoo3BvBT3edrjxE1vxfUICTk1UB%2BbxUL7m0Y%2BBgpqkX7KTsnwjwDenkNpCvCq0BrVDQRqnCQMGjcggfXkh7MG54ds0rYVxBD%2BzRd8xV04IVoLorQ3gswUeSgBu1avphAWudzgpNlBkM8AgA4c4W%2BwbwfELkEo9RfrpMvfO02lVFdCGTAyMmbhdgzkQtol81R3G7HxxENAOkScvbntFB%2FHIfttQaD7aFSTByoVKcS96dPTwCfHnxjym5v4jLGaXo9g01jolZ8w9NXX0QY6pgG%2Fmc73%2F%2F%2BZztnhDruDjWGP6rCwYo5Cw3TthJ%2BA6%2BImLeMJdOsGbl0n3LHD%2FXpkwArUAvg0ikc1C3n%2FvvFvyjpScUsTTlQm4rvO7QC1XFXFKkC32OTvsDj4Eaq4sP9%2FPlZclxj7O%2Bo1lOVDP7caIpWfmMknZtxW1tL7pwOJreiQ96sf8qL2rO%2BmLeb9%2BSchQDgIOB2WjMNzZD8hzXxU65hZvjW1b8o4&X-Amz-Signature=d3fbf33423e691ad76ebb0c123237c55c40f5f464ebc59c6fb0935f79ff0575d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
