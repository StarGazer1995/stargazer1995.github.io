---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWFLI3VS%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T043439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCICGI8vmYLo%2B05w6xgIbCCR8ztlNVflF2TUCxZpItHopSAiBF7Ul6D1cmCykSYLBhiJAWIZ3%2FvDdNq4zWRUc1WsZiNCqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrl2bUJJTqozCQhgzKtwDnxuoH%2Bd%2B6YYkQCNqpmSpLYtjJ%2BywHc01uujnHo5qPf%2BA9sWnKCfG4N9KwsX%2FGT%2BjEu%2BhnGhelmnDZWY9TQOzgbReSRXcxUsYJyDk2iOsmhxnK5wEazgCEty12fHxx%2FQpEBK6NbBV3Qr4IpNauwMAm%2BjZTxkd7OzZrCHhbCyIyTZP2ElbyeGey7nFamhQr%2BmqpnfyJepHEP2w0d6qKgB4ZApgKiKxg8a3miVLtfexKlOoDHWTC0Ydx3Kn%2F3zCBwnk3eUQjZgiHRQicJ7%2F1unfDoO%2FAMr09cVBjrmWypw4%2BFy7M5vMzEOOP7a7OjqTIlPbsejDzDnDB5xd0T5lUwNkPtaLV%2FDfi5mZYQq%2F03YcrfOMyiNZ9LUkeLOYVN6QtLXgrgfJ89C92jnLTEBuR22TBCwH%2F3eJCBjfvlisyqvSLwZH5mPHKGVaxdUp%2FkT3iQ6SaizDekwkHffPtq5kJJmm3LX2JW%2BQtRp4MQ3uLD5Egn6DwIa%2B%2BOk%2BgHbEjAKK3FxUznfMpz%2BUfMY2OcK5pApoY%2B%2Fy%2FEebPHNtus%2Fd3ZmbJpHbK1CuQJTI%2B918so2RmmcWXU%2BJta5UVtkN9iPkZCXol5m%2BlXsR7eycHM2zeNOeJb7AwdS4kTNNLip0Y9AwkOuu1AY6pgEMI11r3zOutc1jCjt146osImDMP1CuTKaK%2F51Ykc6sMVAaEw0UwiGIfKqJwyVGBVPWgQTP0NGTgLcg0udNOoJMzOtOLqtXS9KFuNs29Qp0NvGcljNcZ%2BetWJ6DOKj5%2Be%2FdqTXqYrcEeuKHrQKBoMgya9ql73hz4hKD7HBAOKy%2Fm5qWMT0HpGB4nKlN5TbkPADz4W1woiNAf7V9W51364CPx5BKCSCd&X-Amz-Signature=27ef3f49b8dc0cf572db8adc2c6aadaf692cbc51388a9e97f1f1a02f7481c509&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
