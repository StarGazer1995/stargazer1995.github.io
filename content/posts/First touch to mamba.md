---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W72DLORH%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T012549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCICJYrhREftvWRQxNWFd7yjlMARthv4pW93eBTpsMyZBeAiEA8K5%2BBaM3cKjldRpWypy9GTpv6VKqtNJELSeI1qmcZRwq%2FwMIEBAAGgw2Mzc0MjMxODM4MDUiDFk1c5%2BtM3Q5sPHVQyrcA9TlWEaBegZMyfuWqZNGQZ3Gd%2Fb91xp6o3J3Kxh8DEvCC8r30A0m3e%2FxXF7V8x%2BxMljrIbcVYqQNMK8%2BzUuovlbnbPYZpx4IZZWmzmmEbwxww%2FLXVf%2F3%2BECCRv%2FPn3CkTS%2FCAOS6oGYfv5i%2B4JzeIUAvEKF5FyfZ%2FUec9XcvUoJok%2F4qo6a5v8PcOsq4Fnr1hoOeahjBk59DipWye7D6vgs%2FsbJokpLrIIm8w8IFM4s4cwoePe2AzH5VCg7vgRWjki4eJZFvziK4bOJOky7OD8zUSAFt9z1fVUcx%2BwH3dQ8Q4QcUmPFFJnGdnT7uOI5xkIU%2FJBfGN%2F9oGuVsxlaPwCPHpkoAXJJtkfFbc52d0qTCo2Yt%2BEmQUDBqOqFMA1mlboYKLOGCEjyYA8IBW5ZPRw%2Bp9q1St5yzNcPJUD58XJ9i3LMa2U8UEr%2BN5spYwMYVHDWN5ZsrcvNyNlHGbIfrYkNNUoOLi01VS4%2Fk8t4YsvszLXyQy35zdoqhFdMMePp1n96fBVqAFXiuZ000Hal7DC6d6M1rlIzO%2Bd6%2FOOi78LW5oixegDclr7aDHL6ZDSkLXDBXBzdCHwg35iDQoYCto8eHs7ff%2BkmRVGRZk6Kt5U0tYwgqLfsU8PwP%2FsaeMJjoj9MGOqUBESIK68cAu5i7WlYG9NRdypVRPJoe%2Buy9EfEiKsX8Fv2CvlWIsBls5SzLNXlPijMPzdaxRtJ34SoprklEPYYl1sJczeDuEHkoSkEfVLNg%2Fmle3A71Tb5BAQSAnwHFQXTRpoiOlyMLAyDDuMyo%2FICmfEFXvIaNOFz0Enx4V8ZYLA7FS4rzPMggiq7sUN7iZdJx1t%2BMIhaSpk4ZzHF3WjWh0z%2BE4fAz&X-Amz-Signature=199be5ac52456c8dd1183d10f08dffef063624cb8e84cf17a0cf555f9a68228e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
