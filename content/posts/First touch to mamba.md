---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667K3QZ7T3%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T165104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8KuGnDU3VIuIHCX5MKkTM3afoKnMcpZfsGL7RWk0ezAIgLfuMmmnYf3%2BdxWW5eYihrAb%2FJlKFtSM3MAMq%2FQuXvckqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFnvD%2FYM%2BZMkGRzPZCrcAxtRLTQhcjqUtRm74LRd3E%2FJ1js%2BWSEUwPFOBYzzSEI8zUm%2FmJg7%2FTVv3eYRpQZDG%2Bu%2B74fiAQgpD1J0OW%2B%2Ffa%2FuB4aK8ac98jFvqMf8BGistoN09mOS0X1NCXxJWaR0r0ZPhu37LpKg9axqqKhaOqVExevIMkuzg2cl%2FT7NxjFeeluzXjK2JwDTJgm3UE5ZhGD0wjiia621nWvIiCK58BhNEyVWVvvZ%2FviI8lzDNeZwOvVGsCaKyiE6zqXzzWMkA32eYriWXaFDs4ldLyyQKDaMW5gi3qJbnckf%2BOlZxH6lSQH8j%2BVssz2DIicKBTyzzeEIVNN3ZH7DxBLrHwLgZ4G8pG4gD%2F%2BDdFNk%2Bz6BDW%2FRdD4ZjDzZOt%2FA0qpYn4B5iKixgME%2Fp0GJjn3WK%2BvD38G%2Bk1XVt0QMiD%2BWY9r4Jj%2BGX7akpK4aSbH57GolTaJ3rJ5u8BXlrlqmO7Wtt%2FvqCxZb1oSt3P0O6Fv%2FdA4vK64cus8xrYyExPUegpFMziaLn7r5VY9vIG6omt3O2m4wVZ33cb0AigshQh0aKJYM071xvaNvFyGoTODHe8HVYoTq8kAIvWtQQgZDjgsx349Zfu%2FiuHyUevDg0rTyh3cgWbUsMfdllaI4G1uSsylaMPex0NEGOqUBcKt%2BWmfx3BsktigsxRAjJ%2BoJoWQh8pmSeRDEj%2FOae3tPMLpDYxYwnDtEDH6IRLRZCdYui9j5BGZTqciIzEGBluDOn4ciQYuXG9FlA8OGEdm9XCKHc27UzAxf0g%2FEQH83ZENYiJyBOSj0UESJf8IHlfn7iweIRfPXd8CfPZH0CIZQuYho5AjPGnbvkfu8ouYU4aGuaMQXK4V7wRsP51tIeNJS3fSw&X-Amz-Signature=04a55c2c12614cba2a7874c299ca5ebbd2ad51142b453aa7ba4c12fc37fcf2e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
