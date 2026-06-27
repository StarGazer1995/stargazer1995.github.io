---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XC5EWQB5%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T150809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDGfKUndKz7bAii4g0uhhK2eiXLWum7DF5OY0KO6zRbwAIgEYNBkTf6zu5fNrrzwsqxrpH1rQXC9kSJmscjtYQ%2FJTEq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDP43kacoextZ7%2B%2FDWyrcA%2BvpuoB4y3hM22QiUgwQYjHoBRoh0FB%2FYTPyiFUkqZD9vZa1%2FycBjUaRx8ZMzxgkCcL8UrUU6134lCfPKqTcJp5PzJoST%2BoJuIWSLHjnNcmYIuxcbEiYLZHGr5oB6SMCtww3CrBQlRbhYoIDr4yLc4dXnDZq3v5Mr%2B2h7opnw%2Bxgk%2BezFGUa%2F84GrAQS%2FJi%2Fn9q8HL5b%2BspIOIti%2BiQA5HH4oU4nq9Emp2xn5XwcyAAC4NYhmrvKulENGs8Ad7C8FF1vyQffc3AZo%2BIqobi8D6wQkuhtIy8RGF4ff6kgNlJzWGtIGlbwNgaWFha7v%2F%2Ffclu45JOImMa%2FlzZf9j1DplzlzmNSuXidnkCCoxZzo787WzfMCBXfUMHjZA3szghFk0jL%2BSRYPsDqiPiyFNDwCrUTao9hY6Qp%2FWXxq%2BAVWm%2FLC7Ta%2BcLFeWgQfTGc%2BGH%2Bi28yTXIzGHYvYihc97dEByMTnM9bXffsKlXUaaLkLeoLBR323YfKGoMOg5ENyuVEZK3ENLOp37RDSnGPRiAK3pwn7HUhN8CSx0Ads9JpNw5ViKP2tvcypYRUbtMCadwTp9nba1aMbdeLDI9clmTr5BWtJolzt3ct8Y0oMAs06O7zDE0L%2BmWD1d03Pt8UMLPG%2FtEGOqUB3jqTtnk76WheVmvKGLfI2J7De1VXYWUifvbMBaRda2nl8i8MRtEhBwF9LcnnB3YyYZJlz6GpIVer1%2Fa8dGp0EOsjnMhbT9Q%2BaMfLdNB9PvCM3TDF3C%2BcrZ34paQEm1Fy5G9NrJYWKCaTvNUObvuA6hvsTuoTsPhlPTBBDuIjNIDd4X95WV9NyLGs%2FODWLnwWHtgikwxgb5InEYNrys7VNzJUmyjJ&X-Amz-Signature=4473a16856964738a57f836b6d0875215bc03737011cd63442cf36d1a78d167b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
