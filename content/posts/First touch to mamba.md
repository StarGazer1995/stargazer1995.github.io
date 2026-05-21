---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665I5UKBGJ%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T225849Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCBESwhncg%2FMr1e0Xu9zMRL5dkLnrJ4ViBR52puKIu18AIgOF3y91CHYitfmHsEeKM8YSmAl7zk39Ts8Qtr2JTAVwMq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDHfwbnf3CsNjHzOTpircA3m0uEMa5ZJZqaNyk5VduvbqdGwNv79RhUUK132rn7rAbvDI8fdHiMGuozMdKMyEktrbB6d90FjXEr9YqOBWyZdivQwOhBer2b3tCyQDxf0zZ1TJ1Uk0JV3YUrGjn2hTMy7SplsGwAN9mKdlXSHQ17RMyszNltRQe7KPaYMs%2Bylfig2a7mibGby78tlZBlnhNOJINGK8qjdFDFYZpNihP6KbkATACT7MO7xUpMTtWOrDWUn9xMQdf%2F01u1IxCv8bJtKVscjzVGe4zg%2Be3q9D96Ii9XVzFpieUIEGJZ8UGzz%2B%2FeI6Jg9%2FEmTErdIok02EYNg0HRF5%2B8NsL%2F1ZmIWJnplh8QUInxWxAd1eXA33RqjuZE%2FWyyxCZKEZZMvaiys1fGjUatYeBfLSSQG%2BFTps4J1eQ2tlp%2B8HR2%2FaUHCTADVo5M8KE1DN1m4jKjNMMHuUeQvK0yNGsrw7M5%2FSQF7BFYm6r4XkepPtn%2BEX8GDLwZxBLUf7aexfoZ3uXRcb6b5u0Vfvz2NWow8%2FbHI2YfT%2FmcWycAADEqZGMd5JodTVJ84c%2FdxEB1NOiilxBHIRIPUjYR%2FiEo%2Fo7ek9RG4bQXV5ZQdUIckcTijRowNE89OOPaOtxhjGDDTxNyj23AY3MK6BvtAGOqUBqJyNJXM3Bj%2Bk02zNH7M0dwu4hG4XbB3bo9Z%2FPOcUuMAV8h4FzxOhUgDdZkcO3CkrSis3DM2FTPiYyh00yuoVC8e%2BSZUw7rVBDcNc4HPafqRhbvk1O7WVPa1mn%2FM34iONMeAxffevzkuZQKH2JdCEWVpwMCgPpbQNKqpmRW%2F5sZ5j6CiPVIkk%2B%2BYyCTPyPTzvDXGhcTSeSLLkxwfWlOEqpMgGau2G&X-Amz-Signature=af8f0aebf5d35fb72dfe88437f925b540b78411b558d45db8e3ce270c0832df5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
