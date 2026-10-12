---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTSYQZAQ%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T192914Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCLVQIzwuRH7%2Fix2vkRjRJLOJuDgPJvs5dvwzTlhdEAPwIgVYuCTyewiJGySuW4yYqg1tXUMkybec5QmUrk1elT8VMqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC%2FC6s%2FQxXRjXumduSrcA0NX5bcS4%2FpaoJthVDqc%2BoUUFai7Q2%2FrjB%2F8qW1fi%2ByKWvHS1zmXIfKfD59HWE1yol050PMaflRFWNE3tKbJhVtXn%2Fr9jH2MdJq%2Fv6iU0xFxdl%2F8Cfafr7bLZxIoBTJTRG2SlbMYp4M8Tf7Ofx9spebqktDQGFbSAJcHdpzZFqGSNGHR2UBJKA6DyDG6XhjODgu3EDVJpE495RRxZ4sEnSl%2FcE0lFBzPp8oJcwCji6bX5fZwuyrpJCcVy8wUHC%2BuSui%2B0BzxGqIyA42jDtmfs%2BCK1UP8u%2B9FLm3m7aya2jrdq9KmCv45%2BmFrSjDAJhRTLehCiRhOy599uy%2FSPy%2F%2BivlvwPqG38vPG%2BfpzJyIP04NP3VGOzaZsjS9%2B3tcC%2FhFPgNwVaToxTl8W%2BExqyC4%2Fw52rGlpbde9PSjEj9%2B0oXEjk%2FuDQAEoENjcBXxFWQV57WG3xlhrqmn9Z7vIDlylHqD3Wr5Eo5EVKvt5Bfm8NkRHQ6ddh370G6IHjDmGl1plcOaA1rtnycZz%2Fz5B4dWUtVC4leOx662E02wkTSi7WNEvmnfE9R7N6fJXEuUsgSOj62k46Vzvjo%2FaHotM4FpCpVCjJJMvWvUdCg6OKkLH2t9Dw09lb0Ye73mDpX1%2BMMTntNYGOqUBqz96hDUuONXiiSEoBiSkSunCuxBz3O%2FwwM1i1gTjPh%2Bbm6nZGxc5aj4sdyrd%2FEapZvItcAKsx0KWkogipDuAbnQaMfX%2BbzdBdcvvDvB%2BSGF5BO5B3ruwcEdrUod%2Bzse3VWFE9H8kJGBNOFU2%2BIDtXdNe%2FHgbFjgYrCoIMFCgLH86Um%2BUB8kTifR5CBkt%2FyO4DySDqPkGwNr%2FJTU%2BS9x46WExUbzF&X-Amz-Signature=94c39ad7f2e2fc290d20ff2f9269c802614adf88f58b83ea4145e02e14c529b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
