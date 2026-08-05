---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WUMYTOJ%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T205535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCIApJGQPE43jdK8MZkgI8mJlxKrd1NN8sNbG7kn4gWpy1AiBA6p5PYqQWgPZrDnFvdBvk2Gn62ojmQ%2FUe3R5tcJb3Iir%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMg6E6eFdu6h0oWYbcKtwDT8zVAd727eUW0dQ5roYREOA6ILbFKVH%2BPESUX40ivD1xmbVhvTMYp8y19%2F579FgpUG1Oee7pJNONC%2BPINYvaHvrpgqmbvmMK3bHtxqt5HTRjdyx6RyVsr%2Bkq%2Fab0S7vFjiRFK9d300JDsEwYf7DENDWXX3SFmZcHU6n1o%2ByCCrYzDec86bwMy7VICrmPT%2FGh81p43QZHZMCb7db7aYgR%2BzVG3zzddMGQgumgs9FVUhcSFG2xMhPDPCp2Bka32ypUSynODs%2FNQ2lS2Jmlmu55uXUCmUdNNvQJZI2kOyD6qTcHND2x4TI0Hs9Wa%2B81JG799jgXLAlxHl6r%2BTkBNggosnGPngmGxlV3hXDuEzPUI3yCxu5DloxOAxC09kysXiKyLruxth80dR3DA5vnLWGn8XxqeiqSJoAiWzcQaADZqHkdF2nbD6EAwBscqL4TTLLIaL4NvK2H3TZmh3fPC5xRRcGWzVg3UkTvBSCCVUYbxvFUJtauPGelM4HYpa5P4Il4mei656wNanIBQ1U3FE7KQn5CRy%2B6lFhTXFCIjfeNyr%2F10IWFfH7ChPOGeORF7%2BgYZEZHUh8fvOmH%2FngWtmVpBTTezysQCSH%2Bmn6iXAOW4Eaa16A426KpBhbQYUYwh6rO0wY6pgGDAKAOCiigD%2BziMTehb%2FslgULMAlPjn2bOXZpC43IOY2G%2B3DqM6rRb5xmN7xhJZPc584nQtVO3JYsNDHynQf43wa0XiOn9vDG8TMSmdmaeXtYH5qJ5ePQBuPbOL%2FNBpNvDwYRlVwk3NKhU4RkTd7QAbTPkf7CiMJkgKS8pMyDN8MBM3hXaamsHOyA2iwlroC0w4Z%2FGiH9kUvp16sqnyVzErjDLWiO2&X-Amz-Signature=b4414c6822afd25f84d594bf00d9b9c179a72eba9713916c94717697416bc894&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
