---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J7QUX3E%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T122139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJOQsJuzJV%2BLErRvOh87qdOkqHQbHYtUj3RJXihg8GPQIhAKQ%2ByMcbdZMtLrMudJyYgme3JAtHrt5L6jMmMYhY3iBvKv8DCFEQABoMNjM3NDIzMTgzODA1IgzdcNnEf1kQllq0JOMq3AMeW%2FJ4AFLJ5nGu5%2BTyDxnQG%2FN%2FtCWsvtBpQXATFJ7YVRxzYtyBi%2FTQABDOxMe%2F0vmjEwp8ruANWNgXYQbq%2B3zXrFcJ6hJTzxzhMBB3pZnys%2BemKvNuMac1vAir%2FCcqKFMcZF%2FV%2FB4RN8vrBNLaarF8XQzTgmAQsWWOC4%2BiiRJPg30lYWN20tQ8CqYA2RnT7q%2Bgl1%2BWlbNmDCuZBKcBS6bWSNtxA%2F12lqZtTOVUjumarVfxWg2WK8k3zODXm5qUY438uzL9cEzEL2LiQxpUzhCB0qqjublEfD5ytJPRj7Fz5w74NMVrwHZ7gPGuV1WXmo9PQ7wfLd%2BdezSy2mW12bm0hb2hg8KHKSvAio2%2F1Xcn7kHAjpEkMUfyEIZo0iGWHsIXI%2BYzq%2BAyQEuEISejRL7GATieZRzgEGakGopslDy9uwqvg9QBj0mT9mUlknE7BSAu5D4khvBW0KNjylVreQK06MgNF%2FsIQOuriG32IE4DFEKtZK6YTuu8nG2l7cSRA4quxYWdstrZaCWk%2FfFaUl8EZLcrUj2OR6H%2BGlsXBnATL51LY0K1bpWJWfD55pg3%2FqQctAZThgNc8laHAogv8qBld8QGkMp%2BQpo%2BYd1W%2BAgHtz%2BCM8FcufIYkKjgSDD4if%2FUBjqkAfHOStyyOPvcl1%2F8KnXnlCUVknpKZtLxNXOTTxsY8rANKUoQWG361H4fGwS%2FTiTybk2tw5P4l5bECYrtDa7kwRMLZAH8%2F3JGDtEYAe4Jhw2EGPpYQD7NFY91FdBlfqwz7aTTZdcrbo9LMDy5PKudK7ayODe50eHhePNGGr6DqEBIkC1BqorzdV8q23Rj8pONC8HRltUILpD%2B6P4pPg%2BwPFR7YsW7&X-Amz-Signature=60f5472c0c8297e91325bd74dfa08b257e887133c8e5f0514f349522af452907&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
