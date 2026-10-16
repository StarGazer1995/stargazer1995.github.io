---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQU2EOEX%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T201137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECMaCXVzLXdlc3QtMiJGMEQCIDIsS2twVk4cblCZlyS7crAbj1zHEPVBDYQ6BsfybcFLAiB%2BNtC92dDmrfXGvbr0hBZroTiS24x1keUKtto93w%2F2YCqIBAjr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZCh6dGlM5M29m39FKtwDA5I7KY5R9bYrdyodCl3J8WFpe69Xo6VnTVa7pAXmxAfhICWdjo2WTHlVVulor0kTcfXJuAR%2BeCV3cuJf37auwboBH3Aa2JBEHbBNq%2BVV0DUvbkBTvuSGBOwr0uNOtSzPv%2FbungCqPTWykBEjhMtDGovpLDMEEfjwsB1eYsPucOYS51XjeLUTdcdabU1fU0Po9YB6Ei6v9qWcqI%2F1tiJJMFw0Xf5lj%2FLBeoMa6o2VjOxX4c9YQBqKfYI%2Fd8ppRBI6jW3ekaxrRlYW5gd5Yo2G1k7beukXIHG%2BBsjsNItoRTcRJxXMKu7uXHf2d07o1XXp8IHDE9sADY4duFhxx%2BacN41TQQxYTqKi51KeKv6Pl2v4fi9x1FysU8CV4sneafDbwJHYwm49ZaRMmpcaMGnEF9a7Igd62eiqUJyC1ZtcpxUNZQF%2FKlbGK2TiEitmVrSfCGW65N1%2BbsM87QknKu176ZJuPUowe1aorIfxl9BGYp2y%2Fuu2FSO6o1dyqNHkX21lYGTG30pqgIVHhYp1No0FPNjTHxGeSiJQfLpnOBA6y1e1Ok3SSheSqX1caCLOpRjxV%2Bsni2556uw1lE%2FBuVeHkzG6ggjkfmwcT5vySwz7kUpd2Qe8DtgFBFoO2RowsOzJ1gY6pgFY57r7AW41gzJLMILU8szg6NtET0X1r8E2d21ngAZT8R%2FLdIRGg0t8AjjhDkxWfR9e3p8uxr3ALf55FC4B7y%2FGhJo9gVWHSv5pXWXRo9JcIDPEtNypcu%2FnWJua%2FzGO%2BLLgCKZhEWXfDoN7gCxjPjRGR%2BDlSBTc3L70WuaJYJW0xB6ZvOG6%2FzfBeXtlOKVk3BN2TUzKhohFcpXPMg9owQ8YXOnylkEp&X-Amz-Signature=cef5a17b512bc0c4ab06f76e7650d1165d7de188cfadddbf458253f9b0662189&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
