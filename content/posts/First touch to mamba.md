---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBVIRMTH%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T003329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIH2QMihL33JuXB2Y2TYo7Sy0NgJM2yLE8Hg0B5%2FAdrv4AiBLBmLQbO23dPTpa1Ue8Z9hmqFntThENMrHrjAVpLrs2CqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMItJ7qHPs%2Fp1MmrCmKtwDYmeXuigFQZfM4dcyhRjjXmLc%2BHGQVZBREvghm8s5bZKdZ149oKwZy0L8cVAsR6EHvZelhcbfcn7%2Fy7dLtkCk55dWKVCQK1SaV2%2FxGRQHVcczyriQljVgkuwr6%2BtkNLFfUsmdTd2w8LLExb1cRrGezpExHHDTg44QuQ7WqmWy2xV7hVTeTft4UiAiXETYQWlDCsQiBRJXGu1GlyLMIMD%2FHXeqI61XV%2BhRQwzG67H6pimWRmM%2FSOvESgEcilYvx57N7oqyJlc9Qaia6IvnDpcmhM%2BnvEn6LZEvPWZ9MuWIEDs92sMEooKZe%2Buq7D2EbNVj0U9QIR5%2F53vac246kaq%2BqkD19%2B8Br110Qr%2Fy7nQutgkzbm6TUdm2wzpIM0C45QEPWUuk2q0garpKXa3Omccy0vjvi6FYadfauippBofcQcaz7t7xlIe7DW3vr3pnVTAhoxfRgcxMby%2B0yqKMKe5e6IrVj3umzXF%2FuuL3SIQkxKWc0HQdxpVK1CH4W1K4PVyODtf0dibrE4KoaBOavsvculjAQ%2BmFpG319zl97gdLblxKGVfxG1NYwkL4Zj%2FDp%2FkYAHC8lJ5WbCZhJERVdhbzZlMaLCx6V6nP%2F2cx0wHwq9FJ6b5G88xDxvoJUFowz4Su1AY6pgGQnMXcHJfvj60sQ%2BRo%2BEHvnIARKOgm6363KaNtwXOljP%2FUQIn%2FdcECj6VDXafiwZu9U8SGg%2F2rmRe36%2BCZAmVmSdV%2B7f09tVMYftzNirH3XHwGqDd%2BuivlX2jSjY2n62bqTSR6Ed1hhAdNchNZmBNx2ue3HCe%2BJpnLRkFqhg6rMRecgxGs1nqJzuwf1%2FVksteb22nNyCiISkF8EaXOalgBz%2FJlNddO&X-Amz-Signature=5e0be71265aff2a54cf4dfed742f1343ee53432527e90f2f07b915b45533bc5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
