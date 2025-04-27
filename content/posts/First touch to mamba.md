---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UH5LLBCM%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065840Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsqOhASTjCnFYpmdqeFNwC8G8kgloBBgY%2FrG4eRcy7swIhAJYvLPe4lpDJS0GMmZ3eak%2BTAHsYiTzK9ZeHLzRk4Dm7Kv8DCFYQABoMNjM3NDIzMTgzODA1Igwbi8%2Bu6ecSzjlEvsYq3AMUQBSfR0K7rSJJ7bctCdL%2BhBzwRLBpRSUUTvvPT0jsDFsYV4TpaTqABfvzABgWbvyDEZyeJ2PvtU6hqoNB1GuURpMPq57NcpFv23%2B2V6fPGeCuQm2DmJHP5gubnYYtaukV441wGDRW%2FsE18WSWHOPaziD%2BZVjbjnS%2BViFfI67gSJxMuQxSFr7W%2FEmbYIDalA0hTqSfO5RTMTAdbMyulN26aeslpDjoyxGGnGZIuA%2FQ8NDfqh3V0gzVdoF2YuJJp%2B5CuKgKgiDHrhKGdfG1L2IH%2Be%2FJLJaX10NXLhoMFboBbc0DjyWfg0MmceO1cveiV8VzkUxtn6%2FfyUvGHUvdjbiD1LLjcJNSyOybU2mOzXaWIfql8IY%2FFv9oipKP%2BmllMxIk5s9q7aljQO5nfZ644%2B8TZ1R2TjqK%2FTEEu8SE5VOY7UVP1rFs5PFyDKzpYIEdDeHkhq6LPdyI%2F8xwKihfVUoZLMh%2F3a9LQNEs89GW5JggypDMF%2FuOlgK7mRsDNkEKL2dCKtAnhIOZFlLe1YLZWAMPgHa1tNqx9XbHjN29BGCEtbvrjqSM8Us06WYMOoUbj5ALKhipwgo0t9EW4nVKReSq4qpvfVoy%2FlC3eSi7hBI809sMd5Z8jwvRgc6rdzD47LbABjqkAawUkXqE9tshRtD5Ui85v2%2FXMz8rUAf%2BTMLUDoeWwRgOi%2FqJVd4gzw%2BJdMWBORdAzuDMtS5qTLSeqNf2qE2uouJuZ4NbN4v4qsJbx4w91f%2BTO2tZTINzAjdOhbaEj2wjss1uzxLaoGOnzCdL59Ye3ALy5YIkPMlwoZ9NRJl8nw72yFnBAKN2%2B8wNuM5FyZ08UCgffkme5W2k%2Bwy%2FHQ4wAA0itigy&X-Amz-Signature=c0e7141ec39f8dc800d8e6fae8c29b905802164626176876b3fafbcfb94c4476&X-Amz-SignedHeaders=host&x-id=GetObject)

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
