---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QTHVMQWY%2F20260924%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260924T015514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCICmD7iuQi1whPqDyWED6h4aoh6B58H%2FDz7UwMkjyF1ivAiEAoQNJngUvgfrLKUm1InaDwlVcMCI3ZFB53VffaFiPjvcqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFXadqXYCKAvJYetCircA%2BvDs8yEr%2FyIJ2T61ZaGKjSgO5cgDMS0Ls8RjTawkfZVno72XszMtCGJOBGcqJX60SzbG0%2FVuV9J2onA1WWq5NjR4Q3lzPyz1%2FEWxErqmF8xxRGuC3l9GFig77%2FeGQbYt6A06smsJVrI1MGL1FSNpJhA0hqvgiqUno2tZEhIr8ivocm21fBg24R8e%2Btv7R0ywo%2BwT%2F4nHIZSSu15IrO6Cr8muTYr8QXy62nHOiBOtPxdOkz59%2Fi6mKUMA5EvLxBRi5HiFuME%2FslghZp%2FhGc7qcMQKlPi1mA9smuACgUS6A5U93rfW9pNnXS3s8WbHlCcojhzDm5%2BC3po1leyYQGRtWRaCtZRJ0IzZiPaES91QYITwMd%2B7jk5qzN6NUKCeT7WwxvuoP7QkWaF7myzp%2Buq0E1uIWV7rhgepHzLBt4P1XzJsVECKbjg1RH5gJ3dukHqOO9cAcn64CcG%2B75c%2FyfZmvdDYOf3CC%2FA8jAH52XDZRnycQw5lTs1H1zNxpKPCgcao4bXhIwa%2BoZFxV6o1%2FfCNlCJhPryoEZFKu9YaFKZxKJh57gQlaMQ8nXk%2F8qvYDMoq%2Bz0YY%2B6XN8JyxK7cvV3M%2F84d13zAGnbMc3KuN3u5VzR2%2BvMy9B%2BHjkM4Ga7MITu0dUGOqUBKN7s%2FJ8Jbm%2Fox2nDwT%2BHRLsmJ0C2so%2FwsVZwxDsre1Tu8PJjWj%2BeXkWcEUoedvxAjorWpvTBf5exg4QDXmHrS%2BilDblZzVAm25Xt%2Fe2FHVmuOj%2B3Ofy73L1I53CXXypfy6hbamydXKmXQQWL9ckGZ5Rb5Q%2FRtvKLtN6sl2XJU%2F6ysrpYc88SZ0YoqqfPjSeBuB6pa%2BeIe9UM06Q7QDHPPC9XnDhy&X-Amz-Signature=74574922a579c9afb749b542c2835e1395332ec628ef15f3b2709de9f2b25b55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
