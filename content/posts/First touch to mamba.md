---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DBOMFLE%2F20260715%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260715T185249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIDhqnKFrnyhlz6zN%2F9TuJv4Ojh0KqLqaJb0JpYlN7%2FaxAiAX5waWVfTvJxaCFLsHWk94v3g2cMQYpAdVNP90LH8DbSr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMg51DQx1C%2FSS6zreqKtwDw4Ll0%2Fj8l%2BqKRehq%2BfYQLE1hEXyH%2FkqQB%2BrpblbmD3%2FkrrI4t5wcw%2FR%2Fa9c7fW236KCyuP7Q22q255QvXGYL39vtceCFubKNQxZSUqNl3t292KwxXpytsi6O0gAw9XZnY%2FnACDLbHGTbk%2FMEVvYrkcL0m%2FAfKViDO6tUbjOOWiYdZj%2BV1gVX%2B98B5oIS3Mf4DyrtLdxIsLgLjpc7wPsNhqTwTfe3h6Z%2FJ9iTSKnDkjhet22BVjBDOvkWwX2blWKV22HjYxXO4VsKgn5A9fyNHmZuF4cd%2FO0%2BNoL%2BcvCeJjhQwjvMJFeE821ZKKwH4vFTQwCvjnLZLvDPaTi6XOPcXbsYRRlqlJOTtRvbx2KAeVX5gRCaZJM0e1C00JQV6EfJSk0g52VRoJqTACrAp0Uo%2BTx1GiWj2%2Bt4wQLaIGXGhrC6pfSmDGMz4tRLoDFNYgkK8%2BTLcdQSC61uPAL8kumFsqOx%2FAFrMxBNWzakvMpayTSEKFPpMyLIDsXC2BATEZBQ69WfbOnD8jlbttwsz%2BXUzMU%2FhwFPqNIOpp2lSsI7jr5TBM8%2B45c7gRDflAR6KQPqd2pKgStQKfzETt3jujzyD8LfD7SGA9pH6xjlsl4RvryAhPQ6mISsqOp3%2FUIw3J3f0gY6pgGtRmft88lfgfGdJqkG9KZ45S1prYoQGjso%2B7n6cVZ6xJXin6VKLYVMC7y%2BUir55OV%2BKHXlL9oFw8xmcfvUT0afMBQ4%2BbpIhdfR%2BzsT899rZbih5fPS0B0uoR0t6Vs1U%2FGiNUctS4B8oIfclcEjbie9JbFcSEY3klYT0KS6zTm0%2FWsFxb64GfjuXTLVzX0aD1wwBJqEAgq0s%2BRj4uDScJ7W6Dfqhuoc&X-Amz-Signature=644f70929dd6696d2ebfb5f7b0bcdbb2672b29313472bbf57f257311d1b63337&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
