---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ6Y3GOS%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T110446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJGMEQCIGx3e3p4kbg77RPHOcOQnABrp8KOvl8o0N8ioWn8J1vcAiAFXEylJO8mFOKd%2BYxhuwqXkWvT%2B%2FAaB7fzHidP8jNZTSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMgfb%2FUeHqsdsRd4LpKtwDjCeTVwu0cIWB%2FGNIRTHRYmFZShCd07uEM8EpmLXVtn8p6oHB53E2YYkODmZH9PGdfAsylpJN08hFlMIU5OA95x2wQdJd5zw8AxOGdiY0vL3KmVIbbV8ohkT62Lx7cWUf136bmH1vG4%2FqUjITgN6EDc8fLocC4yH3goId0%2F9%2FiEwv6Vm%2BJoGXobcMKkI2nM7Eu3aDgpSR8dafkVpEIgAcjTCn5VxziFK1O%2BEm%2BpAll9e8YAlBjDXWOW9REgd0TMCwEyrz6kKqyfmTG1VOUmcUPy4VERmuSjVPyv%2B7aY0aCnwoAKsqPvWuYALj5EQWjerEntvF%2FM3ndtHYfqqoH%2F2xiNIMft%2F1byL5A%2FCy1nTW%2Bsn7G6TtK27ERRJ7eGahtRjERyWNu9fON5cuLgO%2BfrvhEWWJIQbJG8WnYSsGDCQQq65e35W2Vc1sPJWVQ05k7zerrSzTgq5pP7uIpw8uxowb%2FY7JHXi7ovFgnRAay434LZqTqW8NXSZcc6xCy0sf9vv6L1BB7PBrxeWrr27Pn3LRvttcHp13dYNhX8BeTuwr0eKy%2FLVbpmRizFBJDkU7BeaJ8DtaZrZew7Awf02ILk%2BsIpD%2BwZKFJqzic%2BrzRspM%2FZnBiIQ2EOmb2mX0kzswzZLG0AY6pgGnbgb0GW%2FvraLyMEzODk6Gq%2BD8LN8prGhC%2Ff%2FVr3bXpRm8CUTRFSP6cZZt6nJ6tZ53aQpm6eg0SeTXoM4Y9An%2ByYkR%2FowgjgcS2tRVp%2FqV7QTSjtp6h%2BEtS8HGUpor3rrzZhW8qY0pYlgsvR7Nt9DQJ6k%2F3Ni1CnWZBvoTFaM6MrdC%2BgNA80bxpSBDGr5nUKHMf9PlMhGqHl6L6jhisF3Eu3VdpdMN&X-Amz-Signature=597367c3447e6b715feb7e1e13f685ce29cd0cd52796357ad64201dde0208f25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
