---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666C3TXRII%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T210300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBUaCXVzLXdlc3QtMiJGMEQCIFt4Lt%2FOyKKC79NEXzkCN91EsQp8VLmn2HNwgI30SsTmAiBx5gPGNu%2FdgqQu3N38RpFWkPc7eOJ5ClOARzfxO8FK7SqIBAje%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZL%2B0HkNHjIDVL1K6KtwDWXmlDhsdqz%2Bu3MtxxCQgtNfLQaWjluaT4s99s3XrxMnqrEOlYeEMMqwL5m7W06SlXm8R9BoUGxFoMKWvEK3mwM79LA0JPA6Q2cyivUKi6dTOrm9FeQSFOWdQvOmU1GESchZhO9%2B8nLd%2FRLfTs%2BJnXxOzpe%2FVIZmwqngLyiJbkgC%2FC8AtsJX8wgFEQueBVyXnSelgvTw4kfPX4JClX%2B%2FhfgyePwJC2dnlXjyfTVoG3S0E2Sw0oqr42bPk6ep7RpDMxa1EEzrdR8hJfd4uxA75zeX1E3%2FWaoO2lLc7XQGCuqGRsaw1Qzctk5l439QEMUbuCgoslzs8wmqVdyKHDQ2oEIVP7MWPNPijZv7KnOzFJLRtlygDNpv74zfWNmV2IlaR7iva3paaSKCpeVcgDi7DydqLiVWCNGBwT9FjIzoIAMvdI4yGD3L8ipDel1OHEttdjQppLeknSbSarNv7GXPKDbmClhNNZDR44E3i00sq%2FbeoTmU2Vn4PDh0M9zLBMtsYdZJOS1AkaXM%2FLojB4vPw%2B9r%2BX%2FAXCJSMedOW%2FEa0tu7S0ZbxVKPtmc7tO6KKbFot8fGKo%2FjlwmPb173N1SGWdoLHcfRIf8LQ84tk7gBxcQGj9gIDOh9KmEMq7EIw7v3b0QY6pgGrJ5E7YbIIj%2BAZMZHDHV9rYlyjCo94mpFEw1KySmPKqn%2BALKqYzHTen3jyLyiiopwIZziaBjv0bctWkaW2wc4b2UFXp2poPSjJbUkBFuA8IxXPQ1owMmqXJ4wwziXN7yDXyouw7LBX4KhiN%2FYHqa2n8RS6EkPCGgTlINxfS9%2BBieIFbVRxX5R0s%2FLMz6tpoXbVZ6npRqm22rHZZoi7%2BCunDp9F3HJy&X-Amz-Signature=7e41bdb01ec4c312dcc4790efddf191930b624bd4d709adfe83cbc31d0419e05&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
