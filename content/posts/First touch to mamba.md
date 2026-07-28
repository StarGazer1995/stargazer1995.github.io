---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXOT2OAE%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T155905Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDwidR7U6vSQUHQa4oUE64J%2F6iakTlbt5BaPcSzUuaVHQIgCtfZcSPDfpUh%2FFzpnQIp%2BzfpM7PATv6vfIy9dbm4mZIq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDJ%2FnYvOxh24v1hLvgyrcAwRPwvgUUei%2FnvmazbQVart1t7SzbQ0ZmLoArUGl1A3aVYLgJAaDnHq6KcYOW9di77ErfXYs5F6N0KPZrM7Old6j14WiIgHUQgVCWd7GpSuCPrNQiR9b5noZ%2BHJUpZRWNN1oPAnj6UnK%2FhMEnHHDYV97ISnHi246HCJVVpaMZDyw%2Fgpgm1iCeYTtG99SPtWCzjSW%2BnYY87gqzYlJQuamdzXzLb0N%2FPHhWbtSinRCec7vZNYKoV5oM8yOnAMpTnIyZ6OXLVd%2B3nxhIHzgoXYgty3ZdfgaworBOVugmJrSIFSB6M9xqF3G3GFe2nr%2BNi7jJxPqhNmlH2ZkAgqK2PbjSzL8JCtaTnhTxlsO7Lr3w0rln6Q%2FwnZkR4peymnDIkBiLHkF%2FGVwWPAzlYrE9jWCmabt0FoevLW78usm1cy4gC01%2FauUK1ulwL7Ldlfwiq9sbFW%2FWGoppftTINAedNnOsMYfYv1m13YHmYRkMBnC8qOcb2l%2BmzLW6qsIZX%2BrIDf6QaJ5oGCrgduH88Ij25N8R7Gg2rIHtbFTUb8Lq9NUfFBCO4SMCIklejCaa0mctP4yHjT8OnsD6skTiJKxn1ohxhVeOnBy9NWn%2BbOabOZYg6eg4Hxx%2FhIHvYI0pLsBMN2Qo9MGOqUBqRFj8Qq2R3r2BzI453mzjExgA9Y27i03gzgLWYwsYMJjwM65tJdYJdrgWUsz81BtvKvpoK8v3vNSK95Ucn8vjohbKq1MJtGXzqUw8Z5LBzDjiCGe7QdRywu2DuIpU6gzC4PPCh6zKZCvvOqNd686ExOpxwInVpbhPTG2ER0MxYeNJ5JseazqYsbSCgs0JIl0Nuf9WjzsXITQsAGiQyPHdx4ANXi7&X-Amz-Signature=7466d60d1a03ae0f27495b398c361f3284ac9774f28839a8261e1501ce3e2fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
