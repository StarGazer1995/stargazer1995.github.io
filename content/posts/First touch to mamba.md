---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655JT4XBI%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T171350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlrKnWzx8fUMF%2B0wmvJFI2PNd4pm9bgtN%2FLpKfx%2Fb7JAIgE1GcAQgE42GfvMyy5rTZA04ofTtXzdCGKHfc%2B7Y9UB0qiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAAJFho5FHQowMJT3ircA%2FXdPO%2F1GuYA4XERh%2BgFhPMot5v8acMMAEOmT9ZSWQJZxgPHv3wH0iQu%2BQPf9WoW3Stmn8%2F30ely6Wk01s2uOLq00B%2FlTat3YUWD0uW6gOpRNepfMAvy7IIewggKA1LPzwVaZiI9FOb3sANzXj3A636HwCyXdzd%2FVrE3EOFH%2FwuLgLKxBY%2BJW0luz%2BdqOQYB5cR022fVC45lfgwrh7MeuVnB1j3SnACqm62ApEr3Rl0xGAiGJ%2FcdY1rBZKYmvfbE%2BG914nUcER7UzTrvjVTeyDQi8HjsZ79NqRIBpOU3ZQvgOsllQUhEpg0UABrRRteEA3uPXLiGIRFtGv3Kfr5a%2F4c6ZbJmOUOGCX%2BcXhORiMrrwQ97Un24tJBuDvoX9fHbzab%2B%2FcuR37ug7GSjh19ewRnCU09hm32jmQdNzwZn6OZ83LXdkWoo5ORBtQ7n8Xs6NCUvSAosTsmFbPgaE6GOMDwjo7HbqJbJ5Y2fWBPTbvPY3wX4OUkgXntOGrJAx%2BIPQTkoPweQO0cFiAZiodN9lA6cIkZ4qvznAF0WjGdwvNPwlf1q1Mke2SEJPPaFLEVUKvGwWTTz4hA76RFacFsgNM7H05uvhszG%2FLwRrl%2BtlJCX2VoKBno3i4BYJ5NwMITnrdMGOqUBLgryGBV2aZ1BV205TS6N9ebGF92%2BPPOnJ47FAL0pqMcRpsiI%2B3suE4ggCbX%2BE7ltSx0piIXj696mnsoUWqot1Y87HAr3S1oV0ZXjVJN7dsn1f2qiQEv9EWjTRVkel55L3RcZI1RE2OdiwEKZofAl1UrX18oDSHUgebx8kJJpqQ8st0ndWBPHvXqiHly9uRmJSb2lxU2soS948yBVw4DQhdLjAK9r&X-Amz-Signature=24bab14bdc4eca8ca3ab54f6714e3fe74bcd53d403e8a65b236ad5c7e8c72470&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
