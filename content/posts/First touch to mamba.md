---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XE62NJMV%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T190300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtepC21C2iw4KIIiN3mGeG4AK7L1pF0ROibt2HRS2UTwIgBpm8bcF5Q1ghv%2BuSXQQvroLxylVQNArCUptrJ3%2BlIzMqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEk2gkEZUFgV5RvW2ircA%2FcF2rX8Pc7sAPcxw%2Fb9hfoI%2FMuKt7JBMhiXMLyZpSw6VNNI%2F7pjLV26XpwZE%2B6wmLsZnih%2F9QJTMMZDLTeS5O2iNLlHTmCXqf0AuRTAbC9oNOK7NjHf3UBBehpSz1s7%2BILDPIsGyLmPnoQmzEkVpgBaUZTrLFipaNxBmYuH4HV4jqI6tMUpFBpU1WkL6abiT3%2FpbeFou8aPNbM9Ka%2Bo0D4JDClceRlDaB5iXjHbVyajLYuKU6zlzQ0aiM1J4f66ym4W%2BqbojANE%2FmJrB5peZg2v5KDcVpFuvSJ3fM%2B5ilcMBtK7EX%2B1bPj%2FS784Ma1Z%2BEcBer%2B8MD1Rqp1cm9J0Mm8dyvKdblLVc3AgQ91pLaHPBiomhMTGfJux1XxgvgYeUfwUen2OvORQXL35sFbbpNQfXomX4YDvJ4Hv%2FlHxiFtwsSBSwuFZxzPYh%2BBnmZg%2BCZKarQIslitd5JZMGd%2F8v8w%2BwyVHRevAuJjOJb37NxNQd6GQTl71%2BPb3ZW6P2THit7hkpPO5jWhxXzdF6xfE6I27ybU3XV%2BuzfnD8uwbNqdQ29g4o4D%2B%2FCr%2BwBBlSlKrpvVVSL5joY%2BHp%2BrsQ6rhR7ARzsbmElwkoBYIdE%2Ft70AHRuPlL2ckQvFHyxt2MOfFkdEGOqUBJHR5XnX8Oupnw2GIFLHre0f1s9Tem0wlsAh0D8iJ%2BY3NncN%2FiCUaarI5UVHC68hhb%2FD7%2BW21FO5caRpzpmFKnxVIc4csInDiscQON5N2uniCAaGyr3NTtw%2F%2FLaZwoy8oq%2FcQOvFmds%2FLS4Li2L2OFVQE0izxVgKzRmnm37t3Ll2gtmjZaOdkBSX5WxZXyY%2BGXvXzuKX%2BpU1FxAKQsfGKrUIjoNTh&X-Amz-Signature=196533fab8227e02cc88181dc8984bf87a8e9cd0cdc258e61344d98939fa8e61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
