---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YHDCCUHO%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T013007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBhTahLd6H0m6GXCoJ0eGw46BdLjt9%2FWsQlPkwb38T1jAiEA1zgnWUgeiQ4yacgty2u%2BAlWTGR300L9ctqNOWR5WsE8qiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1HN4TziNYGpatXnCrcA8e2tYTi3AEh7VqyKqighflsd9j7v66jGQzsgw78tfaWWZ%2B2c685Rr4%2FHSiF9YhojmQrGqF0lzaPW0E8RYJaR7f55W48JgpQ8KT6JB0HY9jUC%2FqlCQlf4P5rC9cvjPyUt4xQrRuhdkWa50zkL%2FfuWrvEKtDoUvmQqEWT9DHmasUw8FyJytH6MfziIGldcGWsYmPOcnEZLCfKn4ImZdxSZkaSMODENoQ7cjW3i8GjTMgeCg3bL4OcRS64EYGun5qZdiO5XubhnU3TgrplHzwOQGtGJjCVoz6m715bL7gO9dLde2djG1wmuSyArDNMCYPw2HLa%2FbFUK%2FZ5msufxAH9WZa811ZAd2%2FalKjciWK75SowwDYU%2BWtGXqphFGxdmZ%2Bpn39LF7OAvt2RdzzozxAXJFsYELPAropyJDoDo5yx%2FoekTx1HLc%2FbhlGsPOnZYorB1hQGNSzWKWjnhsA%2FYtoqwtjNc7PxrcP%2BwX0lKYjgp5CaxdCZJXS9cQod3tLMMgLq9rH9sQfV2qFcPjAF7qWPV5hZTzD%2FU%2B6sF8XmX4t0o1%2FTQ9i3mSI2IzIjgjY53wyyceDBh2xBHgMeB56mY8PysHnfIPHPsfYaZZ4GdheDZQeDsqZltG4bsTJYS3FxMI7DwNIGOqUBqOUy0JBaamg2K2QiK6NGFq%2FwMk4CYpcGYZkLUCfoKrvESScP16gnROct%2BquBw43hp2pN1Ax82aNMmjoMim7wtm0eX%2FBTMT9%2BkRzlQuW%2F5uLkWdKl2pRwp9W0YyS5jKRA4A08XoWKVsjS4ujMEHvFn7xHsbQukgxbzxS4mLyFngEFRXXi8K05%2BYEhzajuhkwbMV2nbZHEQ9x%2BRMlGKZbkByqoM8Zk&X-Amz-Signature=615473203a0d429b1aebde3bca695e5e9efdcc6f199da64dad8365478a0e1c7c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
