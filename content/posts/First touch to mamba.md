---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7Z2SG3C%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T164453Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVQV5ee2V5zPX7waU40kaFAEXXhdsbDzxJ3Sh0VgTP0AIgEwmGzVX1VU4fZaLIjGVcAeFsyK6Nk6Gmxpw4oCGWoGgqiAQIqf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIr%2BWe1SHL8dUjNPnircA4Dq3CSULjB%2FcXxvwxpOXAtmkaH%2BdjH0XGLVZDrN%2BnlN%2Bl7lq6oKAiNsqhxYat%2BjpI0dcvhK7tQwPn2YmtlT6Ll8QLYNK3gdVWEFdutljR88xmpihaky%2FA8xp4IAXSRh8HME9j6Ep%2BBFFH2A8uuA2K97IhAlmDhyigFQvmjsTz%2BNE0IwRTGqVuksI1iLSeKU8lKhdZr%2Bo34gPl00QzxqfbvE75RpXPAk9LM2XyCyvsfKRcWBJDXNm3J8b%2BGUS1ehe5tbhLSMgBnHc6oMm5zGsz2AGVf%2BKLDD1CtLvJxm3yUSNUtUfqInmSFR6%2FC%2BIRM5RFuIoR3rnQ%2BdqVpLwa9W4B4Pi1ETyALq2CpVQVFpJ5hjt7I%2F7oBjM4kG0bQp3TYHk2hqPpKh0RqTEzi4kqVqcemmF9UUZ%2BbG0NEdg9mUO7BBs0GDD0BQsGPthz1WAd0%2B%2B0HS%2F07V7vP%2B1OyjZdTH356rTFDbJzy9OdvMaPJ3NrQaBa6%2F7I2T7WwumDo0Nzi%2F2U4C8xk0DIYXCNevrvaNCvvhKFSLtGhFAfR4Yh7MmZAOn7bZGFGmLxDQuefoEyGYKw8o%2BGzM0L0Gq5UL%2BJxyVUP41xwwoAI4zcD7Mjm0l3FKsTPcnnLbDppw2zImMO3Up9AGOqUBTfpIWK4ueHgCeVJAFzgRQmw1Nb3rO7c4tfmV8mn9Cp%2BZ5Wo0GW1%2FjPqTHdxKQOpkgcz4HpE9ZVKNucTZejk7SoZy35Iw5azYwDP%2FT7hzvg2ptlbU1V1kXkFu1B%2FFwpTxIACLD6EG5z%2B5W4mXV6zJEcWfWQ6rI9ClJq%2B%2BGArfPRqFddeLSWi2oF3UwZbkojMz2QqLyGP2BdE4SgjZd4xMrRVVZmou&X-Amz-Signature=9a5fb8e7bf373d29f34d30983897d4e4def9bf7ba0afde8e6771eb6741dd4927&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
