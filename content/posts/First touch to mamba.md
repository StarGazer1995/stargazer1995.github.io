---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V62VR2TJ%2F20260818%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260818T202955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEUf%2BpPubA0KKNT%2B%2B%2FiFYVO7dRhEN0zABc2i20Rfv%2Fv7AiEAo0jr4wbJ%2F3Mw9BCBvdTNolipjL1kdw%2FKVs%2B4wOLVKOAq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDMJH8F%2Fko4XX%2BvdLOircAxGefltLb2spQOlNpPVbi%2F3DWwoOzAdAI4NHdHIS2JcYAtzYm2eSg3M94JFg5KI0hEr1pXsg4LltyPP1bQCjGLwY%2FAtmSI46PkMtgrYg96QhpC6VzwX6VWQg7yDDfOWcjUa%2FDkqfc3wFdtIH0M9GvcyO538Wc%2BinVTq5LRCFG24ENHF60AjXwvwLI1NGtcuq%2FanLobR8ISAaBeb53QthUw9yNYjd6rMlHe9RY5q7BJIH8pnR%2B5rl5W9aH4Ghc0t2FYNoCfcnEdHa5Di6aSQzBkQzImAplGnrTcKrMeBbAwHtky3%2FWE%2F9Y8jKKvDQUfda1trAfSR%2F8hm3YzCRT2Mmo%2FuEzXiYJgj1nGPJLH9gsrxHkJjYp7KLlfUCTx1h0gr9NlTjfQ%2F4rWJ7Zg4IwdhPjQgVgljCwJMAXbzRpGudGzSgihd83NNSu6yUiDPE46XlAv1JVvcWbi6WaBQlQLukEeHStrc5w%2BmdGLGjcmiNVQxpbtGqtV2vgyF8MFEX6iqdNhr7PWP71GNCL8jgW4TXvO8%2FTTtJ%2BMd8fL1D0nTLbWspzIibQkKlmPzDV1U3WMmKDWaSwRys44CY7f8aW2zKjMedRRis4ysl00AXmy4pW9B7ZbULYYniST%2FSilAAMJy6ktQGOqUBkXs3s%2BVcDGe4tDfMvJ2H2lhlAvr8VPlNT4yiI40AXG4efO4CMUX4GMMUkgK2S7fat9MpeJDCIVRWEJkpTsUf7r4SJ1P2Zt79Rri4ZUn3R6lEeUAi2AD1SQusj1rB4pEeOAFNJd6k%2BETD2FXKzyEYwGtzeP%2Bee04qwXLdnk2Y%2BuSKLW1LeeSlQ6RNZ37d93HZpP7TQPHTiKKSGBMhsj92FRPGJgKL&X-Amz-Signature=6f7350a7b89afe98ca0408dee0fb7681b16b5741199a3607b7f7f6787a3fbb46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
