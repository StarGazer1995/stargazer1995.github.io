---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XLFUBHT4%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T193927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCICwYpt0jGONXszNUx5nszl%2BDb6XDjMtd8ng1c4dVSl%2BlAiBl%2FTMKoDkWJd4Wnj13urHYTmYXyxFUmztQXp3u0Tf%2FFCqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe3UcAex5CVdW583%2BKtwDIh4GT76Tu9vLhF9Dw9CKdlDGToXezKTu2VCm0AOmB%2FCvlNYdP97OegnIa0NOjoUqFzfh4LoAbTA6ncpyLRCqQdKCSR8ZnzhhXbIEOjFPymo5LuAdX%2F7KaVlrocc2dWzeOeInHfBSuJsBY70jeX0lBEtixY%2FCu3CJCySiCSQQwT9LXeCB3QZzjRKqAqw3bHWretkLpepy%2FORxdrjeWCJpkOwbcomZG8iQ5AIAXWsRLWaxvX%2BvvVE%2FKUipcVi7ejjzbYh7B3e%2BYcw92jgw8zOXkpQKcuor%2FxJU2KQVbGJHczkuA2TWIRQRRcbdIhwXQZk3SncHi46dj2ZYpNpDKPYG%2B0kzDtuMAO0MMvf66qLQpuNP%2BSmWmk9KzmqVp5V9ZgQhCjJ%2BYG8oWbicyP0yOM%2FcCqBIh5FCpLooptoTP7ucOsrDugiGUNcJob7LkvQO0YqtucgGCzrY6U%2FR8kSNqTvaz4ZyTVutwCtoJ88yD%2Fm0J%2BsRuzXg3HQL1BSnoqMINT%2FzRGXNccI3KQDTcHqsrtzGiTZP%2BC2RgJj1nVod00In%2BqXks%2F1%2FJRyJEdO22h51ydqVT9PnXe9aWXQKyv5GQi47c8Q1NaQJ%2F8Sn9QfkO87dFSltZu41pGPszg74f0Aw%2B4Xb1QY6pgGIXP4Enrla%2FrgCLdgnCAPlsslDrDgG51YA03HXSoCeIse%2FRVmadM4Pk4yNQXNHNcGxz8nUCHymro81sg29qvLp88zTiRh4gA6OmM4yFn1w2BlxpPW3dhCQxkQkC79Wj5YHzmjH9vvm2bGoxMdlnMgMyMfOTjq%2FjFM%2BNpekSwQnquIsJvi91MPxV6El0mfg4VUNW62nzsk5QMq5hw8nhBOOZ9SYHN9j&X-Amz-Signature=1131a59cdce7ef7a77810ea18f1894fc9dbbbf6592e6f30c706f1c40dec26e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
