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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZ4VJ5LT%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T063459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJHMEUCIQCsr1Tlh%2FTAXW4Qbf6IyKnZYSUuQOFyMYh1LOMzegjnDAIgQplRW7uHcM7OMSSf4kItq2Ao2aNpxO%2Bw99eEUKhYG%2FAqiAQI3v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ2hZE2gLLQQKLPDsircA3HlSl5qpseC5kdPEQLapGDvgC6joSOhxnPDxRjbVA4GlO64agsV0kKEzbaKrQhsp%2Fu2O1efa%2BXyXs9U6DIQmNJmCN3%2BxwMaO9K39z%2BoKrUiS2fyXFxTfDW0GEpwev5VdlzBXzot01%2B4jYYOWB4MDBTh5ndkg2favTGtrsoiGpsWlgDvXPnZYQwsZD5CAinCLD1VY%2BmEa%2Bo%2FAA8cexazhvUnXlsswKrAY0DsW614x6%2BHoZErrl2XBE6spuXdA4ln04Rqj81t1ztF%2BB7CeAuDe9GrOIf3i%2FpWY3mmvCCh4G2Zg9Qq9nm3hiY9Ie5FJ%2FwEKAA0bwdfe6KXa1v3%2BanQ8Q5AbFP5bV5y5%2FFAcTDQPJtJg51CkcWuE1b6sT7sQz69vZXy%2BdSXWfXduYDj92%2FIoaC8jNKdtiCdeWXZZHJ4teWnvOw9kwn7zOksCH9vgt2%2B0Xxk6BokqfR6HZt8KXxVhOHb61qkCbieaor47BAdhZLL717%2Bkj8f60sc0g2yI0yaZq71lf9vszCz1vV0FF08392rodGi6oZ9sqUmo5sq55GM%2FCrjEM%2FevfyqXMXwwqKAspWlDP8v8OoGY9%2BZooSTBDmSFgBYOBL9ZzCHdViIYRROYvFhFNlCFvllr9aMMKjXxtYGOqUBlCWJGfz93N26nHl%2FfxFt78oFx2v%2FwWzHGweMlyBqoQfhzRJJUMV9%2B9TGk0T7ynHoM3I9l28cnFQTGYK4V3TrGnQQqgUG85TSrPvk3vCi6B5OmL%2B7eCSwa0MW37PqH7hIrQSBlm3iK2n5rh4xjF0waqV2ZKwrPzkfl8eq%2BddVZ8z%2BhTLu0akjE3gv4NxjBc1cjGYwGgfOvxcDNvdZOk53IRMQmuWQ&X-Amz-Signature=f7dd8d4460711f109df784bfa2c453afd557bdd4a7ed19107507269308915c88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
