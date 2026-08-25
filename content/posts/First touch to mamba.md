---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RYWSWTE%2F20260825%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260825T182555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDWzALdPUwWkEvea3%2FYEGdPlXqFpWe1B7JukQolFT3TuwIhAP9%2FcpY9F02g9cRnJAxp%2FjmJ34wYK91if0IDhciZQH%2FwKv8DCAoQABoMNjM3NDIzMTgzODA1Igxg%2FSwqnvWwNd5uHT0q3AOcMyBSAdUhLd%2B8I7nGt4PjxiTqvbrl4NePByd6a1%2Ba%2FmZoucsWkWa96xKF01KDup7dd%2BJtNhzhwYiIn8hm3FOooB49En4rLNK353%2FN%2BEmNEOBWDswsX%2BUIH26%2F7yikVJvaEdkuE2gEGejXeQe0GAYLarAZ7BmxjcuushK9uJFGvVNt9BgbtT4ZBzClBSOvKAPooKMxJPEd3NUEUYLQhu974MUIrKPHdq1wMyr7hBquoTWr9aV1B8Q7Ev1yUHt8hc1iUq33FJUua9QeKAt7soRFC0Rn4basfkbumXGiieuxHFPNPs5yXXwPs1L7go3vl%2Flr%2B36%2BbKGCuhhenj5bA6MZJyBYqUCraIjnMRy250Ni4FqOWF032AYMAtoJX01wmop0z%2BVxAHS0%2FF0V%2BdqC8B2%2B3PtZuf5%2FZGJxysCSBszLDTIjdsPnP16r1V34MD%2FC3iIywXwgMVL2bdOVWuakHllw3jElsI4tzt0%2FIzeJtu43maGim8RDybCJePfClyszB97oKxz4RAhm%2F9TgL1erLfA%2Bspep3PJrQaGa7E7IMJEq5aOxDJfByAMbb8ME380cQfBcPO3%2BSkqFlVVDR5WwLuM1vWzwQApmgFiWyXRRfkyJGKXtqAy7IqUBkrTkVDCDk7fUBjqkAVpgK8tOY%2BwmugaQTZE7Dr8xIoo%2FNIKQvJC%2FmgEn7DaysanQdC3psKOWRkvUyjFlrsA3%2FI5Ps7MfC0OgCoyWc1zz7jzmylwLGYFycyGvJ8T8ZNETYjYqTmZn9AYX%2FZeZWQ8xJsUlMIQ66HEoMSBQV8S9Q0TVOtsggOF%2Bs01dDecNhJELNzZoeSkWbe8XDu%2FTqAdCM9OwGVlBCSUxuMinrzdJmAt%2B&X-Amz-Signature=b63b2bb85cd839a6326d8701f0cee0923705b0070047799ea40b6afe5c0673e7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
