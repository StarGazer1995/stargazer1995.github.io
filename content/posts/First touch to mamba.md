---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7CBSVZQ%2F20260524%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260524T020027Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJIMEYCIQDGKwCKdVcO7bJPl2Etg%2FNZWKh17eTrwsF%2F6hcF9OdpwQIhAJii84iMuJCwf20JfYThVgOuZztMHu8vLDDw5z2jXUY9Kv8DCEMQABoMNjM3NDIzMTgzODA1IgyMz3FK%2FEJDgOKGDtQq3AOQoX6ynJJm2RSRyV1Gfe8V5rdIZ05e4ibNYSSsVWSoYi7Qftz9ZFuNwWCpU6XSwiPFptvKMi18mSMHOUlDgMPJNRlKxU%2FqpWfSPjXW1ucGii3I%2FI4XH3SQEM0BZcsz42Ee5W5EWOkjLCBUx4fYqLVbS561fIxB5XeWnDVu%2F8G1N4bkoQHvLN1HpIxgzlsw%2FSfmOOrE0K%2BwFjgrxPxKZTis5txzlaOEsekThb5zcc44cA9MKIJyhtIhj62pxsD3%2FTZ9ITAt%2FWMF5Y5g018XWNs4WzHg9d6l6gw%2BGvuN%2BoL1uP7L8hm7IxxWxDT78ZXABrYT25Zb4tWyFArqzEQVqxUJYIABGF7tW%2BGmiqEm26G6tzrWceo8GMQonSAJVHOBr36orTiA1uOx9b3Orr3RB%2B5cK3BTwozdJu5hQiY%2Fvg1T%2BizFjKvoXBgFnDpUexVbRnS4rbhbdh3UHLJlOIb5R4TjBQzSD%2F3NjmPXOBR4%2FZQFev3hdV3NNjK2ScD3nQLMTnL8FYG94N4dlAgxzKw%2BmajYu3NdpTq%2F6EHFdt79J3ePOWZagi2Fo9tNqtAGdeaN1yTiRmkjkkmCIgweKlv2Kf9p8xtGLbM0eRSagjTjoAYEXBZaElYqbvzkVPCa2DDeqMnQBjqkAY8SkB4AlgmXwJlcImzu5I9m1EWCxC8Ymbd9Swpaa%2Bgakfuwudq1qvf0ysZziShX5wugHy2U0Cfj89%2BBEcQF828rtfHiLb8I1V5pV2aMgw79EGDdkmBSkdfVxABBhkwccsMgzIRAwaC%2BKBewGymUF8JZkBIr%2BSEPWf%2BVQBO1i3CgNfcLHuVJcfgrFcgapcx8yE4T6VCuMsIt6FrdqeM5oHkVkYjw&X-Amz-Signature=804848619501b22deb4d93870718b43edad9e85cdccc56608394ecc92423f082&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
