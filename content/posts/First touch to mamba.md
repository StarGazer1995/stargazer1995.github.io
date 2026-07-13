---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QLFC7CQ%2F20260713%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260713T190931Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJHMEUCIQCCkeGiqDf4GMQXWBbNd0JnCoVPHrdwhcQMD7UHjmzzlwIgJmuOB1HqQRew84JVmyrRWxOvH3ttwQuo7YBgwC1%2FdgEq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDHxtpAsCLWKNOANrTyrcA%2FYkv8AhEPJhP8Lt%2ByNIO6GIqldajFDql%2F6IJTinqH%2Fa8CrvhpymWvMAtt2PoCD6gbLYY2wcKWupzPYkr1zlNcZuBXIby09qn2RX%2FfcFRnj0UferR0jUN1Uikiz6mgL4Kh35BqH599pAJVmiZVzG%2Bm1ROS5kRhtcVEiGPZC5Jjr5jlb6xvnI%2BRHR7zJ4aXBk9VR3HAMKEiZstYLP4l9%2B%2B4zT9fHB19y0irRFrQDYgi78g%2F7G7AOEi9Gc5tF4jIcVghwLuavxroSFvku0Ham9dWyFCvKpAOUgt0tgU4fjB2q8gcUY7hrPOjPrhddwIo%2FwAre5PXJqcOMx0SL456tg0xHkoO6OkPdYbZlq6vdq83M5jwHTv7tzAeaz1IjombqQVNd08GMd2NEvEpyCavtLadE%2BqHAv204Llh1NtALtcfq2SUoCxp0yGRt7SxvNSBAYPiZpqpUyaBnC2M4sGrYcdUO1DCFo9gj8vVV5epSNNXYDqUiC3NbAr9lgah83auBBY8Etq%2FNp7%2FAwiRUTr9SCEmpNW00LUNqM%2FmmCsbLZYpSpE8Zy7oTM1YwahxUnCw0Isall%2BneuQ5iNUkjtYY3um4Qe%2Fjh%2BJJZqEYWn5imeLnHh5V5RiGgsXjrJGYLGMMHT1NIGOqUBKwB3VJBQ710gDo8QR0Rup1dF0%2B3IlI1sN9GyjnDtJa%2FCoBT8saZkc7lrfVGJzbq2f%2BF5x%2B6Qs%2BfQ5fnCbNWRBjRs%2BZjLepSEQQpFQsSEmBbG7vyFkVbv4nUMYN7zQXI%2FQQvbkhq0In8KPX0MbkJr0A0R0CjHeRoHRSfGVn84eTcAi5K0yPYfB6ItEvQ%2BdqeyKMvxVAc4ih1vP6lm7Ls2kWiPIbNo&X-Amz-Signature=42247d4e4ba409ca16a6104fbd72b9dd6074dbc769fbadcd7a85adb4b13bc9af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
