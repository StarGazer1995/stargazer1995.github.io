---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFC6QNQC%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T045802Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAijhnHIap50aCzSPByYpgaOCCQLo3OkJT9u6uqN09tsAiEAvefjub31%2FtNDsUpjd5%2FxbZzUw%2Bu6EKG2Ky6DYiL5RdIq%2FwMIcxAAGgw2Mzc0MjMxODM4MDUiDH1yB5cfxN3weDTXFircAwVK23gcWUkK9wLW2njKfTcTXwABdmciN8pEvSwzXiDe1gZwMW%2FlIN6SWZUtZ6oS7rzvfrnpTGuotABmjB6Gz5LunHdrgBggRjn2XBEVqsmzNZ7LBAnP7yn1Ncz8UKet9XkR7mN3fpL0b66I1Wp3EFhSWWBF3MR9BKpEuNcanPo9O2GcRx2hBnL57%2FxVRIBIyg9QMq0kOri5erUNwf6yiFnDO%2ByrJ2N6pvU47sEHOMZbgHF%2F%2BUswLXjq%2Fty2ac82vpK7LmQGjKRTGGewx3p6j2tsQlQlojvighMha0d2s%2FM3SzzVaN9GLBZCZTZquKsDqJ3VtJ053V045nOUnL5YX0evDI4SVo66CxBo3myo4lNsHP4bn3nAUfI%2B0Qs8U%2BJWyBMour84Ww7sFMwKmVOCj6OMYMIb7%2BWVH%2BM8qmmyCvcbC0GGJJ2QKtwr0QZr26UyekKLu4HrsdNVn3KvAPyDMQRxJQyJY3I2ht1j5W5CVdGKkLiwQj3pxIMLD5aOeKqAYRVxSn6tRbcbkuJUT9k%2FW21V8JPEzOFwL1iG4Edjl40Vfu3bmdjMsn1Sk5qIzwyxpwGYZBeI0Ey6rDyu3Kg%2BRpPIrshFHS7MrWsDvYQUtxxlLHR%2BBf965CXuaHbqMIfEpdMGOqUB3Do3C1SimNHtfltYsYfqqVSDikSbLPQwMQA9IxFbfiqyLkB%2BsX7teijB7MTdnPir2nVny%2F1hqnLdJhfaZntqxYky2Lb8wOo6V0OF9r8CGtqAHG76b2N1WtmWd%2FVA8yjE2N8O6fgLUNgxoMyKUtmSo4CAJGL0nyFpRC5%2BDgJnqccEwNrF2pTg08bK8TkJsMKeyAKrsIX0fO6jmp%2BFwpwutJFmxe%2Bl&X-Amz-Signature=092d0e67b91e477d4ea1ecf0dcc8467ae5daa3bc46893bff2c34b8590705a3a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
