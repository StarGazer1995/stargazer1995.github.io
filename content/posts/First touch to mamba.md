---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGT4ME4U%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T130519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCu%2FfSTfehs7X64FgQ04%2FGbq4%2B3T6yOxfa4SOqmO7qyGwIhAIZWcsHblY8WaaI%2FSK8ntlY5xV0zM6kTgVvkM5X1q%2BDtKv8DCHsQABoMNjM3NDIzMTgzODA1Igx0FDYOIPdWlmKcTe8q3AOcSp1VnUCF%2FcJAQZImeNzehnhxEzYO77P6Z4bvjrGB6K4CCHJmppnaPkZ7KUtVDYfOMotfYQ8leUyWWjdUeyvPH5N5uD9qY1XGGai8%2BVEPkceTIk9uMCyufQM1%2FC0WgiMes2qBi0p%2FlexqvGMDOW4uY9B3yKvQrP0jEetzYEK4AMtV8hJJIwM89ApYGdUoOA7KhZBhpq2FP8uKRMseLZIrrk%2FCTlfrL%2FxHS6mTznln1YoFxIkMY8cf2kHU6FPGtSKJuDI4jCT4PdRApqk1ImDF0I8qc2PZu3DFqFYv2CeIIwRrL3geKtXKkMpr47qWy3k%2FHfkco%2BwLlnU6Ikc4uqIAfzlx29b0eTRv8kZ7h2HciHK64DKtRH5gEe%2BVsWccnaiL7PJonVAtW%2FeDRIKin1PmmWXtzVpqXRXYjUfnes9QItj%2BlTbyoeA4bnCNPZSVQ5pq52%2FpkPhIVHODRIz1xKMvIgwEOpYaNQy6eFeAm5E2S%2BBjWtO3rkvF%2ForHgOSXfbWuwP0wCi0KbMAvXcy7AJ7Pq%2FYe%2FH%2BAKh7khzgawEUr7Wyw9ndYGDUBF7sMDuKgDH2%2BUpEwLXZOuoXKA44%2FH%2FLb7nzjDnEOXOM1zYUv7IrFgfp720hE9p%2FQ8PTHdDC9xv7RBjqkARRTBbjKRjNKEkVLYhS%2BNoX94rZd6E1bZCaccaIrs9%2FtUpwB%2FpULIxu572QmyPGXhR5ZLR49X37dP77udihO9WMqcu3XW0R1NsfPd%2FUF2lOK3g87w5x64yNUn3kmuMUcnvNXbgSym6yV0b%2BVY%2BeyqjIJteR81cDuE4WNxDgjLuXjr5Eu%2BYKaelv1RgAKBYDBcdcz8Yod5yXwsFIMLFc10HbYQlzH&X-Amz-Signature=12039e4af26220fa27e88267ca3ba9ce0b8dabecf92da91346e70d20af043c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
