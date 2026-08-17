---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU3WLYIZ%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T182105Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAcCT7Kw0wCQFp3uIRf4n%2B61VdjajJNXTKax9hA5FLKbAiEAhHBHnFnP8Nu34QMNqMU4Ubbr4JobpbQnalHJWoI0Btgq%2FwMISxAAGgw2Mzc0MjMxODM4MDUiDJMw%2FB0WYW2YxQu%2BXircAxALrpyGhJO%2BsiaeYhhMT%2BCh2lhqh8ZclBqQIErWwWW7aaA7TSAk%2FUTRw9sQAyCtCMm7YZR1JqY7z%2FDMnlX5z3gJOkg%2BZLx7%2Fy8P26i37Pd%2BdI5gZYyUZo%2BmqZjsUlnjVe5wawQqAQKI0kWbxf1LLsWEdbLmBrxyTjtsBBwQky7Tf7c1CA09COvUcE3%2BUaq%2BPDlzctpBkUXx0iumMDyrc%2BgOdHHNDdfJp77S9vQU7M475VRKqMkUE%2BXGYQPtAjtUnws7BrP9xuq3wOxADa6x0q1byqe93emotmf9N6hlyymsrBkCV5cT7%2FsUCcSLqt5F9AEGzcV6cPyVM0chn7wiir9XFAG25747zv9kxu9HzsYTWrTI%2BWItx7netxRy6eREFLo3N5kSvLRjkELCPd15uG5OgsQw4ixW56oEoX1B93q4iG5vF%2FvHF9vdCB3WrjWsAPZNBx7dsV9bqlt%2Fhua3whrgYcN9niXEglBhLxC6bqSfEfQogCKpkrSlZBleb52tHQXND39BTFnF0RqxwMRo23EPQ2eoyd9pRi1U%2FS8c3bqgZJzx3bf7VoZ%2BCWKwlOYXKNehFu7oJs2LHngS7Z6JOOFqCUKuyAb%2BgVEEhY%2FpGWvfKiZTbJZXmCKmXW6TMJuXjdQGOqUBglnkqrL84S8WhPcYRRBjlaxJv5fjzRG5IFw7x5dAhUaw1A7VDxmNKlZ50TBSzIHog037yzmwRmmtmYZzbiNke2VdrncDXiM19e4JZIHqq3uby7HgNus4Q0G6GqYFkgqXMrz0u0pyCkkerdZIO9Lsj7w%2ByZL75qyNctCu8wK6GT%2BvOxgNAlHuzv6SZYymSTJ1ZUywVflglDHx%2F8HmXdODcHtvT6RO&X-Amz-Signature=8a570a661240380c46132bd937895cfbffb93d4bbb73b735baa08012b645a34b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
