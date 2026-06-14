---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCCCP4RT%2F20260614%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260614T080806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHYaCXVzLXdlc3QtMiJGMEQCID9GdBfXBm5EZoza%2FmX4tBzoFXNHqpSzzUQsuf9eyEw2AiA6zfkoTiAHQQI7OsTBat5d8vmv%2F5dyTqM8BxFexzU4Nyr%2FAwg%2FEAAaDDYzNzQyMzE4MzgwNSIMWHPUCkVRY4mFWSjnKtwDG7RQgp%2BZDqcNh1WY7yxlory35PbKGatYwDVFDx3b6JCV0vxT1YMu8uZ%2F0DxT%2Bg0CYvl5DtxkYTCwq2oms4zJQTj7oEGP%2BNY6RSSRRG9dMSEaqbH8%2BRCAkWVX3oAPNfewSGEc8j36y0xkFy1FoPQdqKe0FFawlvxufMdiC4hvQAOYl0bnCRoUCdo07nhjlJswrFwQW0P6tJ8Y9f%2FrIlUxNE0qulj3I9xymF1Tnz40zyiRY%2FCGPF5H2y2b8s%2BVcPVqOnGqf0KB5R2hCNUpaDOvkN5okTeoyqEfbIDajoPGx37VkZ%2BNOR1ce8doVH%2FDwXs7NiPjn6BtSC48XT3X8qgPGMgoNOVe7BMdXRTC62yve6XMuuCc%2BSZcspM2zWg%2Bb6N8FA%2BJf%2FQXUjzXCTatyvDogT9orDha7mkCroCnSDlaEibTNTL%2FILBus1yvzxZXc9s5IMcqzRjn0cayUzclWx2M2BdqqtTXnuc2bRt1WpSHT6CyT7f%2FEBg2QqQSL%2Bhmam7SUzNzpivnWyKf3Mg6zClttm2zjkO5OoVOQyxUr1kWhWPC90VtY0fdySODwAZ%2BI1y9NkqCcXOF4gIqVOrq6OOHbldo6994EYgqLHjJBW17B%2FajCjesu7IouTMUOwUw2Yy50QY6pgHN77D2nMW4qPR8s1arvgHyxYSRSqnuwFWRdX07uA5VI9phbhGVrK%2B7uLEMOIN6Jdbqv4L1QMWcijHjDRJPDBfEeZ%2FuAh0%2Bw6FKlyX%2BGSChN4035jOs4OW5IbOaupV6ewVIIFVsSaP10CiGGkXzpk0PtMR63be6Zqpmdxgo7SkI%2BfWItqU%2B5Nuw4D1W1QOUJziq3mA8ZT6B4e5nQj%2BSk9bBIY43mlI0&X-Amz-Signature=43f37da6400840fc6bfe89cbeeee4677ac9e6ece7837f050283504b39a8805c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
