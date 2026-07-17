---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2ENJPS7%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T150531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAI%2BmRbaJUxi4pLxXHs6hO%2BzQXMwKggLc73Zl9rgdD%2F%2BAiBPBiwWd08Z0RMmtkAikcsaGCSlUSUEs1esATrCwdfsDSr%2FAwhcEAAaDDYzNzQyMzE4MzgwNSIMmclYjzPPke3Opfs%2FKtwDPygdLeB0JSUHnfqSqSkxqI61PACOpu8A458smf%2B5oJJgWOf7dXcT%2FrmBqHrNogKf6th8freeMxKON1CFaCCyZRolVWNQ14IdGTruz%2BxBG6Noc4NJq9jAkU5w1V%2B%2FohK4mLAYvV2HSQ6qPj9HQ7VcjGvgANrmX4cqcs848VTF%2F9LXTFuPAH2c6PgeUD%2FVo3Cw5pZHBXxje6BL1HHFDf8h3WL40Bhpuw5O%2BNyj5jNTpTqpXQKTZVAa2Ihdvw4cbh%2BJNDo%2BNsyP1SOT3zUSpRjJejs3%2FoUpJ5hn4412WE%2B5sLDwneU3vHPHnc%2BsJrnRhNhjms9iDq9UUnSUAKbxNX7GMcms5E%2FhZihxPl2uTRx%2FcrCN71VOzdnsK5%2FQ0OmjBidJOsL15yrhRaAVahyt1b9i9%2BclKiXjrMAd5XvSU%2FJeg90qVK4QE9bBLbwiYuO6gkRVkeyTdk6nJB2tWiiTLi%2B6IeJDRTWvbguscv7Xm3qHuKxzLNyq%2F0zSBxqKjC27pRlC2pK1tbNob1XfTgW7c5qr2LOekZZJx3tiFnqbFeYRpI0cyszuM8t1%2BQTmTD8bHyCCWFiQ7JIg98DDhqxuzdIOKcyIuJvi5i7khIW4j8tx7Uzk754k5W7p30WYa2Uwmono0gY6pgHJn%2BWjovNPVh%2BMPgPFK6FqmGcU4Ug5J1vYhdkyxWeH%2Firl2Zu4ivzCQJPwX7griiJKmwKfQjK1PuWnUoM8imcCG2oZ3JWwHuar8gOjKEb9noPD85mJyqR2cU%2F97nN7pQ%2B9Ltcm7UFdCD5N3fZ49peGL9%2FoEnmniu8xk6u3HzsM6dTg3Enasv5Pf6q4d6TPyfWjsYEnc2Y%2BEa71iSqDI%2FL2Sk734JqE&X-Amz-Signature=bb700228efcf9e7bdcd620b282bfa08a097c822a2f6fcb15b7903386e57287c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
