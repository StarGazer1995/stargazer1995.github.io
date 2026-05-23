---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFXHFW6Y%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T185308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG4aCXVzLXdlc3QtMiJHMEUCIQCkL8PqGe9IK6Lx6v1cj%2FHAMZ2s6Pz0x1a7uSP1zsga5QIgTkGMtisSuouVFWAmdfR23mkShvaIMCA8lAOUUxN1ORYq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDElvPZ6rqKv1fZe42yrcA32TblTiDGcKNZUOTfW%2FUu0x1YGEKEHV5isByfS1FdYsS8I9BHdS6GB04ajsqoV4znZeyaI4ylLFyWieiYFzYzXvr1RdxbO1g0CLpgHmcCeg1jvWayCiRSWOQxF4E59bgX5tXOaT5jft3IAuuIe88EDWwC9dpqf2J%2BMg6sKQYuNZywszItrIUxuC9YARkmbc%2BQsHsXqzFfERUaQkD6Jv1RWEZZszfkYswmerb%2FH9kagg9CrwnJLBTqpiXrr8SoC%2FyWLlbvMJ8m5jv3veXt7c9kt9GuOykSPNFbIxthpzpoxuOEjzH1fW6ccZVBeQGOGxq%2BAAUlY1dnZPcDhEaDo25NvkuzV8o7g2TgO91DM3HktuWVTeOjvbQjTQIgM3HALADLm0nVxKPwrasrM0Rz7XevFT6cnOI58OcVabcm0icViJS2CfXmnhO6h%2BE7Wh90p8AEW%2BY7iMc%2BtKph%2FsiQf9%2F%2BHDvcIjuQrxQLzovZG4SaPaHqYLPaqg1Yd0nzUEVCpBFtxuGyQKzPVCEsKqB1ctBkK0TIXk3EGhcuHkP2nxQQo4FDTREX%2FWBa%2FPExaY6hdYhnp1jCzLs2S%2BXM8MUuurvazAqTaIl8fidEXd9Y%2BeiGkZsssZidZIKuAVkJxdMODWxtAGOqUBA75TmuMiCza%2B1rfbH4ft4eRD32C%2BQc3bZa3PeKET7KP%2F0xxry0lfBFRIoN8ZZMAymIYCDJO4PMzdEszmaxLg%2B%2F9IercoxqWeF2mGWWj0pwNT4wZ0T1wlN3QZ%2FVkkiedHdC6mOR9XxEdR%2FjMZwUZXY2H8KQzDO7jvsuPLz6ty7HoFIqkMRzS367AfeTO99V2VfEuwrZcCx%2F6OU4Uv9sl0KTFm7Ijp&X-Amz-Signature=a01ff4e1d86530173ec435ba8f0748b01bb1167725b5cb63d804ca984ed2d3e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
