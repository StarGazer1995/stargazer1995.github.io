---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HPGYCUR%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T105833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDoaCXVzLXdlc3QtMiJIMEYCIQDPFZBVdHvW3%2BB0rIdI4OtNedgPv5MMSv8yExWickIzRQIhAJIY%2F58IgUuRFXAcp9PQj8pz1sT%2F0ESHlfiCv2e9XV55Kv8DCAMQABoMNjM3NDIzMTgzODA1IgwNwDdCyHjXjlCgVUEq3AP5RlzlcN2mKjaMT%2FJ6KrDckBUjkui7sDv5J9JgTyRVJkbXBRHRf4BjQGlQaAm2qA26BUz%2BQIGjCxk15YWKqhP8g8TMGdoRPkmWtTsek35TJls8RqKRJugVUGwvaSbVIay%2FLn1Ir5o7I5UkTuwdBCAPeJUDHVkREy%2BvscdGWiUrcrIGaJjuenw%2FlaJrm5oA6TDTwk5WCZNPSjbGPWhPrqt9OgC80IStCjJ7HleavSxkh2uMzQpA%2FF7JnKmV0ZJqIjg6%2FRsvQCljhlbnAZ8Td5Av48qPOrBNa2YqXh30FF5tpi1KO70dVz2U7BmKvRZFbWsZmSmJNak6t786xUn54WEvtNS9tipJS%2FMTCEDT3HCOtIjvOQDiDYyle2rr9Z9ug%2FxLf2ioS4mek15ip1U5P6rf5KUpAeD7PYxDamSQB8dbBGIttH%2FwOqgy8AzL8QgQ6od2FRrX5nGm3uBSGZt3%2BNuyEl%2F4m%2Bndoi6Wh%2F8DTctewRpQTn0obHWOafqonqSrzzTjzTjxlAy96HsS2xNV2GofqoTVyU1%2FDXuICOI5tGD%2BhTpYcYyi%2F35HLSnlYG3JNMjGyNZBApmtJhjih%2F27nStkSLdMn9N%2FuD2Dhph6%2F5sObvVMVslvyG3CCpcLGDDzr7vQBjqkAfsoM%2BHl352GJR6EJKB5WLR%2BCnzoi6Fg7FhO0%2FSuQ0ZRyjv1J8iQ6UGecPlHfBAxCkEwHwC4RDIEX4IbSxTXXu7W6SUif558yjbZM8A0L7OImY5fHb38NDyqSWP0QupeyOhpEg1Y5F9aiUAzh0BSx6lButL4bgByhOq1aVH7PCT97w0vnFx%2BrPlmuJ3kMiNamQZkdW6iGdlXJnWmfz%2FaHubdJIGN&X-Amz-Signature=5fbb708512ce7f151ec621a151827bdc18aeffbdbff2311bec3ad07fb837bb2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
