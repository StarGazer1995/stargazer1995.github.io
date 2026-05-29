---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7FWAP5G%2F20260529%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260529T061331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDY5wn9n%2B59xpO5pRH1YHyjbltPiaMYBegjVbywIta5MwIgGXvvCAz0a%2FSfU2rGm0PEAq0YhnHODQgPIb%2BsNj0hvZsqiAQIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBLrMQY0EMZEPK%2F6syrcA1S9i7flIBUU0St7Q%2B1Krd3UUwRCQyk3aVPhVh5LEzWoYfqV2CbIQTkzqScQKCYd%2BdtVQLQUoyag6yBCONJ2NlK%2FYMqk7Qg%2FuQCle3BRa1ZuY%2F9vItEB5P59ha5NAvPAHOsRxTswrCvGw2jNayGgZcwV5c5Q7HlyX0GEbOC5TksrjMUIppnSTtQE6O3YV0JLj2JvtYymNWVUpn8Yg7tAcc%2BG4mARW1WZYHplxswyFMVtGwp71PciDbKBEh8JGlYwis0ZriEtVjMCH0j%2Bse%2BkZt00VlH4PfNuekked6h0aT%2Be%2BMpYONqM2H2WoDv%2Bqh2Gq4MrNotJ3hy0bXj%2FB5zcjd6UZc9Co9UlSfQNuzDNrXmrjZ8Itsaf8lmY148giI1CVlBs6LM4QclFshaepLv6l0fZl8Iw7zfK5Y%2FGms33k9CPWycE%2Byckz%2BhI5m1pQZHaPPdtF6XZem658fbFFViO7L3U5FEF%2BbOVe1jb77ULNsYN4DsJObDLEMvdjpeWF8hUdjotLd68ABq4uQuNUHnqMjMIWbLZZxRjTcVbaiB5Fu%2FNtJahteSBbEGP5Ac4DuYL6Cl3%2FA1kPGLweEXtgSjaTMijvg0DYvaEW4EGMNXPDC9cu0yeLdpd5XZgwhd%2FMM%2FL5NAGOqUBm35QxeUtUb0SjwDZHmbfnUjy8ZM3NG2FDhLWPF6mEoseySFVOODp1hCpMxiNTrQfBhYwWBM47VspzBCrVQG7b86fePwlanASplTZbZA3auXv031zrrqWCUwVbjVzsCF67Px8qM979oOzCBwff%2BWdFRzeDQp96%2BsEKbzx9N9zteztsnBoatUa7HrHk3D4reTssAKVC1s%2FqOhCu1Y79wi8%2Bf7nYD%2B3&X-Amz-Signature=4694b3d52c729450abe2f442895880331cde8ff1fc7b018cbf961dc6e44c007a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
