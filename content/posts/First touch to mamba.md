---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNNJGUUZ%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T234457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD9%2B3soSiTK1dqnJ%2FywTmZ9i%2Byu9ywkUUCmWm3LCFF7ywIhAIkBlEhMHB2ouAE8zpAXvKnQFicVG4NaG34ZO%2FvTk3IXKv8DCGAQABoMNjM3NDIzMTgzODA1IgyW%2FvP%2F2xe5zvNYLkoq3AP%2B7RPsNNKSkgA74fvNu7uqZcQVIF%2BY6U2odmnBm6BXBXvbyrP7cMcK2fhztlXgNDIhdbQsjTsC02FnZGoZc3MvgecpRwzFzV6UMvRVQRgb8wwe3qiCbevK6XUH4%2BkfEIZyTfBGdN0LfRtgeSJx5dA%2FYaffFhEZof5xNf%2BOh4FXTdy4hcXJYzx9LaEqv5Csu2h8vmLJvbe4c9mPn5ZdshK8nAzg%2BVEMUrx48p3xuF6%2FFG1ZMNK%2BUghdCSZV8%2BsVI1hvBFU%2FZnsa3ch1gt3Ukwi6mJhaWb%2F35n8Uv8GkKMdoe6%2BU2GwrPKuk6L08NSQhCiOUmaN5sD5e1l%2Ffl0jz5PfRsj3z2znLPseZ7RomOJije%2Boscg3lWiCvG5lj0YY2uPreNudmL97N4KrAz3yqOlMpdP96gJ2W9Natz3AUMKq4MT0kwzIjx%2FjwPbtWZarAE2vOLdI2%2B%2BCxoBqO%2F6cpr6AjL%2BYETLFNuLyJYYjfPpc9BdbGlGLrNBaGANmz1V%2BdhnaMI9oyno1h1DoD1lf%2BeunLD1cFrG9GoY0S8DmoZVIoOoRtal2c%2F1QjRgzA3ks9GlZaERLJiuhhF%2BY3SuryIVVq0TjdcBJ2ay8LZpp9oJQG8x%2BUGQLRz%2BMSswtozjD9o4LVBjqkAbal93z1tO7b9K36E3Jujy9G91eGYXyythauGaRG7R%2BeziUZipPZqJuKa5YVTMag%2FK7Z1C4dA3fDFwsO%2FNzphk1dLVcYzMUZ0fSv6MWMJ3KnT9UclBb%2BsMSaB%2BpXRkGswE2HXOoVO8FHGPWNy81ltdXHzz6b7p3kJukwBuVYOrOiRdJQDRbE58SHKsVdX2FTVhiv%2BmjKa9qY2nxwr44bDAR2tjwi&X-Amz-Signature=7e988e2c12a145fe5360881776bc1a931d0a70f1daa69f8e33a8844f34ed7480&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
