---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIJTNV46%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T125636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi8sHhdbfQM8PHN8Pg2VO%2FBRlUmLjMB6VeG5xKoGUAKAIgTKTQX%2F2WCIkfCv%2FFy%2BrplY%2ByXeR%2BYZshx%2B3nsZuuEUIq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEJ4skZj27uoqPQmEyrcA4wJQP3JAPfUNAwDIYxeWkt0Y9PUyOhelHI2luJMyB9AuaQpA%2BjBEdr%2Bn4MpRjw8YJ9FOO7kcu4De29aWwrXfA%2FwRtuRXeyJwqU33ObdVjFRRaVxEv44oenMbhP3Th7pkZEFXwkJ%2Bjjt8hQbu4j32kRDUMzNnqFpBCBZw6R3vsaEXRBMNgxpwRFXHgTzQ0Q8%2BfNH7VLR1DQ6W5n573hYSg4mOC2WCju2Eym0%2FPaaZMt%2BeAZnxhEUhSbbU11V9Y0eFwUDnvUEh6d5AlH%2FowT2wVCRUODsZUeQyXrgWpusGTRXPU8FgmuVt9vPbG7sTmOYf6AUw%2F%2BZ3N%2B38KHqLYxOtO7wgMAtfR3yx5Cx3oSZ2wRQRpTmlEP3Ll1EuAFCYATxF0v0uEKG%2Bz26xnXTVvFVaTgZY1637GCTAdBw9SEWhn5thq0jr2GTSJzZ3z6yK7%2B%2F3TAUgrVBxBYxbFCVwzrj8k2eqHEWxLT0yBB3oROUahtMwIp4bPffyUV1HPUmjV7QLRluPI8nOAXbYjtZfBoPlpk5WkpAQBphuFGK755M1IcxR6%2FAmMz57xjNrUCw%2FYyAE3TkO6MGMZnp9WdDOsQEkdNiqciiIdCKXxOvyfXF7bTb9jpspL0Skj13bajDMKnrytAGOqUBySlcNn9AI4oNkxfiofj%2Bd%2FCZQcrGNnADsiuahzt1S7AAgVbySmMgSNllvUgJBlYnUncxVc7dKon%2Be%2FU9vQQtAjNQbca469csArBNY%2FYS3AdFwajfrfAxKu3x4XfCaA6BdG%2BCBtTLC5GkIkbKRTi5168S9xM%2FP3GZayu0uKUS0As3lyjd0IGr9r6SKGgtU45gZfPvym7sp6ETbewyllQYKm7h0zko&X-Amz-Signature=b60b113e62abaa70f0f023b6c80bd83df4be166c39df0b75b81935d6b91323c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
