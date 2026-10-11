---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637UWRWBY%2F20261011%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261011T211040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCY8aRMYUgx96HMf9cmAwLhc7S0uOX3d7a7eo6WRLOdrwIhAKF6GK38kkN%2FmFEk8vGLO7IU5C10TQ5L5MaK10Jil%2BzxKv8DCHUQABoMNjM3NDIzMTgzODA1IgwWuAwHDqyZchJiDpUq3AP57tQ9ykLbllSj9qQl9jNrIXmZnO89ic%2BTIaU3tSW3S7DWEopg8L9xEmBFy%2FRs59G0bu%2FZDtcqif4WeVMBBkJRIP8ncxkr%2FyPbSQehIExAeX0e8wCmZZ6Fl5ERYQM186WoxMot%2BylKbIXguR6Aas%2FKSYvxXWw6Oy7Di%2BJvbn%2BR7ocFjgcWfGKEI3JeAhthLdFZy6tNghlHx01jsOjCZ77ELzlWsb7fJz7oSIqxo8aDWXnZQuJk0614zlWqDMNhwgGsXUlEP4Qog6BFoZMHKOcBw969aIlfgpDmOiMXZIjxpAxAImSidHonsp4N2kadFebnbZML3%2BgPQfzO9BklEOZEz8QwkeKB5Ptt3YmYcGxlOf%2FnKl3wv%2Fq%2B5V1hAEPmEkQQW9glK6gqJ2mMomVOP8JzsYQXALQerIrv6FDD%2FJgJmYuEsxIWdj13XKN2pxer18oQ%2FLBNwUOSelho%2FAz3qLAxzj3ZvbW3R08QkNEsgGhQRYyHLZCi5qw0Mf1pmAFARX6bh%2FI47rlumTw2mpooFA0Sh06EZD8o8Zvzo%2BUraf%2BWMphJavwnw9K1ysJRCdyQnbwN7A1r6ajiHE03eOt9JxF2FRA1VfSpwx%2Bb8jycGIed%2FI4sxhN6wBC0t6J0jjD366%2FWBjqkAeIGbVG2W476CCLTbe5CZZpSgvQd1HQovbbWQaTWHD0DcXTH%2FdkRrJxCKVOE%2Ba9N1OlTm2%2BG7lhE2OFR5Xbh%2BwwTKP%2BUDaHIj%2Ffz8PhrKs0ztFzpBZlDIyi0%2FixarXBZ8vTIjXMD%2FFRc0b0o8azmF0MdTj6YyM8iuaGqv1VvFifVWOxQGEm4k7qSwAAPABE7NAAb9aNMP8Fqh3RilLJknV59GASd&X-Amz-Signature=e47a3c50f124637742b32e73e34d4f9ad8cfd5903c81e4a9f4d5771b1ed2130a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
