---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTQIJF3X%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T014954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJHMEUCIEXfR90b3apaCII3y6mjwelzCbLdAiwt9yCkdesnqgBFAiEAuf7WHe3oUN6y4a%2Fb61THyo1Y38%2FZz1%2Fr4BHU6iAKxZkq%2FwMIMhAAGgw2Mzc0MjMxODM4MDUiDJ6L%2B8wogc%2FJeD4JaSrcA0%2FUYXP4ytLiUUUebeo1mXLSlMEfVkNlo6jGOmaQm5H%2BEqO4%2BCXrcdxuRiYrTxr1TP%2BX9J38Ejzntke2ZF03G3h8TE8kTUqFtKe9tMbQHWvr51kSdQ8DKQqWexSP1KES6rxO90GctaI7A1M%2FAwW7iNmjhVe1oRYfnsuOzf5ymDANskjEbk2jk1xyN%2BfZ7bwd96YV65htOmsn6YN0GAivDD9tlUVs1kJRQ0iY3FSL3kK4RUlgSngzWRF%2F71sRnTQdZDbcZBBBjD5I3n78RjqDdAVt5HM17aM1CG%2BSfm9B4tw0QpMhdyJ4QGeneyxtdT8xsqDAAiXINqdK9z7%2BM5fGDBIK8x19J8b9oCpmJa%2B2ztzKz7F2Izv5np6klDMs%2FtLuFswP7Z2FCNhZL0MuuPDZXo8Qjd5w%2Bu7SRebkElt8UKk3vp93rPWMveXTWKVfmjciXo9%2Fdod9c%2Bgp518rk11Bf8pxY0Hf3StP1VlUPdFxsUddjFcKovPzqFPEmv1r9l1Juwe%2FsUbobGlt6bxjaLDykqnJqkooSyaBbZ8k9rPFiyPUs%2BPTbaQMq8szrYQ7pGMSszsp7MqIKxnKH3CpRIu%2FfpvtRQb9CEEWxaW%2BnMeSIE0upreHmhh%2Bipyq7DuFMJfbptIGOqUBW4A6AfjUoAKCEH0ShUCkCZ1AiBOMJg1NHtC5%2B7%2B6g0QL%2FO%2FysKzL%2BQU6VGkuyHI0d59eaMJuoVEhz6VoremjCis5kQMSe7Hg1InIUjpWwmDZVBaFql157XaGo7Pz1zWFUhLY0JCiILI9SAOy8o%2Bx%2FGaqi3a7UBZC1HNnBIQ1QTy4scafRo26h949tkt5pXjNFCa6bYyr%2FJXBHg5RRpEFIrBkVny3&X-Amz-Signature=9051acb7c209ba9a9187ec0676f8749cf8da0be67e52761b2b9eba86e4b66967&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
