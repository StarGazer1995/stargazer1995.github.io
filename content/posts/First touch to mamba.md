---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLTPYDAW%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T125148Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4JrzviqMB0QHrap5lwM48RDRCO3jCduPZ0WMPPiCgqAiEAhxsmrqP7vXdGvRvC1hsPktweCoGVMDW7CXFfgTB9J5oqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKH3VgmCfKiTrSt3oircAxfwLdFGPLMDoHLYs8IaoqItk80xlh2Jy0dq4muNxjkuAxfqKWW3nKdbzNFTfYHjDsWo0anxCYhBGincYhb7JxoahAAhvBGrEfzH74JGzBaAOT%2FL8mbp3ubt10L31hdI44P8FHmPd4YxyG2Y2isbhl4uxjBUhvQxRQzQO1WAl9O4o9yP5Ny3bBa6N%2BGRQUBiTX4C3yPReNhUc8ex87j%2Bfz0RfHImj1vBiIm%2BDyFU6H6a2tv7zzAA7oeHg8k18bZmMkDFv%2BofLZxZx92x1jGeDyR2YmA%2BHqlVZdNtw%2B1gm0pbT%2Bl1cryilUkX7gTtAFoDKWIKqW4h9W9VNDNhtERYSSoXxIIAoiCIltA2YrDSjVSBzVuhca5CAH%2BGnCymAhfuIBB4vMIfuTs1ildmZ1xES%2F0H4QQ4c5yZJdtU49Zknob0U4AHPUtQPBO5JFF8smJ7UcrVH4mC6g9quXIgdSvdP3NL2%2FxBz9VYsqTi7fuPS9tkCaTvUdIUDusCy2WdYMX5iS1Vowa%2FT4miMcuGLbRBB9w%2BWwIiE%2BjypZpwsMO2w8DQk5iFkNNcpVX2paFsobbepI602U0WfQ348jy%2FfcgInu1HxPWMEDAbM8hjF7HShqTf2Imk86qO%2B65l3rfAMPT2ttMGOqUBWx32ymKl0W50FCSdxKePLH4LRv2P5%2BIJa8pX1J4JfeMzh27Vp75MBtQz%2BnWkqMV8E7WVGRR6Mge0%2FWqYcmIEo0GGKZYVmV4bf1ka1EKLneewQaXk7mnYDRINl9Z6m4R4jLMdzYAd15yhnmERkxukaqmQwftJya8Jlt%2BCIZ6Y5hJBj0ZQDo4TNYV1lMBHnRTYrdbMVORu6DNYDPQrocralEOG1lRe&X-Amz-Signature=444f0e8464fede3a162eb708ebb3003bb91a705ff2c8b987aa686b8408bfd1dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
