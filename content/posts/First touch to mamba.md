---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURRDRLX%2F20260922%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260922T125450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMlScvVhYde3f6CGesBo0JaNEtXxRepFiq1Hz%2BqD0UDwIgN2JjSlggl8pAxAFX%2BaeijgrAZarhZN82pEEraBbMdWkqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC5Z4EBWa3YtdS%2FSxircAzuNQb3nhTJcYsIg7DTqwjZM242mQXh0RB3oNe5WvVxA%2B2fd9Fsy%2FDLqlqFBfPSzLNBSsWQwgLCrLyZChcZocay4qfh1pOJw1jCnvOraYHmfDwZXw86y9oNei4l7VjqJxBpfc9ZLHdHMV1bsnHo6PUUpetP4%2F%2Fse55Qt%2BcV2ImOxLPo2OhvAhvNlqdtrJqX7dUu7hXo8oP8veMRyKb2ruTm87rl829q%2BDlKTWIXeKQOuxvHC9e%2F9RzeN2GjevBJNuCi0txeP15fhVHql%2BIkI9CGI%2FxOhe6jVz0NbGtfzH6%2FCmTWxUDF4RAnfJ2K6E5a2VjdZ41MlV7k5AjvkacOdiXFyvJCHdlGpJoO1uyniSIBUTNWQiTTSpG1jLviphvrXt4XAofPdM2ZBniepapvQCM0%2F7Pcs%2BRyAznthrDv6qfJaYIIuMNaHxjvYE%2FGYVZ9Y1iqQlu%2B9nA1rypilc%2BKkQpOSjf6wr2dOw4QMpFovNgxhmLvz%2B9hS4umKTr0k0bbTZHSUmv0VAckcQ0jKg7kopzzXxhvob%2BvaUOcNWLJ4wEOcHXkWvMiD50VkFx1b%2FTcosFMXju7ITk%2BtRGgYAX8ivuMxxnBgx0tsIGuQ0cwfrhFf%2F%2Frw4G0QwUK4iPWTMOnlydUGOqUByhNhTsZFUu451NSK1CTQ75YAFOUHRIMh1bZ0jUOdxv%2FYdsXE9P%2FELUEx8%2F%2B64iGuRt6NW2%2FwMKnwpfkwCVHNWcqUk1IXf0%2BCwJIoOBydjcr8%2Fj1qeeSYi2zvogaTHOSpJZLU0O3buEiyV1ZqMYl8Ug3SI3Gy6BxjroD1Z2JZF0r7XXshaT9keRlVas6UrWYThqRWfJ9qyEiWHMD6cE7dygSDdLOQ&X-Amz-Signature=fdfd29f43ae6d7ab954ea07c29c784d87ee889da7ca9dedfbfe613a2c3be2182&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
