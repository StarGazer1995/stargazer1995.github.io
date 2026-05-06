---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHTAOYZL%2F20260506%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260506T172639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE53tW9xy6PW3npGVLlbS5SnANbEHzaD8CymoNlFQ0uGAiBwz2oM2FA3Xt5HxXjX%2BLj1DbRHDkBfvKqczpAgLK9xwSqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6wFiF5m%2BUZSsDeK5KtwDg3EUVI7bWZ%2BMmf%2FFpvW%2F%2Bqk%2FsmfnmbgdG2jhOz1ctsX6SjGbRmWwzlwIuzb8CQm6RvhIdAJdOfUHk%2FaDcwWxUOWtzRzzgjtHpPJvPyEoqjV18UAqHe59Z2BPCT2pUxi7oDtShIWCyoahJ0hvPUyYk60%2FZlfwL8NoiwTFiTHOJUH6K4jO%2FpnsZcI47vUiftCEAvCSfUI5P85LCCbBNWZr%2BPVcbBvvC%2BBdlvwTmzxDvswb%2Byh%2BEOaOmlmfwkLlsjAVHGqETDBwtn4aktxdX6p%2Bcyg8QAF1PboI5efZE4unw%2Fvg6K8GSkKWK6430OotJSK%2F7iuKoBJ%2BfnUy5%2FhKYqMjOQcA5e0hhllST6X0gqw13xwj7jF9Qm0FPlGAi6%2BeAbpZkLAieSBeDsbhhNVD56B68kcC0z%2FAn61s9bXCtG%2FJ9hTBlQFnCc9aw3ymwXFHeXss2%2FseZS3RBx7EYbc%2FU9uMm9Oe6QwG%2Beo4cj6%2BDRw%2Bgrc3oEyAWljsZtWYSMJ%2FoaghvFi65FqyUGYfK9plOveFGVVlWJy7wvrlDezjX2l3BQCCV4cVwxaRNM9KPXBYUidXDeM2mmwuViuYMRLehKp9uDdUt%2FOQ2%2Bz00cUjEWJDaLI9imiUtQFhBfG5%2BDIww9jtzwY6pgHwBdPD%2FGLVbAKrgUUKsKcS%2FGScWQTLHkXLcW2rXKOzIxEZSl5XEWQmXf39f1KH9a6Fo5bOwK9USiKXX2ngLC%2BeoO7IGBKZVKLiT3e95a6cYXmoIeM74qdu38sT%2FIH84LvhAsuvGbQrvWkvGJet%2BdC13o8hOj7GacCTirxXCgV9zORA7j3I8B0U%2B2y9KD6JBKoK%2FW2nZTt4abgkqoFrLfySofG%2F4YdL&X-Amz-Signature=e8eaba5c53fd023070086705411b7bd474de16fc7e0f97f2590deb0c0ad49240&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
