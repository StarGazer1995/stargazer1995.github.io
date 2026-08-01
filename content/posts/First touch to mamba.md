---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7HMPF3D%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T185031Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIFPxDmd7jFtnhYhg6O6UXRV5wYs9wTGZMpono%2FD3QTN%2BAiB%2FlgWc2jUsxdERcgbe%2B4QxeYPdDxnvMWme1h41J7eW8CqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGf%2BxzHPtnVy2k5tJKtwDLTqguDNRh0Nugw3yZiZ3pH31B%2BbDbAGWV%2ByEqOMPJuH2ssNjCykqRDjGPPg0t%2FEESnfqiR9vQ2%2FZT%2BFJ%2FE5GqXeiNRonzVTYP58JI%2FLRN%2BD8byl5U1iDGCKfCQL1pEFKnuy%2B6MInJJh%2BstOjP1AHXjalzFuHyhvpMgLxSjZR0sJwT%2B9nKCtVbKlBsyMEbRTup5pnItc672XdxbHtMVXL%2BGm5ukNtSryIQecfiTGoNJ7wBPi610%2BTyRUVLdQ%2F%2FEc61TndRiWpT%2F8yp0zoC2gjgSJVFKqDnt%2FVOsaClgkS4L6zeW3p4EiDJUOqpFs%2FK8wedR5zxigIONDErFNCGUmxc%2B40BxH2ipBwlDs7TAlUy%2BLGP7HN0oy23%2FKgkEDZUozlqXbS3ZiCaD40Vw68VFMi5%2FniQKcUdZsb1qbmqGMmwdm%2FFqrms6wooi7%2F82%2B6aOcMWaPJz8cQV%2Fa%2F8KmlcgFJHhTcfxeYSji5T4V%2BPQFHTqVl%2F649Z76OyL3iZ2aTwJKoc2wg9RsKnlB9Jg5m0jd0lqK%2BVLLkXsemMW1hrSfHcquAF%2FhQDvPsyDc6zlGgJIhQ9Q9tmNUGXF7WZVu3%2BIzOYoMUlLm742lXo63%2By%2BoNZD6oyizrCa7nduMy0t8w%2BPW40wY6pgFGtkGdFUAKJTfxMVpDiH4MPNgnPKXKDyYJoP9e6%2BeeFMktoVcszwFxhmK5CAjGtfOd5WnKDvipdTkXHRPlKi%2FHYaEt3SMnfAhUEm8OJIPlPTXqH4f%2F58CZG1Ubp9OR2u0AQE1%2B6n%2BuuIPjjNLnnr0WQhszibOCxHD%2Fkoq7F9VNFgSEYWLO%2FcSpc0WV%2BST%2FUUxFx%2FFCOCEPnrVnBJPWfaCNuv2Dpf1V&X-Amz-Signature=1af2cc96efe03bb7612699e6d4974d94d74e0c133e4be06dde314c07262fac27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
