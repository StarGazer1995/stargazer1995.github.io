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
cover: https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/50591284-f16a-4e30-a23d-6c56f8b07ceb/IMG_0091.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLSK2G2R%2F20260915%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260915T065340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICOsinkjOFpHnZXjdEsoIaLGgyBRbCTS2O8jFCCKAYXqAiARyX26t%2FduoQk45rHuxa1dR1M0xnLe4F53rNPE7zyVfyqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsokJrZXb9rEk0JeUKtwDujJekBjYcWdiN%2BScZR6UKywKrv08tgXWBHIx5XTC6Px0bloirNugfsfBhw2zoXqNoNP5PAEYlXotZxC62s1p2h3NuPuRC1EfUdu4po%2BgLp5Lxuq0%2B0QXsFrm9wwUnkGov3%2FVB6EubzJBN4%2B%2B1dWBfmV8TkF7E%2FCeFMtgtzlYGyKpxMJDTPrMdiQBAc2sPwPZRY5yYOqtE4cyJl6qtOynSGnqVFj%2Fd32ejq05uswSejLX00KUaambUGBfGUarB5XREhy%2BHtpwVEOFVg%2FQZRJijHBbbVfuekmAbZWkL1qgBLaF40Vk5l2vhwzWf7e0yDiqsoW4JVoXAz%2FmABNRq07fpImSHVeicumiw%2BSI7GwpWljFGBZISDEn4kDEaj3KdJuHt1Wqv9SUABQNBte%2FXq1%2FHnSlEVV6CcqLFHraeb6PVqXQtx1%2B83h7TKsATbdXgMXlIgyLPLwkvzcjKljml0lgcwEBDykuIWwnzzGgSIu945KIdA9u%2FFQUJROgv8ECYkSOweXMPcKHoXSHL235cZ9Yog8iVACOdlc02tNWeMCGhg2WwCUnRgk%2B2H7RsS0t3%2Bu0GK%2BOZ32EQUXHc%2FFjzKCEPBZjL5TbF7UDGeGWpMNwm8ZSOSlzaXtE%2BWEWRxAw7q6j1QY6pgGVVyymxkdgIgGYoTb6B15PIA0vMzrjndpXqzE6bYOiOyO%2FjBv7Pz%2FzP47fZSKHi%2F1uPsrDnJY5jVqwBy1BFTGyJB18VhAe2YbcoBTDxWPs5Mzifdy7D3Fv95AxDGPfJhlkPleY%2BjxaGSGMPlqiGOu8V8RcHvPAtCrbWc5h4tXQHC9jgJ7o0acEF9mahInE2T75m86Q9HRm0Md742t784MK%2FcQG1x7U&X-Amz-Signature=07cfdd54d3ce0702675119bc6cee49b90909c0b37b5074c2a6276d41509858a2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject
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
