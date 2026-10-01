---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BH262C5%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T145430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCYvMpn0iB9uCpDaDJHUiOI6sSdJ8XyZ7hdr%2B8HlHrjzgIhALOer01eDEkQ9yKEOtW4yxgATjy%2FqNj6ud%2BRpAxIQSxOKv8DCHsQABoMNjM3NDIzMTgzODA1IgxIzmsdhMGqhaKjzi8q3AN8948Mz0WgZqMGZbVqC2u%2FIr%2BRrGy0FzxSL5olTbz15xC9W%2ByIgIDsZMxhmp4dfisLnbPXIsXSeQAAFuPJVB%2Bc5bEVPzFLJ%2B0N30zormk9FiiMchYTwDgwujTHXe%2Fh%2BUcRzGp3ark8w8pgqUZjusjnvrkvxlJg3KsVVZCBkL6LcWdXRrrs5aHsWWtptGWdiyKjHyFD0bY9FpCHKXPVdFzYybAEOVVAF%2FIQlQrF9knLiVazBs%2FAAj4Y9GmzYFgmpbTM5Dq4ECBgamuuq3MZSydbvKqtbc1SX10OyU8SAaETKA3LEYBLIedp4Wrx7SjcoczADwQcJMgmsykRSqn%2Bv4%2Bc%2Bn3sUo9mRB0iqzv5NNmYv6N6Xxx5G7cYNZOUnRev3wEFWmwugNTfXJPj4ExX5hZV3ZPkDgnKhrQb%2FBn9GxVyjjXkk84NI7FpWH2bYiYvIEDO8Sjn3buG%2BQuNKpOfzd6K6yMr6JmRPAUvKTvLW%2BfOHaKz%2BjRTvPvthBS9Fac146V%2BvMeWmR19Il%2BY0tgBrk5pU72CF0cJ9VOrEGzyA5DrbzQnaVzL2R%2B%2FO8btv7HoyRIaA3jxoDG3mkW%2Bpd9oMNPtZVChGTK70aXwc%2FPxvqFSQNOFu%2BXjZUzbmpQgzzDh6fjVBjqkAUQIg%2F2fGwagnYuQwPkDgR5udBJDEQHY5BZ%2FOFztybTdOYQvQE3rQn08H15EuFv4BFYuWAnbfOHm7ureangdtvCDcmgz%2FiC9JnUVMPG2tWK4MYQTjb%2BU%2FonDmAOjh%2BXG7m0eSzAFEs%2F0uf4ACGZc0Orzy%2BHw%2B7%2FiV0rTnEbDO%2Frg33AONcia3I5WOYUqdHFyVHgnTH3xg6qO5lhENpt3Xxazp7NR&X-Amz-Signature=55b58e46bda77fec48e34d545f8efc3171a317762c27224f7318c5211754f1f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
