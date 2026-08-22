---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665L5IP7Y3%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T061918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICDhLn5%2FQZB9rmI1jdswAc2CNduim7uaBocAqGhDOePQAiAktRiH%2B3M6jxmaMPYap9s%2B3iYfADid9u9GblHBMINcGCqIBAi3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrtxt9htiYAUgj662KtwDvFlNqfOuDX4s6Ls%2FHRZch9yRFHjk3MZYDOxqri5vgOn%2BtHCkHftryxXLe0Tp6IvZiWwWXD266dxZ3SbdW3R329%2Bxz1FOuygeQXRpTkVeVRT%2FeoX4m3qdA%2FtF%2FD8P%2F7b806o4%2FC2Zbdav2YG0EEL5NSVByGdD%2BPL4uOW6IM7btHisbeKuGZCWd31ZjCkgp6i%2BC9DvU43IY8kEFmxb5BmMr6G5MQfqnPHRmh4hzys5GpEBGGxTJsQZFk2bs2%2Fl%2FZ3phUvpPauOGlsJilSZAkhRn%2BtZ6ffuiu4ddESzbeM4n9AIhbLJYRB%2FJHpcVQUK7gULRhv2YgmJMo4yhwo5hU3qculT9bSPqXNHbZ9vAVG0umqZP70aRUKj7pujUBzLAJS0N3UTEA8GGkEBJA%2FL0wq5YWl8l8k%2BClH2qGDH5%2FO3sgt1OuR6tbwXavqIX18%2Bg4LnQlwY8pJxsQw1umOSI9NG%2FwABxXLfnxNY3I4BZYN5GSdPZPxzGQivmiEXW5Qgq00g6nw9D7ocAoEdZgoiQQ8joVJnMqNLSk2eEuQ53a22lOnWKO%2F9ngRNkEWehIi8lgtIlksjeAyRRV3JTPY710jLbd1AoKozic45PhX8tMU6IoOuI71U9Y97NNw2dAYw1Pik1AY6pgGYoDEkiP%2Bd3P9r%2FgPAxO%2FJEjn1EalaLtitb6LaoKGZh15FLuZvCMURqDfTmi2JSnzgeXfj1ZRr2qfpLtR5xw7KqurHhp3Ecqt051BnXKPSyMo8hfq9lYhFByXoJ51N1vUQ9W3qM1ee5O%2FvxGphqQloj%2F9Nr9tRyWi0BVa6g5QJlF6WIE1IT3Bz%2BTO13APs%2Bc2RTxoewPG6sTTwMLoQ%2FmakUjkP0gP8&X-Amz-Signature=919d8e9482d2d62fe41e1206bfa4ad6de07a184dab2c0289ce3df52d545b1636&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
