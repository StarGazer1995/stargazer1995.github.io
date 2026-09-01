---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBVJSQIT%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T233854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE0LDEK7FyPWcfycbk%2FTwv4JTmQCiWW7%2BLnEIC3W3gljAiEAxfWHONqoLmdBJNNJvXDxqR2OT%2FC19np5RNMY2%2FFW7IgqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCjuVGpk3QPALV2KSrcA9ajJISobL89uazT7mjVyoTpbqvBWJLpWh6lyOGFdJ15CZyYYj0c2Xs7Lhfp8hmJIWzE3Cv%2BzDijJcOUFJFS5Vu6Ne4EOHTGJBiTJRhZsXhbhhJ%2BHT6DP2DrZtQgrmuncivIatr28mpPDH5FkC686pOTZ%2FjcJlTvzZ6jyJum9SB3c2h98yH8%2F2JBR7up77q6uyOlrkE2hTGDC%2B3MvVLs2vw8aEiQ9mgMnv4jkUjjgiotWAMpAJ03GHlxoLbEGtd9%2BjlA9e0Sx%2FAYSRozJZF5yUntYB3jLhOAMartlTt5G7yT0JczVJIl6MkMJm7LHzVw6aiMVwV213TtvUvFrVr8dD6AHEeWTLyuMxbMmIcnsGGGXe8y7Iq153CPCDhSvt6q8%2BfFsX%2Fm%2FrHqBW9G6uDBRMaUe8FUcRXBw6NbqH%2B9MRlgzr9MlzAhUv7GQeqqXf1bDN8zgBObqnmHZQENyKGYMfYD1opKBI0roBxae4zEiH9fVq6%2B%2FjT7Al%2BCVz54sP11LKXHzrbAl%2Bvh0mZb6KmnzGwNNWORANSRhFiZz4%2BEyekeQyXdksPPYD1%2F3MEXUIxwln1B%2FAb1YDKcHTd89dgyR4kwrY%2Ff%2F%2Ba%2FGMzqrqSyiRHxXb2%2F5laAxY2BvYSBMLOa3dQGOqUBUDrRpzaXw4edVu5Wumxg43d32Ek5Wjuk4NAKY3rjGaFJCyOX4JssmXn4MDF%2BbZ26NT2Ws1BXwx8QRNRpe4KFWWzSnqiiFAml2eu1AanoKJYrVB5AJIzIKFYWuP2ZS9Yp%2FSup2YMZIE8NYk8atQqjLO3aZ8FlcKrORVdMhWjtMmHNiCBo15vkgQnm2hP5%2FY9i8oan80KGRO%2FEJRgg%2BPJm0ytQjYbO&X-Amz-Signature=697d786e681855d0b21666c57cd6d3aaac4317445771e68846706ccf0e941059&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
