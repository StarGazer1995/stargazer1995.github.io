---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNXFEQZF%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T143311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIE8cpPaDpeF32jh5f3YtcbV0HfMEZ3%2Fowx0rKesf9d1BAiEA8%2FKOuwQa2lHLaDHFyo31QWk589CT7p6Biby0ugZgvSIq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDOaFKaafkok5tpmi5yrcAzp%2F6T601ZkH5HS%2Bo839RRB6SFKqjxIkXbDjhSmZx05SkXKvrW21z2U5UksAn5nJ0757o0Lo%2BFG20W%2Fnl%2BLH4qmy2b%2BfGxKGC%2F7Xmp7LfYE%2BMMThyjeo9TGOkxeSFPjfp2QJLvDAYUnL6EO%2B4%2FJcN3iJlPuAj%2BbgAVHZFN8bmt6Sd%2FlKw6hbrFMfqs3CRJrPjMqSRTGuae5gHi5qmJYynF5j8uTUFT0Ol%2Bs%2BW74FbYyOg9PoN5U%2Bgit%2B4oAX68sHBDlk3LxhNgPaKYy6NVBufpXhWo7POSmA1rs0CWmyy3I3%2BeFJJ%2BGAOgViN3%2BKo1iIV3rrwGtFBo3q7%2FLR4jX9d80FjZ6uAHxUitmqN%2FRfbMPYmzPZExRN3ZXO7UmQHgTcQzjOF%2BauP4kG3%2BsNc6cL3GNjm%2FChmsPhNJN%2BgoPbvWseWMv52NhIY1lCE5N3yyOzSMpiovx82thi7CGt4HaGN5p60XhBGDJSgmNUjZaWzXiEVhMHC91kzJgN3wAw%2Bmt9T7nrolo%2BYYCOgU%2FQXzrVRLDxm1pY96V3ruUVMAWU5rlcZD6%2Fp9c4JmXeE8OLnWg0hYjjRV4XRzgb8YFuwvUW%2FtRPo8VcB47J0dST2%2B%2FZYU104%2FoYKMjl3%2FPG8qWlMOmJqtUGOqUB1eChUDFTvDsRxRPHE%2FMAiUPp7SN7OOFyslMspE6%2Bl3qh3z0brIB0LLqo3ubD4eL85UCY89I%2FAJQqOStep1RkdTkaRSdLWcvRCc9KL7N1hWqPg5zcRjegsAdfyhjPL7J%2FcimSHrBd9ttzzPMRbXvElIQFzTAZGvW0OelsfJ0xjye8OfR3dIzCcbgv1wTON6xAmbupUguKXVIB7W%2B4MuZzTEcxwfFa&X-Amz-Signature=f3677c69e2972b0ae416d8552eb50e9ada2c0b390add23ca3f823520ebfff79a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
