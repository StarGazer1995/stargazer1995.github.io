---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UZS47TOZ%2F20261002%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261002T011038Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIElhD4n%2BmpfeAji124b67eXGmk7dDS624gz4NqskHmfhAiB8zYHhNCmT6mHpv1jkLBWcTqdq5FOYvT0j5S4k8O3fuiqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjBxfcDy66K236NBZKtwDm1SgCtBHgYvXN4QH0k%2FutXWsGSlSB2yKNsRicUmROixlzOS%2BVRDZV2A%2B9zcCVyY3jw14qDEb2WHkoADgQmze5nGc4xLVrG%2FigLkTXgqbcUZXeb3i5zfLqYtfRZKj6XTl4x0at2kyxsYRatlTZ8BdCNunPrWLBTzEOuAZ%2F7nQeoH%2ByxHd3Q9gEUa8YjsyvJO9fnHN3iG61WEp5AJhNcpV7Cuq%2FzdBDvluqbgkRufphVbhQ51%2FmOxEEcVFhuD9c8Rrus8q6hqnDEQl%2FmfhAFQ58LwLGCw%2FQWDLgCM4JYU4ux1ktneQVJwl4v4EP5a%2Bf30xEP9NvgT9oLhIExIRxldmjNj59jV3d2gNEwEcN0d8exm2nzy3dejUynEr9lONZMhqmebBJfi54hpyGi6KPf4J19qrzklFVc5597rh%2Fxixl90Ttly5BI5LMqPgT1KEQtjk73s8h0HtUzIfZnqptUPLxwJnM4eX6fvOnsBG05C60kE%2Bj6ZQKkiBxBjsaSNKOYbNvTtfe%2BxGa0YHLN35iovnQAhDbeL5Be78ygpZXHmi6Ij9Zx04qKEp1lUKLRnc7c6wNXQklVABYsVdAxAg5w3v4z6UvSDR5CYiNdNn6K%2BZSijEY%2BPY7Lk5PUBh9Y8wyej71QY6pgFV3BSnLqV95DPoyNMUkB2OsmAUtDx%2FZ7OTzfJ8w6ycIHhZgZkgOozHA%2FN1B6Kqp2U6yDfKgR79F9BNrM9D1vSmKP4YN6y5eMu16Z57SId0zwycfmgw0XcaPnt2Ve9ZCt1irTy6g5%2FCNIM0uUTH5IsrEQfW4D1KbgGMmgCTUk4jFHEKVYdW%2F5pfruRBZwrAgPcaMFWrDYAC8Z0Nds%2FqlfXpar3OnXuF&X-Amz-Signature=359cdfdebff447240fce5d1e29106db8111e3b133ca274fd20239442457ad22b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
