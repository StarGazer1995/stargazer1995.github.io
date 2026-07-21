---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TTQUUMLS%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T190344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQChpVh228YKiYiXDLCQq32x6Wbg7Akyr0NCxm70HmcGMQIgR%2FWEe%2FU8N1WKKpDx%2Fj%2BtE0iJbGiAbZSZXGqQEP2tQ0EqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGWkB2bcRWPnOH7EHSrcAxFWMYlIJXZYtGZHjBmlQo0lOpaPz3XjUU9QYMipYKUI45yfubnTy7gT9Pm9kMMGjkxrlNkKVLCmwLpHYAx4k%2Fb%2BmHzPcVuRZjNAEz%2Bdt1bSB%2BhWWFX6YUOpGzQp7%2Fa3wUKKF0fXOb1jY%2FFM9VDXf6IdE6OcjyNTcIsimyxiJj0RYG7llHFp3LR7fumP65Pc1beaV2c%2FmIG%2Ft4Ob6kUjGsIgsriS64SLm5e%2FntUNGgUPiepL7Esq%2B4wq0NLGtXxMRw%2F0feubXZOcrenM9bwpXtxQDZ0dPNfekoLWrqV7mACm0oyBe7npbbS2jO2w4suBdwuOn30gxa0XpgTohFO1enL2z6ezmJ51VKfk5%2Bu46UZqbPEgzg2jlVAT3qwL1StOPbgX%2FKjP284H3euaY0SfoTt1XTrcSYotMYJ73oLkJQMpetqdE97f%2FvtOE0LPQ8conVgQMfobyIvAwxaxQDdl7Tqpo0%2FYYD1Bal1kbgcIr1%2BoZ%2F5gHb1zMd4s7aZBz1My12130hvVDLw5tZ77MqXdM1gUle0LUrMnSmVJ%2FK3fNiQiXO%2B2tmTBS7WCQHpT4Ov9Dqe5pJ14L28ki3lBoMbj7EFnFzXpCEA6aQiHqoNM12k%2B61KMWqcOp%2By0r0XOMJqp%2FtIGOqUBMEWON8%2FMk2nO0ua7dYbhhut40gX3AhUr%2FVCLSJO6uIHZTAZaWPaB%2F7%2BhidTJ%2FOJyGIbPjv72W6VqHMF1g7dCJCSBl9OAbZdmoFBGdZlOot4nl%2BsISES%2FDevViSDKjFkbQ%2BEBNG79hVVpdd4D9rJddI7%2BQY%2FM%2Fcfd8Z6caLp%2FCuP8lW7E6hVwpQJ4ymdE4Z6m2Db3EQsW6qpy5uT2oVJem0LqKW97&X-Amz-Signature=be1a6df943bf30ffe13a45bd5c14f6602d294793996882e863ed0c095eba75cc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
