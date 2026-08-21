---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XX36PLD4%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T161854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUEiBInM5fF3oUTdUgeEj7yJQsqoXMOjup29NjqQvv2QIgUPvFbBzCE6yABL%2BcxEz%2BC6hyYr1JybCOGwITYGBnOBsqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHuYmgibJjOAmF4eTSrcA5P4tFI%2BjK30B4%2FfsZKlSrKIDnNAmUrVYPrSeLp6m0Vj0Usif4J3I3k0lH0EiQ9nuhyKsJnWBzQ%2BZiAlSKwSP%2F4nT9a46R0uH0jGapz%2FZILpC27d2aSlQ5qI4bMa4NjeChEUbe377LF36gC37vWCcPGQ7H1XpIVYl6fWOT%2B2MoQC00P9TG8TxOObfHwLWQQqx%2Bz0kdxcy3oztH7rXuTILi4uGa0j6UnGARhTNxhU232gXUwL6kJwfNBGSrSz3haZNuxQNYn9Jwid43fUqt4vnjx27%2FEJyDFYqU4Yssv5VlpijFNI8KLz8J0hUwduy8ERho85ylzERLVwujf5pJ3BcuZ7Yv8Pkslnh07YJNf6041dWQIprij9IiLM0j8b%2BmuHWwYOeWesSajPcZ1JiYw0bMjzzI6ZXertz96l45RQmG%2BE6FPFmZgty5SHyRWkV0z%2BXdmfYwdNSyhBt16%2F%2BNrq583Q%2FKLOad96%2FgmsIuj3bA02hkgzwbjMlxTXdDzqy8mTaTmjp%2Fs59TmmTU8fZzqMJDHOx93Hhq%2FxtQrTVMSDJOjtlmNHMWAUizbKAoD6ASOvxp2oq%2B27pY3roCdkRlBXFAZ79Tg2x1Mcgnomndh421PJv%2Fy7D5IeS76gAyGHMKzBodQGOqUBrGEECcLTNETkV2aoQPxDDoiY8JPBh0k01IJ3SqALPJZluvugaMzVx0RfldDTvmFV3399I2uvhp6p1xzvgNzdJFOWqJ5NAJSwOkwKAcwszmL1RnFCQNnOurwnrXFx3MDlfcmbVfMBcrYzhQEoDxZhqcecIUbhqTH6OCCu4sDGuHPls1KcRK%2BWNvE%2BuHR7KdcZCvlTeQ3IPGbt%2FwFwBLRxlWRND7AY&X-Amz-Signature=77f514ef62f6aadd080dd7923e65ea9f3c55f2352295ac721886ecc561bc084b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
