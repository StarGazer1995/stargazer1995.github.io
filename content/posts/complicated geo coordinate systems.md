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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6OXTMQU%2F20260819%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260819T042553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICY2uMo4pE%2FiWxTN92mRudRKHKWMTvSJvcdLShNC9iXTAiBNnf%2B5fjtBioeQQ1gsupYgNYcBi%2B%2Fb7fCoWmnqpGvKYSr%2FAwhtEAAaDDYzNzQyMzE4MzgwNSIMs9s3cOkcu6PYDxEOKtwDGzaGUHW5dpMFYuqDBRffUuE245g6Pn10Gbyk5WgUWW40qFxhMxGr06timuST38U%2Bugh9896yIIvwItfhAHMC0JnfXR%2FLso7eMbFs6zyZg%2Fy9%2FhQy5axfldqOB%2FoThA4aBcBhsI3F%2Bx5TVR1fE6m31PrQAXnTtBi%2BN7DtT46VBDRFnPAyZxsE3RG71b3Y8TSWwC0TNCgt0iurXp1ouaCuJrmKyeJvQS7akgLfQ17V6RjgD2mOMl%2FXQ3ZXUCG%2FlitMf6RJp3CxS0268req%2BQ%2FeOfI0WW1cHop4lRi0U60aECR3cNOieb8RqS4z97x9H225uO5B4A2PMBXfozdFVjWr40n2BuVqPqf6DsPo1ZaADHqQnjzggPJXO%2FGUOhnfT7P8w2v3nsc9u0GfUO9WoKc9ryco4FsHaa%2Fa4ADYQer4aCmHhMrsBbG8x23kiAcM%2FzmjCjzYt%2BxKt08K6GHsONLsR%2Fj97fX2Moh%2BagvxegecE4zey3shgeR1Lzcl9cBF8JRSk4P7un4WFGy19HcUCX9FtIyIJfOIvuv1YVaRJqMok0zhjxvKhT5PR4iuFp9JihlrMLJyCU0dqmcNZMlo7Q7veowegVPc76VAJ9uLITb5rzF8%2Fc6V8gOJdsUMlhcw%2B9yU1AY6pgFSrx%2BjT4JMcjXCpkUY1RbEjUSJ2CyZ9gTGxrDV1NNwIxXuZ3Amq8bj3ZZWvze%2BUZRys1jgfCXh85os0PeU1t7x%2F7oqScwSOUyPlZBe5eq2h6cPHIo0Deh6tWrzV0fPYAbJkYll9u84zufNCqgzEwP55FoEuNwodgWdvxlmYIg11NA8yWdBfLA%2FtnGw3C9DpKPZYAXGI43nGsc0rnEyCNWKqsLOSPkb&X-Amz-Signature=4ff6dac2159df08dfba756a825bc6bbb62ac03f32a93eb9aff8bb63224411226&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
