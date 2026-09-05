---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675WUKARX%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T112744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEIaCXVzLXdlc3QtMiJHMEUCIQDIDHCZDj0iKtRgXp3nQUW1lnPcZx2lyE2F9s8msHrgfQIgfe4Gh9wB%2FwM3uDdGfRuzGEdoIR0%2Bs6D4Wh3aordR%2BLgq%2FwMICxAAGgw2Mzc0MjMxODM4MDUiDOtV2HqpH5RoKQI5xircA%2BS0tVMVr08Io0G%2BuwiKZtfg%2BAxgUXV43LojMNqZ8VuOrkWTvF2WYyMIuy8RfqsZdE%2FKqJVz5WFjhN7MCTmLpf2bne8erfhOJ6SLXIZzUl2HObrLOQ%2BmynT13zTYKRByL2JTE62lGDMdvlaFQ3LcRexgsiGzfnU1ZVCQ8547rCX2jssG6ed%2Bv3Zi8s3UAm3Be%2B0nfKkzN4yRv3XsZZ6HEr%2F09m%2FkRJdQoTO8yCQ93XNGUoJ%2Fs01KsPU6%2FxO1gJHdZcEXkGJ5GVAymcDvp81WgnbCVY3s7qQyBrujLWiJ8OIfdJ2e5t8p2gtwhUYVfKse%2BDaftTGCVK8itMSES%2BjBA5FrXQBm4yH5gGMXIf0oMvSQSmMp082heUxVSUamDUYtPCfAWeDbVWqOJZmWL5cye9BB%2FhVRWXsHpSDtxzQqEJr0RwMcAJqOWZkFJstiPTSeIYPze5D2xoDqKK%2BKhjM9DhjP9I0DdoGNhotzuGjkyBW3pncSF6jsTn3mO5EUCnIT5DS8YHJ0idx30cY2fROq0u31ZM%2B7Yy5VWfuTvFPJFp%2FmYl4cP7F4Myw0uJO6btuUINwbnezWY%2B0uKK5Rl11D%2BuRq7VUZCAtMEVrEug38luRx%2FbGNT4%2Fcj8hHqjySMPzX79QGOqUBcbrud5rj34J%2Fq0lqMAO1yN%2FpTI4Sh5FeyqoqGVNn6K7rwI0AYSZQdhZnKnkiXmHaq4WMWr%2FReBimwIsUMsNnOkJhQlSSRj4%2F2kZXsYeBAWJfYInhIkjVXkNZvXfPMLnj6R%2FEJQX%2FHDoJmdfdAHz%2F9S0AtgP1mS76%2F0baNOHl%2BHEunFVoPyHJrGMN4EZoNidVPp%2Bynd%2FZZiX8uGbCqab3u0HeGFxY&X-Amz-Signature=eca9aa6b34dc02d81ac8d59e115fdb1e7f000bcfc316ed374528e3872cd6d0c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
