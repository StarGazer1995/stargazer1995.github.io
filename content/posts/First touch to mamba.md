---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC54TH4F%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T185141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHkl0FVinkWI6XbG88AauaPtDL6IgBt6UZZPIIevDkAQAiBlYbeWyUSiQCbl%2B9gOKonjFu6wEorMj8483s2ZsoclYSqIBAiE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJubYnenoIkDWdejQKtwDoh0QL7Xyh4B1j7wgXccpqsN5hvGrUis9W%2Fmh9XaftfBc5zU1Al4fDGwEDqX3hG0g64P%2BIqpjTGjBzK%2B15XJVs49JMMw9t6fWqVOkbK%2Fc9RhJyqLspLEcagHdNtxGoQoynabl7%2Fls30aSViRYbDtOOePYpdj0FsGqrNP%2BZOpDbbZ0DpRgnbjnqrRh5XxtsGGmuHKab6p%2FSyLstWyTeNhGwfVXr%2FjRx4kcbdZyCMs0VvoMDycr0hecPMTLB1RdcoyHCYySrA1C%2BjFkGQ36Tf9U1ajXLXA3bK1auvQrCiF1cwPKl19T7NpM8qk8uPS8Ragt%2BCcJ82GkXmRioOM8TnL4b4oJVThPI7jciEamBUugXi5U2bKkjBiMkvrmXDC5TGBdIMlHhjJVYGZsDyouqvUOiSTm8UOnv1aboDyPcNFEiL%2FF3vwkojvjKTyalPgoR0UTxD4AqRQQmYzTPlQU%2FYOa25GjTTW%2FAd4b1PL9HGTQ2j1HSev8a0xtpnUhDG%2BZx066TR6g3myCSq8RsaOqxkR43rR4nHg9WoqpZSWa8Ax31hkk4rcFojmrwZdKUt9XTfsrrt3DRuRUMvo0o6y5evM4Cwp%2BwRQM7%2FBuRPiIcA9Nge4QFAYNNJEoYSFO7R4wt4up0wY6pgFjhYAg0npKj%2BbQnyxJKRQbSfSDyBQt4cPWawKyZdDoG5F4pHdGLMbJU47Xr7zNoTj5288VGebQ2jDshdEJei5S%2F92p0D%2FBX9zvvxXNooWSzQUxHod3eYE14KHeJ0aR%2BO4Qmn5Fm4u29nlBgfYN4SOVZIy0J5t0%2BDgCCZal9a96WBRyTLdPQ%2FsAQQCo1KZfzhosGJl3cCv37iXF5xa12gj9v3wCxfYV&X-Amz-Signature=a1f5f7ba5dacbd2b2b207a9c3dea1e14402cb846cac3300ef7ea295c8313854f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
