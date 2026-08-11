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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466THSA7ABY%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T004800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDz2ok%2F%2BTEFOSlThl2HxYo8I6nYnkb8BT5ZBeFD2pYqhAiEA8FqZa3A%2FteMT16FbhF%2BAjayEzERDCctTo8prIMDv%2B2kqiAQIqv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBf16SvYj3zG6GsA0SrcA7ITj0tqUDZhf7U9XxkoLXuDnqg8t75s9LSZ9kRlEPIqz5Gt5VnFREQBUEUniw4%2BApFYcZXcE5b3mckWSbR33rvc4P72mztNztOvV8Pa%2BoVesXW73nxGLtKpmXs%2BAHWYREj2t%2BjQ7qftcN7ZURgBQHqzbqI8fWKc7aRLZ6imebMPgOwJmNSQwCA2dMwizUeaPBVVfHOK%2FzmRx%2BfYeXjD7VjcP6%2FKr9DvkH4zJbfBVrmvkKhBhVzu3tSD4cafw2zKmZAs7NF%2Bow5WgrSjFv7vVrCqznHv0i3XdfarS2dQjO3t7RfHqX7rOQrv2G3F1P9SZCRxt7JqbZJp7uP9DTQMBnMSDat0WGXYi777d53vjywD6EREaQB9ZoUWzJFpjaVdY2HBYvRRQSutOJLAp5LhQTF3ffm%2FLOGNpBsp8BjKBCPrHkP2smva6f%2FsI7yb9xquo1Uq5NH5M5CHS%2FLIoKfV9cKjwDFulGCtm2Bi59zm%2FL8jKUfA5ZkIWeqeHem5Wvou9xPXaXGfytVKqxeBS%2FoUmrjA%2Fl6pcEujsU6wK2%2BQuJpvtq%2BZiY4aF8Qp2zbrGNN9YCqwsVFCV8reeShNFQUFCG3hg2bqIAJvTaJO%2BWeXrLUgsRsjOdWBIPD43NQiMLHa6dMGOqUBWSOHmKzI%2F2CQkcmhP0An%2Bq6m%2Ff2jijsTzrK5A7it3zkxrI7iPsawZG6%2FZU79mJB5vA1j5iupl4Fsd4t3CTi4N7ONdkP9705VCHcueHeM1KRpIuH35kK6OP7%2B9AOfSSesv3EaV4Txkxs5t2WLzkScVNXPweYXttEq7QCAHAbkfh%2BjWbz5%2F6csUTWgKwj4GcoCbLedg5FDbvUBn9qp4J7MUq5Gp%2B%2Bc&X-Amz-Signature=f85210797892edeb26d456b4ea7d77113efd7586ffa7b8512aa9cfe893df38a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
