---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6PKFRAV%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T201049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHeRuHXfvyG54HJzkf%2BMCtMNLvbfvvK1zGy9UaHtV9e%2BAiEAuc%2B4Bb2qiakdIwtbF92oVgvmbFvXvEI3JvtGlmvwUYIqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCVVOjY6CyznPT5OXircAwGoC0j4o%2F4UVqnhX5o%2BZ%2BeoJlrH4wjZjCwynsfMCGiUxuD2DPYvKE6mn7xg4IlvNGHm44O61PEhCtnuU1zJLVXqKY%2BKUOCsSpH9G%2BJHHrUZtDX6O8tInh%2FHpW7bK6KA9iJq5kQI0Fl%2FaO8TlEvGiZ9k6FrcpCXgFmTjuUw5VRu0hs9I48Np0bzxaeVjVqW49sd3JJOPJSTsN33sThBuTd5C%2BEDvD8sqc95vqBtLYMZbYlIz6XW2U6jTndfz5rG%2Fi0IBgGw%2BZCFVA9gbsKOrnFPCPKC29415VSFexTNoF3bwejTbyPDbvu8pG1nWc73xc7EYnNOjs8Rp3AlwDB8jr4RWW9ZqyJh8Qt6siJ291FkwC3xw5L8F8srP9VhXF%2FAU4%2Ba97ROZZuaI%2BvakFSMa267oZSBPuSdWBl5F93n3DJyBkkBKn1MqNkf2wVm%2F97nE9HdJaau5CrIPxwZSa2X7EuiiEifrNS5gMHTO7IGH9gKWSuz%2F0ldRjgInUpVFFKX1v41mGnFS3Rq6lIuXUYWhRCnzBKvL%2FVXDKwHWcPjGFuSFAjiYNaOIzd9IgRsG3cW1fCeFNr22nrQ4egyChDDJnczhWDKTyOGVboOFlV24bgNldTC36%2B%2FxfkeNtM2kMOf%2Fi9UGOqUB6hPzfVz3Ruc0%2FVxUDYoeHbZXbBdAt9wDzL1%2F7j58gytCV77EmgSf8H0bRPVjWtuWR0arOrfie5d4mB8lqwaqQOG7UDUV5pIInpquZ6QMKvSSwRhHyB2gaJ7ZE069IDsPy0SdJQttwUGALatnLv2X0H1vPARNMwmNmpPL5akqh2pbb22XcMxBQVR%2F9X5FQpA09m2TgCYgEGXTaaQIfVS1isRUV0lV&X-Amz-Signature=9f10ab9fca64623da05b2f42319affd2dc78b3486f82f72c944d129c6ccdfc68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
