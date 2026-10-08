---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGWCAJTS%2F20261008%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261008T170904Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDmLK5LacsYwW0E2tPxIB8bb2S9VJNUrmGMT7bQp%2FsoMQIhAJjH9kVwyDSOGkcOS9SSTbqzu13kQHpVZ34%2Ba6WyXLc2Kv8DCCgQABoMNjM3NDIzMTgzODA1Igy0ld96KqrsmCwcW00q3AOZw9IVjHanB0Wpc4m2P920SDDQqDB1KsqvBVFSVervYI6DDAjFZZUph8h0BbDcUT%2FR6W%2BwyzyzhyIoXukJoG7tGmy5b%2FiC9bxmmLwBld6SCCO2%2Ftubosha%2FurAVOq0h0Ahq2KEVqQITCIQ78njUrVYqD75boItfLj1PEQ8HYUf5q2qgUgC7%2BC65svkLkyuNNLD2uKwxBhQoPdqTYQUSNQ7vrGHcVRXo%2BgmYTkCCQ3H%2BhIYqOBtByLeXdt6nsgjUhgLf5Ia3emfQKf5QDisXKcIr0%2Fn%2B9roNPFkqvlq8bMshCOii2M8M1w2sEupiaSIO1vMlTnae7px%2FB6GiOGaqc8pnepU%2BgO5CG9OeaKjannQQ6sIViFMJhdTiTxDU%2F0Zaaf%2FEnSNkt%2BrPmzzQ5vS8t4x9b5zotAzjRcsbV6UgT2JdDlHcghWJp7v875%2BpEgg4%2B%2F4GEGmQZRr9mVBL2xkf9n29g8gzY8L0KPlxRLxfHdfncQUruwcnwyrlhgT3sabzBlu6QAN6TfgRgIL02TNNiCp6TPXDnLXfSnyP5W74KQsctM7KQvEQ97JSLNgzhIG2Fgx6HFFNScEcvdGu3Ilvigy4IKhcCH9WkipBP%2FpcPGT3QNNVSVCtX6v4brvrTCO8p7WBjqkASTkGYAeRZlaPaLlccIXPQByifj37WpKeMX5vvXSzD0EWeDZMq%2BzKSGBmdrNKmRGlGusmQn%2FOyp8vQVLj68oCEMkzvxM8GO20J685UVT6OLjfCLdXJFI42wG%2FUrMsj4waapYudWLWlqmDZGIiEdTMAOvr7WZW5nbfAJAH%2BUiTsSCw%2Ff3Sz2vFmWqXy4dRacyfWaPcBCM2%2Bn93%2BxwlOVjQcQCdGOz&X-Amz-Signature=9e8d5c1c3c46aaafcaae704b900db84d38459bb04e6f4875b70606c98abbcd6a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
