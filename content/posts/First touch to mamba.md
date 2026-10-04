---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WABU3PQY%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T073228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE%2BfCPnhtGGE1bgpT%2BgE2u6A21rc3crZ%2BoijQI2eLfqwIhAIjkqDwvJnJRAP68oiEqcN3%2BqcwycxpYEXkHf3gpUT8RKogECL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyuhDrYVqpHh6BnLWYq3AMJLMQihwNo2Vu5ld9Jy8FxckB56O2I9u64hRxXT0cPLQfcGTO8R9JiAoVVvcFJS9uPkjzdY7QQwqvgWSPGcjMOd%2F4waglpBC%2Fz08y2df9zxG4DJHF0xSaRmp2ElmWVqmNif7HHYrphvJ0%2FN6%2Baw%2FIbGtA%2B8Gf3%2FfKWWqibE%2B11KExQmvKuNRdgqh1fRA%2FKnPIrS1Sn0Y55rBfoC0DEZEV682lLhiI3BnZn1tbAJfuXzWbEFV%2FhNic5zGmpj8lNi1lESytTCWCtsNU5pHnyAvQHBhVzznv2jdxSJuU6mGb40OzDSccQmGm4DE%2BI6wJktjI24eO7C3WJYlRGteYrFTeh1z8j7GlW0SDHfL9M17wAIEuLBR1RuXPx%2FLRyIDAxJJxT6S3%2BQ4fiWe4jjxogHuZsnTse7zj8w1omJfWDJU8wxTGNqYaGoHX%2FL7%2FZm8a5XPSPmD7cn8NXxRAyjntnd%2F5ZxDNVL36wIp13TXSJ%2F%2BOMiK7eIIXB3K52E0b8gqiqaGBjzJpxnJ1DQiiE1L%2FGULGrN7sw%2BJKtFa9GMk4dIZYK8DQpJ%2FujvAF1WJm3dp2nSbGP8Kn19VZW2TZ4EFviira1srxPRCrrv9%2FB7u5Sfnn0p3018st35zlnVMD27TDu2YfWBjqkATPbWnDbYr17DSSqlR9crW7SCNQge2QQ%2BrFiYhqnQcf2EXOa3dhRag%2B4vqcEkenWlu0RZdkVeuYWQ8L0tN3l6dPR0CajfXzXh4TMmAJm4bREyLdJwKr6JiAurKvxJuKppaj5JYQbMSxf9TOECbwznQ7DxZ9zkd7LIFMqKK2y38E6YaZOONF9gvzV1PhyDfwNwREuOlQwKsA0HWSusteVMm8OCczx&X-Amz-Signature=627e9fd5b602a7ad51ac1735e3da7e0fdbe6964293f32d7d7900d7b36e166c42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
