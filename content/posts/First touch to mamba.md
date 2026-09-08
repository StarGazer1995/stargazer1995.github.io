---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QZ6ISGP%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T014535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpOuRYGU7v1KKcm%2BLA8%2F21beaJEpQ4ICAIFUhfKeCYiAIgS8u7ePmV66iyWdjZsBwhpF%2F%2FxTqn7SkpbzI4M4D%2FZJ4q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDD85iG1mJMgKUi420ircA4wQJEKa4rogRStt1x2TG1fI%2FG%2Fo%2BN7CSzPmVVjGIEaVv6o%2BC5upXFa8NHHQ3SwS9SHuMMSwhK%2BR%2FeIJzw1a7%2BjawjNIpi8xxjRocwYUZaymZ4ZQlbAKksKWDsxF%2B4iy%2FkTYKwHmKwmI%2Bnyqth5Ui3mFrbYjI%2FwggSZYCdVbzuSlI%2BzrIDK%2BTnmF89wcWqj96FtFXEV91g7PllVQhHN38e8hkAdvYtQQtiR5xSaa%2FddgnbfvqZwE3%2B95vXX4NA%2BFfKfukcyySg8KzENqwMCNKqH%2FrI2aswF19YPPIlZBNclUkthU5pjPFM%2BIUf8ZSPkSRjtJgp6eOyKKMPcuuW0ABAp1QmERUS0BmR4BuDyIYK669h%2F8wBDBW%2Ffq0Rkeh0CmmkCdO26yTzeYirSh47aFY3ufq6xUHC5v2IreZMY4P9KZQih00vFIdbMlP8kBunaMcIzS4d6GN9KrxkoFPtGudJ%2FxsqMqf%2BVr31p3%2BaISmX2VcCbaEAtyBef0DnU72LM%2FHLVcRdZ7IOHN9O6JfML9n8Bod%2F2saxUGPvuj%2FyCw2IyuB9OII3SgiHBNQ4UsKopS7rzQxBPffSyDfwJaDuC7xxLMgWhOwNLAC7L0pYPsG1qwkRyAI5tCU%2BSFMqSPMICo%2FdQGOqUBVbV2yyE1W87MZYB0ljhIgat4p5BT%2FnUhIL2eqKGVoDuY7kbT2ljAq76XPGqf99F3mb8ukquZ%2BFzzG%2FCerKege9X8J2XAUIOeTIps34xBYRY631KBa%2FuI8HEo5ES8AEK87ixwBF9r6n2EZyw6UlHaLplYX2%2B3EaqmUnkLGCS4PqlvM%2FUdnysxnCPJuC9TQ3VeyC%2F8hjJW5XcvqXTPr1%2B3auGhuxzN&X-Amz-Signature=aab8956808034eea80248800248145691f34a97fad8944b90a1bc66a80289d5d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
