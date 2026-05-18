---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VBKNGZHS%2F20260518%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260518T192245Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcVDs6qHy72jmnQpKztAaLWvqfkEgqMliplmHChT5ZnAiA0G3tIWplITldUNpJsa4HOiJeAYeb8aPzeUQ5JJdp0BSqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3W6qs6AC8UA2%2FXZ%2FKtwDUCDghxa7Jt9N9KU1goF8sLMc0OvpeTNGngBaP9AVsTVnfrlcJsiDS86sZG%2F0%2BRYvpchvjXdU0HT1a4up3Pc%2B8wqMqtKcVuz29piuEJbo3nLx5GtrPPwuohJzMNZXjIniPhKMvfLN9x47%2FTUa18%2Fb4ZYeYKgPH2kWufLBwRMlaVCTy5ABtQPjfzARsi8cmrJiIQzPeel6oQGGzXjMUh8v1u2nv6JAYZPhiYGvcObs25y37Yup%2BSyJpOsQ%2FdU2x8c1Y0fuJ6bQcDPWxCVvHmf0sFi%2BqPVAfTA6SnNetRf5a1aPLMzXjIH0zBwmIYYHR46mV8nus0TsjZooBBmT0CGeltDFjigff5AwMwYD6H%2FIn7XSPhBcZoGO1UTNv21IeUzkrykUyijdF9H%2Fi7aMAzYqbykEqoYZhF3QOmlBsUMHR5Vip2FTwGTz6uSl8wvsLKLccE9%2BX7QyxWKIqHC8twD98oDitS%2F8l249dNFgKwhY3KXiAnBH59xlBUQTJy%2FYDiuMuDfDbBT3HQZ98%2Bjkb8AYs0F9NW%2BcnjuyfaxvWfCTkzk%2F7ef1Z4UP861ZpiIlQWdru7M5hUWyWt45cK5dFSly2R%2FAA%2BO6y9L7m8fRrjnoIEWeVX7tX4dbDc2JLAEwv72t0AY6pgEp4AIWERYjSDx%2B%2BewjDsAna9BvHuBLMRiOxR%2FPW47KT7Oq97uKNzxL3eANp%2BmYwFe%2FtXiepboIayUXcK0YuEPu0O1pVsIrParxDGzypY%2BImUDWXEpw8JU7dY8yyBS90nLg31XVNng62DB6bgI7%2F%2FOk71JIi2sAigJwJlfNvzPItHsLbuPNuEQtLnQiwSHVXV%2BrX0fVI275dCTWKdxvALwKnS7TS1EI&X-Amz-Signature=2626bb33686edd5881c41a0ff3fb07307fa562c07d69752daf1cfbfe8376e1cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
