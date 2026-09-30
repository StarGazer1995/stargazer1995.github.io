---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIEB3LN7%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T142129Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDKHEH5%2BvRTZbpck4ETDfUcJw8YyRK6FcMYr4KUm5gtNAiARHHAid02KjZPgOmI1jWvESJs8eHk8becoYxNBwhdgRSr%2FAwhlEAAaDDYzNzQyMzE4MzgwNSIMHaSgzSaFz8zprsXwKtwDJAQoCRQWUw3%2F2oJN9Xm1ESzQDuPg5Tc6U7f1DVdeUWKrBYc%2FxGPNopWHDzi%2FU3ZL7SCgVIf3koRc9BtvSa9S2UVu9%2BT8RzlVrLHlUb8ugyPlrP5BkIIUCMwMuC3ft84gB9PrmEEsZQe5u0s7mg4bTxkTRcM6fsfYcbCK6c%2FqT6d3fsAqn1B%2FFE3c%2Ftz8jo6JJjuNR8h58ZGQ2Q9GwfnFqlJ5dcXrLtWXiSOHrIqZmOlUjTpa0d9Row%2BtvHL0mJCWYtuUszCqraj35lQ40OzcfO6XEu79tKUFyqQG94jcuWbFh7k%2Bm5IARfPLJGNyDXFaw9PV7wzNKkAVKVqd8XPlkvdDmBfvn6zlo6Pw5bDw9cJZFT49AohkVNwv%2B2B0YCrWLrH%2Fd1tLT9YrXA0yyFGN9JoXhnj0ip03RQ3szkA1D8i7qHsl%2FJzvgyzqFx9zLs6v8TvsFQ6NN%2BQ%2Bw1RZVjRmuxcrIDC8zH7yfWkeIe2hKjNg3pCWXXrjyePNwVrtv4RPDagZ18E7EPEEldBnxlIveJTEQI13iOjfoMK%2Fidq6%2F9iY%2FN8puPiC052GxijI5eaDzkzZVmEkvwWGRKjd1%2F4dtwEvEQqm7UEqPkKFFvR17S%2BIP1ReWKgoLOraEPQwpoX01QY6pgGZ37%2FCi%2FkWHNI3ngbL51TOEYN8zNfClZUdaTgH%2FDQTs9MvuSrzCGGsmxyhpB7HelbheXZgsxoeIWa%2Bl0Z6pDSLtCPzfoSqnbP3TPbE6ep05aWr%2F4E8fmIWpiBBXaGCGkMc6zGMhhGDmKpDPr9%2B6XhFazTptkErHuupmqnGo35WzIppyjj2tcqcgbqgyU8Y%2BYrjMNzEjfT7bPvD5SrhOj%2BgscvuvjGK&X-Amz-Signature=4478278b5b38ed19972680dfc81a91cdbc04f249dcd4ee36ed38464c3908563c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
