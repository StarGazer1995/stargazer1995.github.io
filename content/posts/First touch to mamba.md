---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VZHHLUR%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T120808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHT%2F01QS18Dfz11LDPbiGQsA4MCVSQ7jZ7mOEDgGxtgaAiEAzqsQmqigaHbDwdbgxCOR76M%2FphM8X1MkbAWHlsV1ulIq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDMzx5AJwFlyl43u6WyrcA3o0yIg8L9SYZfAxExRd%2BKFqvNQYI46jz%2FR7fKnHJLJm4DvHuv0E8ZO1focpJmOb0%2BaN0%2ByFF44BTiv8hcpKAwEMsEKexHneiEKAa27pZNwVUd32Z%2FAKStrtEBtXlbbizGEzj5baway5mftpS4LancJe%2BcOWMLoMf23HPOgX3aIq1Y%2BWstBuZeA97KCrD9zd8Z1WUpX2DQWcKNTX3GkZuaCSlSx8VHpxpkoMvAfldoE6MQQi6cPUuFQEpCyKFYXi270oVJtRuAB1%2ByMamV6s5i7SwR%2BZOE%2Fhf4jcjP4JRyFK8dTfhq3n0zU19J7lvWCkMCkcnrZEZ2BCfwHMkx3yAW7QX7CvbofSEc5Dr8ruaiRYu11TKk3kRka6ChLL3m9TFU%2BraxnNK2H%2FJdOGXpaiOaWtaOcrvljhc7q%2BEqeATDdWuzeNYd09%2F7eQO%2FHLzkol%2BGMXf2NfFsJT3k1vsk65tplvlUXBqwVWVz1icGYHBpV6uwD5j33Hm5fblkjlGnCjQiNH0kRMHPgt4BTKb43q8%2FcTscOI524rvrQxlqGoQ6r%2BuE3xahwZMPDMSJhB%2Bhi%2BcgWkyb0stNMaD3aXu2jsnZtg24aGeQS1pdSgSe4v4d9qDhcgy9nvQSD16sMOMNrpuNUGOqUBpc2gUlgKdxfGQQydeTR6QHMDVeO7St8SkF3JhN%2BUf2UCPA4CUImdf8hF%2B8im1mMU%2F%2F4SuY9aocKU3UOGGyEAoC0jtK1OXzonR%2FPn1wA9O6pi1q4yIiYtwa4BhSnk5nfA7AewzGBcpMR%2Bz6Jo4DJjlTiODgTzlkv8ZTZF0nlPp5YHxtiFopQH3Y5PYnV3OQrvBkhq2GZ3T6yvVQ9n6LyZI4JXixX6&X-Amz-Signature=007e3ac75324452351fa9b2414d5785bfc50306ccb11b59698b06946d7f7de92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
