---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZ7WVAWE%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T020546Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQDVmlhEfgff%2FfJjlD%2FjVN0pgO9Pcb%2FnialBtzjfJRud9AIhAKB%2B14FRPS7fq5n27tJWo%2Fc0IMKFGTWoNhHgeBziDTDiKv8DCCMQABoMNjM3NDIzMTgzODA1IgxRC68IVOrBAHioWIoq3APutsj2fooCayCcNHRo02ssubv1nKyij4SmPowlu7yXT%2BxmyGH1rYoWdanq0wOVTGRTjKOLYgfU3PiHD5yZorjSSoQz%2FvB9liUATIMEPyLkMeU2l6%2FY9Gx428RTyqpucOvLhxW6oP3b7qsnH6Z%2BmY9lUxl7MtAO4t%2Bhtpuqqr1qo0Yg1f3gPFQMwTlSpB9SJ3pdVLkKY1cRWtF5ztE9fndIa91o3v1A76s%2BR0b9OjOSOkDi8l79fSG0VNB4WGNlOEECm3kUT2bCpfzHWz4%2B%2BsyS0UtUCzjyfIr144%2B66t6j%2FXMjv8RrD2yi6OUcLsYpZl%2BalIrtLJBlr5bcSw7aBYeSDob5FKgBYyk22uzpTyRLHZPp9o1Mw2URgFvom1O%2B3PnZpkvsJbqb8LfKmsc1HCBD5oRB9uGPFZ6yfhl4UFIB%2FQ71%2Ftv99DNrqbkQHqjXImIMelgE%2F%2FuUcPdFBArCqckw%2FndSrg%2FcTMmZZmTXk7tP21wF7HL5oLCJKb9GRShAXR4maerkIcHZxve2SaX6fRlYVObQ0jLx48MKv%2F27HAwtxDGWj6yr5ker5iwvJ9nqXw3Mzx%2Bz2aFjughGMwGE0tfDGzzWtybyRsRk8VqL%2FhMj3RINj54%2FTkTal7pekTDEhK3VBjqkAcV3MniBveCGhkhlHbSB2cHn1zDhLWt2eQDTVx2hURhuDI%2FoNIsjoKBqaZ%2Fkkj%2F3LBdKsLno8TXTs%2FT1oiFR8Xwuj6MEYRjGDUlA92sBidJfk2N2Yy5tbRlddfTvt2Bls1fte9z07VfYZWRQGobWacCsPwxPXk%2Fq2eVX8y8ZuhhiyDlNiJ2Wmvli9hgXlBum8HyvzRI74or3aOmzwLjLhX2SS0z4&X-Amz-Signature=c064409a184bd494778956bd218a474b807eec98ee39dee9c15e03c907ad6e39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
