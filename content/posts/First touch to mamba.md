---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROO5YY5T%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T084511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAL6YC142ZZtgu2Qz6s0Xn3h99PKwoQj6TOOZStrYTqVAiATGXK290oXE%2BPvGAUO8OLbKtF9fDJy3WT1hGKiDgG5TCr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMKln3WFojcHXDtdboKtwD6GQPCG8698J8ekzVVNlsctKEFYffw3AdABjSfqA3Jy8hXJsKBVAqQ2fZAKzA6jgmeYBu5ffSBOG9hsiX8%2FsVGvJZBEm9cc19cXBuV5uI1gEYzMShmMlq8IIpMZXw5zE0PBn7x9AibGTMH6Z75qq6cIyDMtPOFBjpgA5DxkXTeALVGdLSJZnkCuggsEgleRMEJ8DSj84YGupDVlHuN24u8Yn0rPU%2FV2mFTylYrHz%2Fy7zKaDyz5MHrgITkXrSska0HqElAjQtDj%2BzsCEPCdeK9WRf3WkZOSryWf5Kgn6LA5%2FZtXQ2jgQU0sDeC5SgZcgdoxeZw4f%2BgDbr2%2BG2EvaetQJFDmvS4Mfnl%2BnKMQU7Ya5NDsX4IUen7laAEk1oVi2Kh72XUxIwbOW6ccAS7%2FdRV1g0ASSQM3E3vMiZlyb2xkIZxw7ciGygVYILqnGuifLwRbBKk0ZTxUq%2BoTdFPPFgvRjHZDJFZD43VVHJeAG46%2Bzhajb5tKtdWAL%2Bd8xnAJFMwSZDEMWhz6kQXE44AysjDTgMEj68c6XpXKifqxjlheRh%2BKP2cu3YeMmjxas2sf1plWtNMXkqo%2Bu%2FU8RiOUNPX6X9xQ9FWxAK%2Fwt5MNBXpsUaPRgcnWtCzuZ%2BogVowlY7W0wY6pgGcIX3bUFKGztYqhgu4QB0vt%2FAMlbZpq3wDUYoC9Ir78NWKa1tlcZDy5YfvsWruBtxa3KBrTATkRwtSxtvhq6a8aQNMQ6T0F3iJz%2BaSZQQH99w9O0SadhEiFBdr2eV%2FDsbP6z8qFsKVlE8SQoELQB5AnElyTYZ%2BeJDmlwz0Gp9Au%2BmqcDukoMO4bZHAU1aLhqfM85EqQE9dRDjWRWyJIuDiyeMtMcw2&X-Amz-Signature=e3fc9f023e9f20172ad372639b0aa324106cb9576722600f318031d67163606a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
