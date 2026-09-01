---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QYJSYDSN%2F20260901%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260901T125144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDO5NqKwKvgfc4%2F5heuYg0A7HSGaBh%2FDVyFiWUnhHyLjgIhAO1eRiDX2GLzYDWhwZI3AiyjtGzJCzjXQOiPqDH9QeYQKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw28sbFzIdxuSifkncq3AP3lueY33CQ6lhXbB9dmUUyIWOaUJ3sfJ6kV6jiAndxLGWJwzM%2BrnzWb1iM0WrZIHY%2FJewsNQmqPSKQHTEdnbQWdV7JfSnSS%2FOC8XRqMWMueAWJ68nlrXGV%2FbAMNx20giNUvEHoa1MJIBbyfdkKk%2F9tjOdk%2Fl%2BeNj7xduZxJDAIwxn3QrNJgramDnzCbHUG%2FlP%2F74RD1LyGmImbBBzQJDzgBlB4hPVDOJEz4WLuetY9A5aH2MEnvg%2BJGDSZdryE8I9m4rkkdhUX9zeoC0PmmM9xruco5xriPJ4BWvQSghvuTy12ZHaRZ9vUItDVLsFom7oYbkURbY%2FlWXAaYTfzBWKD%2FSF22FHJsY0iqSLYCbj3qAkaRrnZXJdqWkNVyTZxlZD9wYC25gd%2B3mW5bVLE0%2FG65zynLio8Yx1VQMK6uBLoQ4AgkUfNWZMni1YTr7O%2B%2BrE2WZraPqVURRmboz2trCXbzyuzGSPyvPv6gLm42SzYSi7pz7Pv27jLXz0%2BVv0MXcTWuCzC3tTk7q21bK5XbkE6JC2OmyNjOcinPB0%2B0b7BIZzVC9sXLEbCgUP6TpRAShewnH%2FZWnxEL7jtomMQdq15%2BBwQyv8IuiRxxLEWkPzZTje2cvoAbk5mXkIKajDi6NrUBjqkAZ%2FrTXMRc3AzZRyWYOPSuN2nDnMM1IhkPMXeWjhrGJO4syzq9RF4KaAM%2FNl3YMakLPiSEEy6oreq0ekTfopck8ThTHFQvKovNL7p87MQ72eWiirZKtHguIEMfXmYzaxDYbi%2FA2qyvkvccl%2BGLKS%2FqcvIwsH48uWjdeUeKynzwqxQaqTEbYA54uHm93FFt75FKL3r1%2BHAojrRQG6wc%2Fn%2BdbTqPDnU&X-Amz-Signature=48558401bb10be1dc13edcb8a8440b88ee85fa11cdba408ac8dc3462be3f097c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
