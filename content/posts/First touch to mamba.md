---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJKXC47D%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T054105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCgBmyZypB4tGwxHJQPEITasFwHNCCE982tf5QpkViXRgIhAOZxcVb0gH6PEdbCFmXTbOdVzfsfPzzhyzaN4vrSe3zWKv8DCD4QABoMNjM3NDIzMTgzODA1IgyAWjNcrL4Q6yTTgmEq3AMoZidxULMaKyLKd0yR5d0E87mdMsHV89YG22fnK%2Fbn%2Bn%2B6okJPQ8Ymtf%2FrzBM3zZodpA2qp25RhJ0Sl8SPLzYwRiX4byDymgUW0%2BGMlTBOyuY%2FGHUgcUrp2kWYSV0TS8pTMXNGh5VlTB5CHt46WJZWf5zkDMW4bxqi8yDXpn62jdauwPHdoGyaptVqOwjFENGiLVeJ%2BYWT0eD%2B69lgOKTjbfwcgJl73yrewvy4tKF2yTMvgi1X1Ct3xyIvCKyYks8Yba40TGEM7wXY8sxbMksiEqXce8B2ahO67DYsjzsrfktOqIdjAjbk3D9XHoc%2FMsB1kkPjztFUFXZHXS87QET4QLqfvW5e0pV67VmLJ39AyVnDu%2FfAhpQ6%2Fv8WTpOBQvNg3we3ksiasj7LHMVJrQGk2070nqmI3U%2Bxg3bG4YS%2B%2Bgk73hfCwoZZnLNYOlRFFpidIuhUPduP7t%2FA7nnQLA6AHZqyd43U2%2F5Yx6tpnl0PKOx%2BejO0u8126OgPfuYZd5ragPn7sq%2Be7zYvfpFwhVfWdP%2BqyI3OnjHgd2nTWwppkK7h0ly96X5K8czvL9NyKJxCYVtf%2B6uGItU4JCsjovkNelUMH5Ssp%2BwOvudZIcIUvcWNp1tZzvO2LsHzeDCkh5DQBjqkAetxAq18y7s4uMjpzfUmu2Mb22GUjKSdykjsfF2VuD8KuP7J7C5iAaJNeudvQywKl%2F0QsPLDak0Lgd6Fhs6nsw%2FIZiewNJzPUdxxgag64D9J6yA7ldoa%2Bm7RgG63XIWAIuIt1afctC9qKeBENs9QoDu2NCZJ1oxNYKLZeBgLYCiI5t8hJW55Jo8b9CNWAdnHQA2VQapB4mK7s4J0aj4fThroGEx9&X-Amz-Signature=2b80dc0bb6d16f821bdc3145660a786bf2f2eda698041efc99772a00eb72c2ba&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
