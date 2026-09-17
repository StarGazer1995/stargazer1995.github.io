---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VEBEDWZA%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T223134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG0aCXVzLXdlc3QtMiJHMEUCIQCWV76be9TelflBzJO2j8tkJS39IaTt%2FqDSll05iWkV5QIgVRvRsoqCdb4KAq1DEB7vR%2F4hX3Q4XJkiESznA3iex8Yq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDHeCoMVkfh8cKvKEhCrcA%2FkbrlBSxCu9yyANhRPd0UOy%2BfbOVYpWWOVrDGx0lqp3W%2BVKeRj1jyCV1lc9MRjgJY7UzxIpJBAge5OcQt5TniLOvsxMiC5SBsbowhiPLHl0EqXoc6tXO2s86M7B5FICI%2FAHGynj%2BMXPYin9ErYPzi24ZvktStSP8G1j5R%2BtJrVmO5jBQ2YY04ODr8A7iDGYOpA8tXab0BUoHjObYQLJPpdUwsywwgUsTRic3Cp219EnYDKOuAJCZ%2ByXlhx7%2F2JCWqMIqH3lhrvSAkUtCARDIzLnOzQv62RzFuIR9I2XDYUcag%2BmxXNFg7L9cXAMHPT0JYwSpuiLTwh1DMSGtCm8X9SrqaNYWBFMglzpKcXu6KbzhfxXx3ieyE4CNdyFsO2xUQdq6cQSYYzj8NBawugIPioG68nIGQHOFanIAAeMnkQU%2Bgh30WkXn0ARIigDMaZ%2BWEDbJQK20V4cvHcrIZOia9J4X7TAvDqFx0GoNWLDBJIjcbVH5xNbC61MIApaWEb8mbZKxj5npG%2FY2Pz61Mnpx4t%2B1MZ9R9KICTaHwBUFkpb%2BjXoxFLTFsQ8p7ew%2BrPlQFqGDprlTqOjFy5eNHb7AsuUro%2FpNDIHG7AzT%2FWRfmmPAQghlCoIYGCXzjoRZMPmssdUGOqUBThrBsuYFl3kYy0QtgW0lM8ew4hzKOGpu%2BV4OQlBqPivuxYdO%2FAMugNydUfurtXzgNbbnupokLXVLm0QorwkKIy7UNPQxnahyyRby5gZFkbX8Q%2FgmqXknAL0NZa%2BQUuiv7%2F4bqMDCBEexlS9QzmtPW1T5mU91PSb1S23kMTQykOdJOp8hnF9U5acSGqNxmac1TJCLnQdPcC1YiV6lCnDVujQBqKr8&X-Amz-Signature=85274e2404e60dc2d5186671282452d55039caa63917fd7453efcee589c02a83&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
