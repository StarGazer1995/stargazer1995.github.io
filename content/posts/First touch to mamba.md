---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T2NMHFLE%2F20260510%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260510T125039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDjUkxxEloNEIyYoP9CPDHBPYRauzdabr14Btydw7yJzAIhANCnevFtUrmyL%2FJzp8Y%2F28yxhMxJgFh%2FV9LUlusKGDvdKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzODUNv4hiC33CmvEAq3ANFqOk8hfZFlcVlM3KQBt3YsXCOn2c9JwRu3lJFFs2ZJ0c3rwdBTzcTnRi3PMnTiZc8nHzrtGHM%2FQG1pF57RjASLbi3iUVAa4dO3zD0e4h8gXvkTucyHPDbNc95Zer4VwZy3gUiFxcqrhBeBqwVAaVrpUTatk7EVvMX%2FT6gKlxHyXZzAC4rGTGDYtq4Z4v%2BfAGDn4ir0mCWncjPyC7ih5E8z4AwkH3oc1U%2BKGtkM9Jl9guyWu8umAxYCrKmgmWMo2I5Xqinx2Fr7DD3JEAeO1pky46chJL9a7BrSmWUnXhmcryjboSzSSyrt6JdD5P7xFhZV6vdOpaKC1a82wnA99Gy%2FFvIGZ8Nwc0StoKWKKiaepptJabkchDEDw%2F2W1c9Iq%2BeJ6lXhgUB%2FPKCTls6N%2B0qt%2F7by8bXxCiS76K%2B0c6I2L9h375nHVIUKKYrOo7zIZg1ujJj%2BXuZDuu3G1xSkgH%2B83EPaktl7bCbxi6nSnD9YqrYVocdg1IVYeQS0%2FwT5KsrHTrZ9vnsR7ShaQ3bdJAFda6oTikzpbXqCXRZB13iBIhJ%2BdT8iL7ItNnmpuAaQLUbracv9dWEY8%2F9PKbnx9JcMCG7o4xQhaRZLgP%2FfvlwC0QNSRHxYvxQ9k210jDusoHQBjqkAVpv0NnvwYRKGZjkjIBg3l91k7CW8%2BZjS4Kj4JY2pKzR1ZbA5zVOzOD3LiZRkysFuFEYlAiyPTVV%2BmCT%2FqvkAK9KrNY2rkANlTW8LJrDCjgHqKy8Rjd9CuKtvoSxXsSibP7w9aq%2F9HgahJP7tsVgHUnOHxFAXlqxRt9lV9yqWiEAfXDjZwbpBwSeteSn5Ro1%2BkoM2x74nTSf7sb0e1wALIGuVTn8&X-Amz-Signature=9c6dee8b30e04ddb176e1b7635a60f09185f941ef729a155b587c70f7107ecce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
