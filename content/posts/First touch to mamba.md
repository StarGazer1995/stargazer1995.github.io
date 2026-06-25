---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LB3CYU2%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T212113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDNcSxdHF%2B6ZILZbNBV2EZ0PO9VzOU0ma9d4di0Gm99WQIgIkD2cIaINzljq4n5r9Vd226%2BCkn2QHp%2BZctgWgf0higq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIyVsqmHdzhPUcQOjSrcA9sq8fjaQgSHwrXoBuNcF%2F5k0iZLS%2FfXJDp9fWS7KTWWodjVeCmsMqQTlZBQsiJPu456oPlNUP2Hl8W4fUk6rRT7OvV59GGmEpkVxlcNeiwgQrT4MTwujj%2B1LVB4AZ2zautKIN7YUzHVe%2Bwr0y3VXqIopWSAYZ7kugTWlm9RlMt78cONFuufJer6GCgTWRJAexh6dH0P5e1OX8eI0RqmZHzS%2B6sZgxoDWPCV8b0og09czhHxFa1pPvwifzRO4Dc1J%2BYnaQBTC5beN9YhLoXDO6ItGWc4r5%2BKwEzhonTkf461ohjnRvZB4wyAR6TLqSkWz4X1sGoCXojQOwVtC2hAXQw8K6dpI1dChmiiNzZOybVRfLdiqniE%2BXfhM99xg6Y8IDcDkn0dhFqDOIHtS3a6wddSwEPmn%2Bdwx8v5KuPzW2fPJv3vnYbwkrzMhz%2FCfySGyomzO1n8smfSZhkWx8JJyb71DPXx%2BXnp4Y%2FgtIN5zYkxsJ9l4jLHaSpwVG%2BNQHEYHW10IBSU08uQ11Z633CIzKkUKL8p3Kdpb1F9%2BKsg2BgLiERMIC3IvWKbQbNYa3%2Fj16Cusl8sqYYT8JdaUEa0IroTLm7B04mgrjripsSmGoWuzfuegI2nF6pw4srRMNiP9tEGOqUB7L7m51vPTWbdjte9WlkJpPgHaZkcrj4narPndwi2kAH%2B%2FsceTvj6rYUmQlANOXcHI6nCUoXfDu%2ByDYxgaZ%2B1hc1U%2FXWs50uXGGOgDzAV3FGkmRyaIOFbQ7%2BuEGNYoH3xXOI7W96Ml9TRYVksDfdA1LxochS4jSJzHZz9fVVqKlZJ6Wyrn0zc8ru1%2BgTzY8rptHveeAzRpOKK6ZS1jkQMWqIM3Dqw&X-Amz-Signature=1f9c49ff1e44eefbaf6c6ae65744785f5a165f433f9b8ac92534afdc3208940d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

From the perceptive of the structure of mamba, this is a discrete selective space machine that runs in linear time using linear space.

lets say, matrix A is a state space matrix for the last system status h(t). we then can calculate the next h(t+1) based on the following equation:

$$
\begin{equation}h(t) = A*h(t-1) + B*x(t)\end{equation}
$$

$$
y = C*h(t)
$$

Where B is a weight for input x(t) and C is the weight for output y.

We define A matrix in a HiPPO matrix manner.

$$
A = \begin{cases} \sqrt{(2n+1)(2k+1)} && everything-below -diagonal \\
n+1 && on-diagonal \\
0 && everything-beyond-diagonal \end{cases}
$$

By doing this, we can use SVD partition for reducing the computing demand.

$$
A=V\Lambda V^* - PQ^T = V(\Lambda - (V^*P)(V^*Q)^*)V
$$

This can be done
