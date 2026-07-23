---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662ICRL2MB%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T185706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQCFroxozUyRtoGVWbD0EwrMwTyqh5SG4yPlxXjGQu8VSwIgGjLIHqYsqhy1is9WGnKWI2E7ZMg8uDZ4TXvUkhKwu%2FYqiAQI8v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwGjAPH%2Bb%2BIjS362SrcAyABnsBFPbUApMc4%2BJ74nHoOREo1zlfnvqy%2Fy%2B5k%2B1o4uEP2AwwH8IeyTcCN3q5uoVeRCSArGItsf47mzNyKn7xm1DvyxAwGqH%2Bx0N2SkrTUKHGf2%2FzxvWSQNOoQXezbjqG5XX1aFPJeg0yXjiGC%2Fo2OxRb8EwJkllDg3FCqsg%2BYJ8qMXgHVCQXF6nQtiej6zzDEsZsaITRV4U0nrbald3wm9lEhg%2BpzVApJQM2GTh3dLrtcJu7DlHIOcUJjHL5zVfsdQLTuDKnCYLC6IwaEYL4wcaZEyZhoRarkY5wvVa00n5XJeL2SD%2BWyHv52wHsQ4f%2Bn01e2IjPCcc%2Fqxv8aesytbPdQWDDMZ4hXvTZ0KdfqbwcP2wDgo8E2Ica43Fo%2BR2HRAIqcqzW2iF8QVK7vdYmMoTnvp9GPx9IvM%2BBnoDfkqNjETh%2B0akk4cTKtQQ6gYDkcknJB1cvl%2F2f%2BsZvne5QIAolQGsWSRaX%2FxRdKSmABltUeRcB4UNeexd7Y5s0aHB6yT7hOCNKN3opNooRLy9HGjhcW%2Bz68OGU8NF%2F4VW%2FmAqUiNYSUMKL1HSDvtNTSUDxYU8TTEai6L7HEEUvQiCzubUjL5GwoTUuZNolO8oRE%2Frl0iwWI0v4XQYHpMImMidMGOqUBZvemB3y42bHZbXOPlC677BruD3jmswAZhu%2FVdGwESpI0UFR2EzrGxPZLEZ%2FDu5pCaMnQq2VqjwvCrp3iTqAFt9TfKLVEEmCM0O09Vk2yi0Fi0meFPuehgpyMmAUmeI6VCJfZwuBnCGUMRtit5XDGnEqxQtypR1SGkge0L7DxiAam7JTSvAJNDIn1pwTRFZqRYjOnDXi3OHrH3JDpVghpubKvASPt&X-Amz-Signature=b63cd50327be1e721e24404dfc1bb3d73cacdfa81ec9fef1737dce369b55874b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
