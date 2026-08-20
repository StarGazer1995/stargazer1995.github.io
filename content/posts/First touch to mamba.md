---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6GJ3UMB%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T003215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJpzbvRcraYHphbFRbNTHx4IKq6KDFo%2BUZd60O9D9xsgIgVV3iyOumQx0t4mPgnnpuyDMxv4bOeCaYIPVzN6TTeskqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHykIRWH%2BEVQEBId0CrcA10Rbwk1j4PZmbpCuruJV%2Frft93pKknkicpHqRDxgM4TqfyD9xe8fx7RCKke7PCu1f9OHyNcrfaSkVPl8NbtzSjcUcQekFOaArlPl%2BKFjsA0Obd8TuqmFKQ1PzvEP1zLrW%2Ba9EnhXcLh4OGLiVvR9JGQ8KCv3tIJTxlU3SuHYL6FWl3sODC3A1miK665SFxVEBUfROukr6nsvxdIWLK6YpjkqtJRUgnYkyuO6l969avZZmhQ%2FIG4AK7r3FCUnkcp%2BWjiOhkUr%2BEv4ssRI6%2BT4ZLczxOa%2Bw1k7oeUbzrG39Mz1DWH7rWtowsMZlulYOMXE35R8z6TgLi9UG%2Frh2q1%2FTS5PQ3JF%2Bg739VPe3HGFeIZzAugePfpUO9RfbYaBSbNALeyuzZIc890lEW25EGex52tF%2Fc2m59fuLIH46o4GbGrVhEHLspT6W55bjiSsIv2hNGlvmDpyJXpTufTh01BdNMcI3VlbN6MCxKFL7rOxCd6Ymxk27UAPE338oisbJ5hp65ky01O2e%2BcFwPauZtWyQ%2BHxfoEKVud6QxxZDOEPb8ZY5o0%2FHgnWxdVj3vumQsdKR%2Fjb6R7D2AZ5y1ZdvPT7Y%2B3taZoO%2B%2Bb6eBtq0ilrr5iifTUIUVpoI6qPpsRMNfumNQGOqUB6ueqjo%2B1PZsS39bXnbTwYB%2FexrYo7PKR%2BYluYK27vpfWyeAcDbcH4jVzHfXdIWhswaq3x7ZS6Im0zAOHgkpb3BZMXiSxlnqcJrcPrgaW6uMWMptbhmXPN505snlrUhSvyPjMwsHzutuEJthBjyi7c3d9unui1wd%2FTLTzliLejB2xHjFxO2wpHuSjhA7MYeRPI1m%2BegZZ7CgNl7Qmj%2BP6NYkxdvdg&X-Amz-Signature=f4a20bc45a9e3788bc835bfd8bc807caf2d4fe03612fe63c25f18e3d0e0f304f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
