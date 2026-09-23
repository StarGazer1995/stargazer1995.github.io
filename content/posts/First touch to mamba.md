---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642PXUVXA%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T223256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6qR06EQT0LNXbbvWa2LMNFRoxW8rJDBKp14qzsqL3nwIgJ6LzUNeapBxsaHSrwZPycp0mAkh5veSgzSSkFU%2BJoOIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKuA9Z5fr2fBMefLLircA%2FUhYZwLB0T5Sot1rNjulxp%2B8NsdSEF2%2F6yW7qAwvW3X6yQdNxYnQBRXltEXOuI8whIhQAq6qIzhmHmL9bRVrYt2Lo8JtZ9%2F7o7ouuRZBGRqvIZV3TZjr9QsiTKlEG%2F96y0arPtzRJ3uOPHzY5TOQOqsRzOMSXhJgJ%2BWK6HCoX85u4D%2FceTH0sdS5hfVa2cou5VJP%2FZrHh7vw%2BFv3%2F%2FVxoACO%2FjUA0VKuFWU1nPyq6IPg79IQlXwSbHgM9ovMYKcc38yIpmjISsXthkib4X503Zqa%2FR8dkiZ7kOgc%2F%2B5sBADmw2HSowJ0D21o%2BrW2fNz60YQrqTRwfFXH1r19PB%2B4TnesO3kndDawR8R1t%2FMCjOx6fAyeZ6lfEdHu8gQnaUB5MjLDtUx3wmUcMI2%2Fmce5usu%2BCwbkJ6CdpN6ju1UP1Ih5OdCKxmUS9g5%2B0wDqreQNJ5nddg3B6u8ZlQyED11ITKPVjBiIx1aiFOfWKDZB%2BFCIa0vus9vLfEt7WEIZTlAB68nepybMJZ5pkgrOqmmw%2FVnwV0nQALyiR4rXibbCiYbq29FKhPeq%2F67M3p6QDEtRGdPCje6TWIi4hOdJOemSxGsKI%2F9TtvqoYedK%2FtuH429p0WDe9wjTZDS3fVZMJCx0NUGOqUBbqGBNSvwjwuaM3SVrxzfzgsMOqBFduo2ddPEYK2qIjNu0qAeiFdzHoFbyP%2Fq0E3DxKnf%2FXbKF3Xd17bLgu7GVScEcoZFgczXxM9DabC7j4SYkjVxAoU7L610D87Npw6UZNqfZTqAKuX3dd3b3hj1kcF0F%2Fu7HXZdtMQ6Rjv6KaXqbrulrxOn%2BwwqxjFuA%2BOVN481HTBRChsX2hrO0jmN3%2BkLba7c&X-Amz-Signature=f27e5673a0baea7e572981cb883da684d1ba82190ee6341fccc9d72452bba82e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
