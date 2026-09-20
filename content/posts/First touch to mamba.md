---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664K53V3ZV%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T195522Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDghiifK72zITdm2NrwLeV9qt7S084ZF3bff5u9LIFIawIgQm0S4krAXuZyOhkvLiEq3EI9ZdJ5eMvQFN1jPxWXmfsq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDDbXgB1jxAVQQNJ%2FzSrcA2ykaRBv3CGzSkXQMTmi8WKQ%2BUJDCPUooqPojQA%2BvuaUKG9DVcx61dKSMZ4raWJwsuQBT16N4hj%2F8HhDuWP27nC2M%2FV6p1sK7uGxqlpyD9lQ%2FioFPThV%2Fs%2B7K%2BttYhBcHeQc4U4f8s2Bv6pq%2BIWENKjbf6YzrCoorodcOHpbCwp1PKpRgD8t2Gkm5iONtlXji2c0cD1mM9RxyY4m2M3LWJxpb1q0JXXqycpkNh6xftLVI1paOg10ObbmRONao9YDU44fMeubi878CT30ydatrI4oyJ9bLi9zJBNH68Ni1KNqbHi4g%2FHZFAOdX856q8U%2Bu5TtThcLsN%2BnPPhZ9rko9KDEPQjhEMVlrHXCl%2Fqov17OVJWou0ULDh2OTVtQh3kY23nlbo7O8le7oSFD5b5BGboZd8ki0rwTFL%2FkF6AgO30x9yshkIgWJKohcuNlxZxUcjYiv4F2GtxDDLTdwd7Hxo4McnaEqp5R5crn3kVsHXt3SM3AAa6US0HIlhZ03WVwyUNOZcMeYtqakOgqOC4Peykwg0cP06jrLsWmgNnPPw1qjTFEp4soI9KV4w2gsN0Ko4DnshuDCeoiC1xgJk%2Fl0Dmx6AR%2FERnprbKHrP8YnimDshuMXnV7AodyfBeIMP7mwNUGOqUBkUSGPune6gt5wQ7yzqVJ0hGbtiPHakWuRhVymNcdzHI2oDqF7c%2BjY3jxHZt3XfLZBPNkW%2FpJBpfh1H1vr1gerV3qUn1c07sGYKL6mEXEAEku353srs8vpgOYpsd9HR5mrhnTao46fNtZP8FW%2Ferj9jBUEHWwXwLRyFIJe%2F8KQvAkv8XoWLvlK1mFGsQ%2B%2BIwA0mtMG7PNLd1Pi3GjwOarrcSppU7t&X-Amz-Signature=177427dfaa9cebd36a1da4b2e65f36692337b45714ae68dab5be7b9ca920c690&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
