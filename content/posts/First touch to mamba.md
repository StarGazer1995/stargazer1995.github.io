---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T7DJLHL%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T125924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJFMEMCHxq7Ss%2FHPc3pFDphv7%2BBVE57a35NeB8%2FpjNOw9Pekp0CIDEoaIti6SjGcRRJ%2BtLPCOFHp0mCVx9FmiSTIWrWenW0KogECNX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igymb8loSZmALfAu%2Bj0q3APRbBFHWPN6aoNfKWUFuSEMjdZ2SDka6n9hDSQ7sKiwlIgmcSkMegZvit2qKD%2BgxrPFbnRQEE5S8dAOM0Nnab029doPY4mScLFcffAigjhYPLob3kCX5hf7%2Bfhlpw8xomEtwlRgJj6bADt9QlJyeZnuncJkIJG6IbRhdqOrBYziaWkgyzSynTFFcqUmvfpZUjbySy6D7UM8ATeiOa%2BKynz8gSsR8WtbZ%2F8jLB7Uijz0VzKCssJXu7Yv2d%2F07fH7EcfQmQ45Jg5DsVOB%2BgHx79tLrJf8bWfu%2BMhe9Uoy8wCg23RdyVD699lcQd8kVWWwTaqqWBg29vL1Skd%2FrHYdrXatOuR1wcUn64DwOcX%2F0WXikedEhq%2Bu%2FUcl4sHTmoloM7yDq0Ddzqblz98d3kQlFAB%2FdeJZlPOchfeqCCmUpBbabEJO5QwtdVURIT02Jaap%2BP2OJEX59IhNMB8WTWfiM65CAitK5Bj8%2F2wXmZIbMT%2B6P%2Bo7SjgNMbxWN084XwlECEs5p7kbHEXjdCM8oPKMT9pCQoaZ6%2BuHn5pkOvutsZnVUmCW%2FTUpZc9DRib2gKUmrYCrAlnPXek1jPzgiwwSw93ADMDPbqLCKJUPQUMo1FPHCfE8vPQFArxA1DqGuDC%2BndTVBjqnAX0SczpHn4QAKVMkM1B1RScv74Cobdywlfm9Uck%2B30wnska7EugLJpGb8DpRTGxq%2FjWTAQRbTYYhJ%2B%2BfivJfeai6z3Rbk8snriTbAxmhx53XFCRC6eUA249KAyfds1P4rf3MJPflRsQQjueG3AyoUZSIVYgjtIaVlB6Baf935qZneONwj%2B5lcDv5Hu7%2B1s86YqJfzQgV3T1PYTxry6R%2BjWgAaqJwVVyj&X-Amz-Signature=8f940061cb6274a4062f23fa3994da66c83238a4865014b6857b299d08778622&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
