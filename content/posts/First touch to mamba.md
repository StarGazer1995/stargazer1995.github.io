---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VXSPK6J%2F20261017%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261017T080724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDGmqausep0b0a8W7iKB%2BMM2LkxS0NsLwRi5qEssWYUXQIgaXPdKECyUk2PeUouogwaxv3tL8aR0K0U1K9glJcMxhsqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIo1n1mgzSTdmGj7rCrcAyaCDgDuFCjkc9N9fTYIGrtwCYQGmC9XS6NWW1RGkhAsFOpPCthq5mtUdCoAH1QOdBNbGNnvPDS0wVHKKzysQ2DY0DxoiyyLgdAL9pX7Jyit%2FVhL1os%2Btnv%2FwDEXg5bYcIkgxKVW3MAuPYIXuO%2BpTxyDGedaC9Ku0DXCr7IyQlNxcxNyH4yQ4QD6o3NyKcHTadTAAMcNpqoR0ocC8brsLmkE6mo2VFoppBcwXHtdDkpuMYdRsxKVbNzoBMr%2B5hioTcVDuHuwM3yfC%2FLWf5R%2Bg5ap4zISht%2BGfBsFnKkLCqa7R9xaySUbPJV%2FGejE9eqT80xj9xVlpd36YVmScHehlrzul4h%2FwvyIaqeLakgk0onc4odzwgydgEy3pQLgOHw5b0tC4xxlDxHPMRR1SaBX6HcYlQ2AnpvmF8g0VpE5MHVtv3UytenOGulAVJXQX2wNuLkom6HHEQqnKJqSX7%2FSTp6TVbfF6N3JCQEWSpgJFI6TRn0juBHf52KAshsHtzb5jm8WPO53mBbJOEPJVp8cEfhUvBarn9Gn%2F4kjZ6g567EmpaWQsgQ7wdthHtDiWShywNMiuFeratBtVtK1KNoWJn3pEY2M26ra1uGEnrnnLIcPMlLHfBT8qjyLjn2hMIfTzNYGOqUBqxco2RwKsmlvdbcgybOufPwpy82wESGI2BcK8eTIC2zX7hqx8r1XSeK7SJT4F8dwwMOCGVaZX7JwJlZhIYfxtSKMJhbyZUGzaEuZfmmofrwj01ZP%2BSZPijQZ4DPgusjc7JizcRNU2Z2cJdYOE1d2b1t91eoYwNgfKw9pA9RudH5VEAlBV8dA6egGL8yqa7gow3JdkFXiliRbh7hoFg8Yr7IFBK4L&X-Amz-Signature=c2dfebd0b7b1839acc1046ddb599a0e791a04f2ec52bc69ec416ca1464393a06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
