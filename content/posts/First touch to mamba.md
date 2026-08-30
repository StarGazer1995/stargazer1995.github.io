---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NNKGTNV%2F20260830%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260830T143337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBkplhWKmK8JMjEMkryrvVYwqfGzNFR2SpQ8kk52l%2BtdAiBJt4Efsq03xGNMjv2OAF7pg6e0xKd5%2BBDUUB%2F0R7qI1ir%2FAwh8EAAaDDYzNzQyMzE4MzgwNSIMlK00mX%2FDOY87XTGZKtwD84fiw%2F1Y6aMbYT7rCPj9wjYx9vOa%2BLpmOsKF9Tzv9AiUHefpfowdJ1rOkBhQQAsdwg%2F48DYOatGA4yPBXPFOLz5gb%2BP8kym7RP1bRd1ES7hF6yGNV1i%2B3RgaEpWtRBzlTwkH2zOdM2SsqP5ZDaDqzl6YgOtdVgsTI5blLNGhQ4tTZrrWgfyVcBpjoxBzzMFlGvaewr19WMZBoURD%2FC3obeSuHE%2B47N1XqfyM6GlIuAqfhVsxnH%2BYyZAawkAIurmzQSM5lDGdTyUdGLcmwdtwK7TxTmr7lsfX9wZi3cEk02Vawv7mXOru5odyPsC6e1WLkqNt7iMuIX0ZY9bj3PXIkLKBak6QpBrIgMEF0r7tjtqawGakZGK7d5ZqJaSCa2dwdPoCUcPUJNfAJwJQF4Juc5jOf9FgWDnixqPv3NoyeI%2FaYaBig%2FPfsbU5x92YLIFG5iLZ%2F1tAQ9ZUFP1nJoMm3Knzexugcmy3cjgO0sP7GWNN25Gc%2BgxXL%2B8vz8TPXd9IR8osrr9onYFfeSIpLz3dPAOcyAO%2FkY%2BFFBPKwkcMxvrTTML2Nf8fpwltCT6jYM1i3x7qRfY6%2BIJq838Sl8FNWNm9z7jHYL5JMRk8%2Bc64ebIRIDfYLiAk0cdRdKMwqozQ1AY6pgFkcc0CN77uhpzUkYCTHtemJBiXauhEmd%2F4%2Bsj1zxS8gwpjjNICBZT0bgHlgGcJ2pcz2%2Fk3fQKgIAmIcVh0H4n0n9yXV6gp3YuJUULGXpSCci19DbK2iToNVgKOgcHyjMRKhcsQgfjHk%2F%2BgP7cj5s8Rtwz%2BHun%2FDWKRweGbZK5wQ1PM5G6eGxdnpGpmR%2FXgFem1SjW1LP%2Bu1iic1B8jZV9vn2XMP9pS&X-Amz-Signature=fc5b2a00cd2ce0a3fce543eec1dd4be19b3330866c93a8c8d8129e600c4b27c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
