---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUPSAFZW%2F20260704%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260704T053526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQD93vtK81DjUlfnsAmA0u0XDSiJkf8DD84N3CpOvxrZmQIhAIlMewILNpHgUOschMGA2QFqSPeurvfQFqrZfD9IUUeRKv8DCB4QABoMNjM3NDIzMTgzODA1IgzzhJFZ%2FGiph6ikNJcq3ANbeAqtEcpqnPuIPVPlWP1R0s8trlFSvhHX%2BSNAJXJs8ZwoWHw5qRaE8RvZgo6cN82Z0ZsXb%2BdSagr061jNb7mC%2F069ZMGyZhBoeij2sHxbICsLuN0p%2Ba6E2sA%2BA4kKWSoYJ1o1buEGFC9DWLqdKwtIeMudg2WHL8naxWlPpSbiKEUTvx2KblacyAr9BjXcAmWbMoLwy5QE6vCLjYv8YWEsQPv6IYrJ3ldA%2FhO4jD9qi527sBHAndaBX5kRwLZNPcRS4ukDn8lVgdb2n9sv20VtgOBjQJnWeLWYssZpHBGJC9nKyhTNuY5TNbj647AqimQLuvQgEcN08FHOMSTOkNKWe8Yt6rIdbU4dy92Im58uAwVtgvGgX1q4fBQ%2FyKdXjGyINyVuVNRPTKTb95OFhxevYQqK9TST9%2FRbrfiXBjtSYrVzZ%2BHVrpefVZN2NAPRQ4lF9XhupwFnOqbmnKK34DQfODC%2BNdItCcHGm2%2Be%2BNILb7VvOiK9Yer8mE9%2BDjWLXqzOxN1Xi3qAxlZ%2BCrnMYg8X%2Bb31I7PCUwmRe1ti%2B8zaJf2nDs1yJF4XcERSPDxxVIy9uqoEnVJRrePHddEwMUUGefpXXoJCstCOJ6jGWdZydVU5Swm1Snme8rupdzCFm6LSBjqkAQyDrJrEV5sqEWFA%2FpCUkFB8YoMnzLlxxG5Wn8gCin6z4ef6SIygeANVJIb4knpTmR8lhFdP%2BlYvhmPiT1IMZBn%2BgUbckU8rvRwstY%2BpT8uXHaO7Xd0fFUmU13FYYL%2F4b%2BQxr7kujdQdwOzrianrUDxkf0Pytw2JH%2FZxqRok7efBCFm4EpkHN%2B47uIqmECexEBnsym5WHUVLhgmNyMFHnBnis%2BJU&X-Amz-Signature=1df74747dee94181de7168713e09e41749a30ac1cce37835df608c53ce1ef365&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
