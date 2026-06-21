---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q74TYPSC%2F20260621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260621T082117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIQD6F3WPXWN5nngwM%2FkBmwox4BoAmErVtTc8wQjwOoFkoAIgeHC%2FTncXordu%2F9f6KkK7Bzd8sJ7GGldZY75xpEAXx24qiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKCLM6p3Qxu09aTPiSrcA3hQfQOc%2FxQNBQhytCmId9yT%2FuI5RTZSw4YHT4WZjfhe0t6dtdPqwUMXPH00C25PvDpbnup%2BIx1QjOuraMFdcV52%2FLg74d9%2FQMcwdkMZHOYKRwdSJxLCI2HjIvxx9WHzYWjC9pciPrSTi8Czw%2BTPlZRBIkFFjIxwjzh3cm0KR8XxQ4rh7CEA3njhcnxUphb0E6iOqSOXPYSMn%2Fu9%2BhTiQ7TpYTiTW2TJ4HivB3Rgpdg8lT7uQ3%2BGPGkEQjIUzMnu3rPZUj2oP9NVT4uhATGNu%2BLf5ECFACVsliVk8vVssF1DHHpP%2B8w71Ej%2BfGBP4EmbOL3qcoBxWUhBqcgYEcrJ5B79HjpWtazuPXiMdlEHE%2BIMpeutzBIbH25500fx0YtsOJkQpgSD%2BvBDs8HznLiOPCqwijoHoANjkEYqVIt%2FoI3DHZizMpp52OjWxf7pZjWcjO277GA2yEsxmV5WaEOBNJM3S0xd4Cyg3j9GKQ2%2BgMsumsWzYI3hjSbzU05kaFEfgGOZH%2FWIDBOnnY8iJ9iPEF%2BIqNSI9z11prcwv5uaqI5CsYOgKo4dJxcui5f%2Bm5g1b%2B6pAN9ZV5JWUup%2Bir8z0lESjFpFobkalKb0TqMTBabAMmrsGTGKMJzf2ATzMMWA3tEGOqUBe2oWR3giX%2F%2BylFeg2yv8gMx9fls%2F8vFUTvb08g9HOtHGfmielfJ%2FJ%2FrL2QNGVbjmrk85jPpTaFLze0sQvmCKCq3PrOOsZo5Ry2XyURnZDWg%2FS9zOU4tMS1JBe4XQYiAOoFwEB3vW11up7PJG5eku9mYhKYnwskgId%2FG%2BpHfOO9MLf6wQJuAShE5e6yZ89HAKzf9Q4YErHK5h2y6JfkqM0H3evAs6&X-Amz-Signature=a5cee66e00ed5c4c9f345df6bba40b7311adea6d1d15e143c689a1cdbadeedb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
