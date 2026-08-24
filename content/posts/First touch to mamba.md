---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVWBU2AH%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T063332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGa7oiw6ykYv2ZggzdkgEdxT4juLDgRugM6MkgK5dRk5AiEAmsoEqHWAwWUHgH3xhKX6rIPIvagootOPKv6ztLBd4gEqiAQI5v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOttYw0gU3Yg9D2RPircA4rIdCLvZOCRLEuOf3LqC9N8mdgrYJWZUL4JzHONJWZ7HXV%2BA%2Fg1DRkcxNfy34eNfD52Gw1uLsuQbPePaz0PxdwsfKWnoZrfM%2B6n%2FcwIQoHkbX3IAlQYFArZWBHhfaQLFrWpVirExV%2BciSp8U6QT9cuCiK11MzAVhgTmB%2F00uGEDECV5oJNgoQQBln1%2BOTK51Wy1XPrIQ%2BtaL%2Fl04OOr7e8%2BRuA8LTgv4sbZBiA0%2BT25ZUrrK9MLRWS0dTq2l0r8xPafeeH1whCjaom3RxZVc1v%2B6DQuJ7zLym2jQoptwXRbOPhjWFb350m0Q6UO00tf1hXOh%2B0TlrgNsYq1zy%2BJkiS81jrSqlSA1Q8V%2FQ5RI%2BU8XRq71%2FPpM6QUkkUJCSQtSgRUX%2BaImy6z6Kd%2Bz%2FHLMpKupwYvZ1mASEOcsQaLDO3doodq2aTuukC9cFqlDv6hsl27OU4ZkU8IyCHdroJRXV9UV1AQgA0hBbgzIX%2BOKZX525H8D8Gp0ZbWm2%2FENaZt8KNvf3dkvM15EYa1%2BT8xElPrn5Wwv0xvbRYkLRljHEsikZ0H%2BtuKr%2Fad8zD0RqRyX%2BX2oJ7Wc8SuSddGtLw866IuP5fEQUfxsBOZ9cJ%2BJmKoUmTA9gSCiH5vjLmUMJOlr9QGOqUBUulY0Br%2FZtjEcgnjqo2r17R4NqGgGXJP1ilXXSs0S%2Big1DgWyRZJ9X7IQ3LKYeYPusLJXQR6wRXYiSG5lm2bpZqn026SR2R%2F5jZ87E0%2FMOoQ5VTs%2FegXEHjtu%2FVmCNYK4MRMRAz92Fs%2FlXO6meIIK%2BG17NeIfIG3TM84OaByGBkjn7ExehXhghOCzpI9eJRiuDQzC2PtnK%2BPHiXuwe%2B0oS6VR7bT&X-Amz-Signature=3d5ec2ee471910ced772ab85e3a1f6d20cbe6c6620b721a2c59d4ef9efd8defc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
