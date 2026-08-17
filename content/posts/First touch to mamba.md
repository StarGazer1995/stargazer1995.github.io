---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEH264AN%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T121913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIHockPxrlaSNlcvPsA3NgbrddSBJlcsaVF23b7TLFol8AiEArJ77Lreez16UO8l2djBwRUA%2BtnYETNFMTCVB8QLNeJUq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDLfgA5q7BKGCgEhSCircAw8zJYgBpLU8WG7p8YjPO4YNYP%2F2GyfKUDJlXZnX9shP42XxtveUAiFXnwh9fW9GD1LZgum%2BN3tik6BbCn39ljQpgw95EeYUsbXmd98HjkX2jozqJ3Suq6BxklgIAyrNiQfuw1woFMJLI7CWPA4K%2BwZ0HAjHQfC2zgFnqrH27Ou4Jd2PRzwfcQlpVA2PEtND5wCBEm%2BO9GLTmKouD5b%2Fhs%2F5ayZPAHDVo6PRzpZ7ebhFfYEmhHbq2ua1%2FWTUgitAuCfQQPhmPePGkgLA%2BqfrqGJM2GztNdvJsTLXcZhvaMqC3OWiwfC%2FHGW0B5EAvHuJcmVoqSlO0xnCciC9aBnh%2BlgjosRvqM9HmQTtidiDCKyv35Szyni1Abd0oDCdJ6xrwcJ8%2FzC58JoO4%2FCglSMPiiReLnZ5jYavS%2BESmNLFzoZuvDYQgghHreHBaInEV%2BEeBYz7K%2BaynwDOuaLFaewWIGyeFnreMZNExiNN6yqjrID%2BRtOg0pRKnodopl%2BVn8t4FKmcdeMzIifY03%2Bo0D6841rLvj4opF5SaUKUfJcAlIEO5nsWDsGMJQKK7xdUeK0rwzaY5ghuzHZ2LbzhYsGn6qBd273UOlQ35CN81Q6cMxtrddls2bTLtdEAKipXMJC%2Fi9QGOqUBBtzWkGKbXWD5BmeB3XBxmZclYFETUaZ630uYMtzjN%2FnJjQl8BTivQ7zdtS2a0mf3BAX8zod2SWh1LEFX0kgpa9O7%2FK5NfxLRYyW3b6DQ84nh8g3Ianp%2BbUMra9LBserpb4%2Bxv8gvA%2B5Escm28WNCjF%2BFxfrGrmVaOymQ2LZkRq3wZzV532eJiiw4vnksfISYQ8wrLwBeYyQ18bL3tNMKFxWX0Hnr&X-Amz-Signature=d23724eae914fad29b391ae4eaf49d38ceca245236672cf2f94476b7d231d107&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
