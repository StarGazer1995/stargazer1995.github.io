---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAE4CQQR%2F20260625%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260625T230711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCo6SAstuf%2FUWHkXY%2F89D2AZiWXpNWfPsTV1Y%2FdXW3yiwIgYS7FKFT0nPKVYJ%2BcTAQLW5tTUiPrE14E8ec0R48Gw1Yq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDKZlUSi1dTsIobvlgSrcA27ilZ1eWLMRkgjpI5xQJfbfUfSEg%2BrQ4R1BruwcgVrnbqKuH5xNp%2BIfQQTuCjbEgkXIOI30zmt82s%2BJIdOBOvyOQ44%2BCm%2FB8xQ3OWUaCNqW1HnPncGgQdVzB03KF%2BefiJrou4RZeS9ZDMeklNRQ%2BvgnMAh8opAwTF96ijIgl4ffTjNnouPHvwV6RPfdlzZw1lr7HwrJsSknQlOc%2FHOxj3r19Af0PzOMgdMTS%2Bf2Xrwy0Ra65pwmGAeLhzuDg8wEwvFC7VfxU2VHEEHo9jZ5LrnHlZ2225MIm0LTFFS94NvYxlqAewKqcKcXjYo6%2FvEbZBCaCAuqMWihxNSQT2M1U438S1wXZQQXQ9IprvHYnSGVvdqNh5Mnp8jnhyOR9gM3oyt9bDXYlNKSMg0ZMKgLLB3PxXcEZHJjgr3xEZRPdy%2FKoBH20dKlgDYh8ImyQ84trfo%2FFf%2BcJ5XfB8Y3nsJOprFP1FfKtTaQEmzvO7kdQFuAn3DHAU6iNb7Yn1F8PRPM9aba%2FX76EIIOXFlDZ8fag7ZHEX1muyfOtBuXnQQkuAr7FVLGSg%2BBRLX%2Bk8X%2FxQFhK%2B0aOq9NaSI6a5b6wV7uqr9mYYx96gVztBYUiiGGbH95%2FXKIBocpMN46Hi8cMO%2FP9tEGOqUBXZlNEx4%2BJkXTdMPB0cyvmVhIzVXvIDPEWD2ogdGUIpvY%2BbllFnNm404TJoWM880vMGj%2FgZ%2FqbQ%2FG9ArQqHDfCd%2BNDBqHrIO7xIHkYi9dViVxMQn1MGbHGeRc%2B6Ucf6gAzq0bF7S7IPwO6E4UnZ%2FPmrX0JHcyKUaD8Ek4gRMnfnZNm%2BMiwdCIDUlduOLRnHk4VFW8AX62LYvvmuH5I79nf2h%2FWY2e&X-Amz-Signature=259eb45443296907e6da0c461cba47aa520d8d7194a1c79d270ebb34c32bcbef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
