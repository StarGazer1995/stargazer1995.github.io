---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHHJGQYN%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T103327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE0oShSjPeJq9vdmHws6GZ2g7GKiuAB6CVHentUAf8a4AiEAoqKXB3CIgqVhaHrsOeTUEukcJ0%2B%2FpFOjV04RKzmm3Woq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDB%2BeRnGkHU%2FdEo9GOSrcA1l6a0W%2BPxAhn0ncEQyK0MphL1o5HdGTrkmniHIBOjtWwlZ%2FsQOqocxHQWMhRqse%2FCQbz8CYPWGpVsBfGdp1SQbGsVwg0qK8VQrnor5gA%2FWAOznxCOp8WxOc4Rnx5gYhuvkZIuYHGpX29iTG9zdrBWcNqC7%2FGkm2XoOT237cQTFzyHToLubinh%2FDRDW3B8bcUoUPhxf6d8EFAjztfHJ%2FUUFuxpU6e1LY56AxdOoJvN8yscZg0drNesDkqsTKqLv6fJxQH2D7%2BoqkiFdRBAmsh18S8tvnMOu1kT1wEPPE3VIND63ogJuR7ot6USmX4gSa1N9VCfZchPCrFl5Lylcn82siARYFRAYNLwN2mXcS%2FRrIqz2HFxj6EjoGyE9%2BFMvqITV9Ffo8GIRWZt8YELSZx03y0AleuajKG1ViQ0bbzbcz2p6AmbdbQlshD9ZhMTporDV2qwmfjNOh4%2FbwzFYRZrDaps4MihLmL0v4gcIQr233hYI1%2FExvCazKJO%2BsGUQj9%2FI50i%2F1%2BIehqLBsHdaj5XgKE3ijkKCiAVo4j65340sHfqZETcWNCUKQT0z7yl%2FlQ7qaqRQ4Kc5t5mHWGqjZtem2vcVwkwJsi0PN7MuBgnOQVagCec43GiPy1YfqMNrO89EGOqUBHZ6DRE5BoULcG893CvKmduCtEk%2B15GWVO50feYgglsF5fCFhgiqV3QHDxJYcY1GFTUvXa4ANwE9%2F4vRtGCQ9ILm4lLDmgUV%2F7tDSN7MGuwLOnD68xzGTHMx4HQ1gXNSflQEa2MzdS%2FCg5Nh8stFm7jHAVPb8L%2BNpRIXETQ33Bd4Tin2xgqCUgqUDp4ewla%2Bau8xV%2FlqD6S4ekKDIY4J8q0m2H8O5&X-Amz-Signature=995dfbece74427d12ef09c3a0f50b7a616c809f086d0d76eab7e966845e1a641&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
