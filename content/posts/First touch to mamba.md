---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GDIKRAW%2F20260720%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260720T192229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCk%2BCAuoSqm%2BJvviNUpLgjC5XMzHDh3Mm9TfdXoREThLgIgYxPAB7G2M9a6LwL4uJCLgGqOqHLLntLUJiBF1TB9F3IqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMo3FoSIqO70JF5VSircA3SXZvDRAGmKY2%2BtMLkxeyj2H77vGyS25S4TRdje%2Bb%2F1RRyoPI4xZu80R2Yk5%2F41j46VW%2FChOLIe9mElZ5Mm0EZ%2FAOBU4iH6Rwfj2ergNbj9dIV7nL4g0D1MBG0v6bkvItCTDdp%2FhohMMJRgnQK7SXi07OD2%2FJ2aF1vCBX0UUuD7pDPrDVd1yJGl0Ui%2BggCI3qsRd8P21DQXm7%2Fqbb%2FH%2F%2FgJJaLq%2BVdre0q5ydPrak6etkkU0TefGPyLsa14ffvxlGVpjJfEypHZkBeXmsLxHe%2FdQUfdE9caqUmaa4mM3KOMB7qeDdoVNeUIxAEqcEe88dLz2ymcydYZBeZWWzugVWbzPhiQ0%2BTYphvoloYv53a1pRAKhMTlQJgpaErgLuqqGVLVMveJ9ueAIuKUgjaFv9icY5lo8eS4Udb0%2BZiI%2BQjYVWRCytxEHbJ8%2FZRoxz3GE6bAtA3U47DkaQkdISn9Uvi91vz3cVyOXS3zEqddf%2FK5hJUl1WYBFKK2FV1iOrfrSpnGmpp5%2FRhW8nxSX7v7xwkh9uXqVI83QRbZHfpgvIyyB6KRWyv9DZOgN6CxZPj%2FKDo9jZlc7imx7joVewc%2BrpKZb6m0jgyTRnz5IUSzXg9gIQNGa3jg5mEEsSwfMJzR%2BdIGOqUB8yuNJl0wcbZe3NOYobbxox%2FW98Aswrfq4OXe%2Bpxu9P04xigHQIQyKW9fk%2B4qPuja4GZHUXnhL8dmw5EIKskqOXBaccBgqYCzCT7T4DB6OrCl0thoqmI5hnNyYrO5PtPCfc7C0ZNUzy2TAVBeY5JykvdZqFeBsuSKBS0Q6aSV4BvkqI6aL1kXmcKn6uemj3G7KuP2d3j76QF%2B1vhLFRmCoEFSfjtZ&X-Amz-Signature=0161ce52c182062b7d1d93ce353eaa566a430e7bbdc8b6e2db070431ebf07ca8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
