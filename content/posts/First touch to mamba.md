---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624V5ASEO%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T102122Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQCjmB2ABFC6rOg%2BG0urVl1fE2dbOxFyhEqX62NvDFlYpQIhAMvrjXuXMxnijvhQwN6QJsQptXdN5SaUm8%2Bx5AgEIjkHKv8DCCoQABoMNjM3NDIzMTgzODA1Igzl4nGPgdJxae06BGwq3APAV3j%2FjGyhQBTWelgkgyZ0UIp8pIv33Z7hA4HhM%2BBT08GVG2yCCfe9dTJSkGzZ471YJpyO8SpyoM7ZHEWVeVvd4PufDy9pR2%2BY1XLa3og39FiuDomroy2uf6dbRN7MWmAm0%2Fu1w%2Bzn5to%2B5ZXAbQmX30xXGVgeU%2F%2BUCcJ2FMDYKAF6OlECsVvDn%2BoIBVVnivAWAkYwbnIPiI9pExpZNRUT6LtNeTKJ1XoE53tmZHJgtZsVSt%2B9ggrNiP%2B4h3SEXmD9YKyWtkeNAKyByxsYndwFEy7n6MQA4RHZmDzGX5efMXuD3oe9OlvUEQM3UyaTZMHZQo3DXoKVswxjHdhehXzsOMA%2B6MLY1x8ziJCz1Nz5%2FvrDqra1EaRjwAJeIZFvs5nOHslIG%2BnktZs750BrAc47Z6FCHQjhfvjRcQLldKJ8P7%2B8zJXwknMaGIWSCoeBFAGoUXI5CdVzo9iZ%2BMbg7gxAj1CbJ4KSjBs%2B7MyfYkO0W5WISLpr53GrnkXkqj%2BeZGLvBG936qth%2Bp2i4Pz9X29ZeakEUi2RDH63B87ETAEKCyZ6HK975oHjQXBLtQDKYiyeMKf6NZGFor4b3r86rlKKAypfvNfneOM0BX84XAA6w4hOg%2FOiFd7D3KeYWDCzxrTRBjqkAag2vbgJRpN2I9umSnVKruzQiijotkedr%2FyYKJV2pJlECeR0sXvUCQkA%2BMpTlIDud8pigxrIJMEktF6aRFCnFUyYVlNvMhBq3AOYyKWf5wgRJIzLy%2B5qDQrSwjC0lveFHqO6RLV4K11z1onWvWJWyghHd4iGfyAG3y5iutQzj7Og5rx0GNcT%2B%2BnN%2FgT4r9RmWb7ukTaSJlSb%2BvgR2%2BF32tE4ZBHM&X-Amz-Signature=58450287ecbfc2ad8024a792462cc02f42ae9f0c1d9253ed1353d4072e218a13&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
