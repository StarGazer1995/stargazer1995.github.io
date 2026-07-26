---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YJQZSJN%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T204505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIHKbmfV6T%2BOnl5YaHyLKAVr%2B3DadG3TihQpmJRmckb10AiA4dqlKn0dbukIdaoaH%2BhYrJIbC%2F%2FVb3xq1fWzYcrMAhCr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIMz6aCL4%2BDIOCpGtZcKtwDdLgxSQ3QPqRQuBBhK7Sy8Fb5sZpShFHlvxbIGhJZH5CD603yJGU3KwF%2F16CJq4AI9TPdMd84GeQ2lYok2d21HrLqB4B3bYPCHGKLRoQh7CbmRaPEBaX8R1CcPwdVwPYFngvGNPY4bjh2dIBsybAVVjpGJ7RLD4hiR3pTyN%2BDeQG7sDpSSrQMDR2MHQnEFCXhtvr3FinKmRPJDvut65s4TpbClT03OKi9O69rdaMJM6a9RViVdZpLREtuUWdJkd9chfH38IjbzRQLMzSsDlOQSpapoiZcKZq%2FRUcMUtmDK6XVeBOfcjFCcA7aYSHZwd6%2FRV7lAtMWwBd8ydupcn8GOx5nof7NWGgdtWp%2BxPMLzKRRannQEEm2ujld%2FY9el3YE6FwOrixsMJy%2FQCP4OMxEdTSz8hyJwV9T35wm%2BNiSYx8kHTkn9JfaD3R2KYQfUeNvZLEFhZeQQPvHUBJWk2LW4uKJGHBgG6ESSMG9GsDM%2FdWc2JKtyiCN6523VeyiSK260AUBrIbCH5dhOsujXzEXr3uOosRZsu955QtVbRpUkd2WkklLKAZv3Pj7JV9oxB39zCJ5VDrO9GRZERKB0bPh0qKa%2BoBVE44xtLJ2Z3tf4gSEUCK1Drui7mYwEaYw3%2BqY0wY6pgEDdawsEQ1aNZ1zIe6VLZH6wiK821OCgVwyueWCAZ0Cmyhs3zNDFZUxXAVf1R1SQ%2BniTeaswyMmmvaPn5h97QY05MQXBG3eryy3jJx9h8m3Y9vVZ4QaeawDOFUDw%2B6CotODTs9u22DVTxfs%2BcvFnq23ATa1C2qwGA4V5xzci612YMX7nBRgqhCd7JKmcTuLfNE6aqiEQ5Mho0GYf%2Fx6%2FSpF7MTTyDuP&X-Amz-Signature=de1541abd114dea704238d15e4903e22ac55357ce15062da727fde74c2d51e8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
