---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LAX7XU4%2F20260528%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260528T214959Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrOSFBNHco%2FQSiT796uXwNIu%2Bq6T76Fbipp1RPlhOwsAiBygtTEhsYpNjFmhhKvDVgsESvPviwf61Sg64GHhIYcgyqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjhkUa1UKoNc5k5OzKtwDKemvrw%2BMussdcV1bDn%2BnddAAQXVB1v6LR%2FwzzPlO8Ecunze6zyuBeooM%2B5J97O73Z0JWp8Sqynv9Z95BiYtW2%2B3oJAC9jMdATpJ%2BicmGClT5FVXS%2BF4Wh2OMEwKIA0d8HJPsLybgJeSi1JGuO3Gu%2F%2BMsA1g1AzQFcFrEFQ4WW5EvwssAL%2FHpx16ZejwXM7iIQN%2BJg5q7wWSRDWsSNrbttAkDBl%2BPLQloVOYT34lm2VOI960O20BBl5CKVUAOppmIGKcaFSdgIMtp%2BOHhB98NOKvnhZZT17XXyCHB3vrIEcjcky2OoYViQSwanahst4mFiPP0EUmM5HTJB1DcZoooTMuH5l2zpWEB5c87TIAPBQUMYIGoGxz1Jov5ngHjN5h%2BA80sOIHmeF3jKoHTBsjxg9l2mmzVhledBd3vuPe5ZzoCtKxFqFLVSIkLYKHC8n3kp72iAhX2PhpyrIY%2BY%2FDWtaGlvP1pQtZ22jkCLY72U2rr0yInte9%2FxDzaCFgWruakebBp8VS3A0%2BR9XZVdgVKiA4PhcwwzvPQvBlmEFTGe9tfwAxr0k0SRNJvGjZVkMPb38UTwnyDQY14lpZJwYe4layWMfogGXmHRROex%2BBMy8QpMhu01P1WrY8eMucwkt7i0AY6pgGYiOE064AY4rx56aArmueAnRjV1gHTrlHpHXDS0VW9BJ1W8NCSw6TLkAOa5CmKpNqApNaft8XnMnJIoLVe34Pd1qdHMtwdn1jXpctdraAuBVvAKYl4T9wZJ68MiNsKlcGeG0OdofjNQ7K6HwL%2Bf9SQf8scQvvz3WCh0P99KgV9xBfAoG7hq%2BddmjhbjLXD4u3hgHsR9CuG3Cit4RtbX9i8UjRMUold&X-Amz-Signature=44953bf356eacba9c5031fa4256f3963e2d8ebe3b765ab22e70f22794994da47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
