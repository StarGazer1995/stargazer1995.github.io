---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HCJ2FD2%2F20260522%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260522T020312Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQCmXRedByU%2Biijzpz8y7EK%2ByTVQF%2Fy48PwPoQCYqDSB3gIgffQE2oh7fFCIgqS3H0L5fqcmUaTRZNY%2F%2BDdO6B%2FY7qAq%2FwMIDxAAGgw2Mzc0MjMxODM4MDUiDH05vEx5xHF5GOSKeyrcA9XH33%2F%2FeQvCcaIuiND4htOgQj%2BQvAs0%2FVjxnwTq6l8iUolRlcQtyHlC5hIi3TPnYxhKNvQWbXRmGFK1hxuXW5MkS141anXu3uEmk5CNHeV282dhb5mq%2FFax1NZCqdjN0Rvp8XXCD5PLjwsUmD%2FMu3srAHqHsUQsDeLZnheLl2CctEwOGV1Ts8YubmKFCePaoLliU4zGliPXW17KFwPjd10Nbbw5C4sd4e%2Bouaxi0XdcfTSzGdn9I7E3vrull6efNqMkexPYoAQTuMq%2F%2BO5JbkMj7VZoHYrxwNREHTDgWiWD%2FB2isQv3Z7MCo7yqzbCEgrpFvCAWIWmKnzhULbjs10H5uSgmiBG7YOFbOzNJn%2FUnhCAlf6Nat%2FulNZVVtPqAyrLadoPxJfYVNMIW%2BSG7Sc07hFKdce2LIzzaSkUOKLTpx0YvOTXlO5lwkXMck90LbBb2RcvmB0iN8kcOp%2BXRAzkvEWz55paqQIX7RFmpCXjtTRoC3lEB8gLtjg6XXpaP6i7RIsSFPf%2BVAGWHBtU03kdHWI%2BDDjR3NYddU8Fjr1H33LucFMc1wninhoabyAhknNQhE7N7r1Q6VSR6cmFppz%2F9wiJCZz5kEE1DtUj0LFR%2F%2BkKBal2BgiDE%2BAyWMJuBvtAGOqUBtOqhMUhv%2Fkp6LDjYOYzD0QapsGCMv6vSwshTjHwrwNDGJY417OL2mo56nSiNC3H5MKPJMHTflhd1dDJEUpD%2Bncx9SVRRkLrLzO8hfp6cKxy0mMt9W3M0qjwR0F2mAguV68%2Byy4sIQAbtLQs0mU%2BOB6EalZxYaRSvycicd%2BgjjBJ386DpdQ0mjhVayBLogEnzV5UEotN3tc41M%2BP%2F5sTQHpubr%2Fgv&X-Amz-Signature=3cf104b6a77e8520e979265e308b8337d4ce82bfbf5bae14c0f1b56f9b290d9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
