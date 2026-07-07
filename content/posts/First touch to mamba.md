---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TM2TKMYR%2F20260707%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260707T211423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUCk92XNjUa3hp7UwwK7nsOC3aPx9F6G1XQNQSnHCirgIhAKZvnI8vorBQOszn71B6cbYGpNAGpfqmjUWys7rTtGWMKv8DCHYQABoMNjM3NDIzMTgzODA1IgzaOHidkSp%2FWRZOhFEq3AMzVcf7nfr84bhmEZLGD4po8MTZ6MjFftZ7rrlF%2F4CQUKGS6Txuwtd4U%2B3ljE29EI%2BD%2FhSBQqKfhOi4oJW8mWpWFFQvUDmj%2Fsz4VPGT0sRl0%2BcAC9ayA%2FT415A1uS1J3BRx16ZApXqJBLXxAiM2oKMnoT840IHDhgYaK9Ns5nSzXkAgGwKmC7clog%2BgLtT744cWefRVWRPiTyt9Ls0u2P2FM7CLYcT0dWVUzSP74YQxirtGq9zl7NKd8NWHGUBwaKJKEKqsy%2BV9t1J1yVMWhSVBlFiBzofhwPAiKZOF3vUxQpdCEo3BJHX3PqnoXzQih8NttmYOMdjESfJVQxCG61EBgtGbR8icoY%2B%2FDM8fyN0knEqbLrUryj6VgWFY7hSkD41FA3lH1qSYCrm4GIQjkM3E2BQdO5DXOutsEh6avlVhEkwgj9%2FFM224ZXRI%2B%2B0paa9TqpcnmhgwjCh8kdJf15FzUySL6%2B08SY55b3z0Ua9ZwDlU6ep7vOcDj%2FwJzvd1ySnJZG4jdVwUkW2mamzpLYIII%2FEEfhu71icCCyXzQgHcKNUqcQBJDeMuEBuh7h7To%2BHdUyrx%2Bm4u4XQEiwoRJl8xVG7GFD3UdaZIKxOnwCIyOVapSeRs%2Fjv%2FDvuqSDDGy7XSBjqkAaY2v7tNHgwJ5%2FKE%2BWvrc%2BSdu7ry5oJzxaI39ycZDuKdTEvQn9ELGrnaq5v%2Bi4BgxLIJMQzq%2FvivbWqaTsIuEIff2iWcscFBfHH1KFo198xBZukdOnZb0BD%2F8ZEdQdZJouNG9nXfcF9UQxfNvxf527Klop1y27BoU4i1y28zVUf32TTUSAhefM6rEoMTws9nxv5WAvto1oy3a4wwZsvZ3rz6ZZ72&X-Amz-Signature=72d57337055a4d7ff3608627050307eb26fa03586cd6c18e976377ac625a0bd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
