---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKP77MWC%2F20260711%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260711T164130Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDs59Mu1lKcF5zVGlxaRmxlUGqwHEqtpnBqDNtY0PSvsAIgCszy3OpdtuNYeObH%2BPOwijkCOPM3ulg10C%2BaV86nACcqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMV%2FiIu6cpItoNyp1ircA6mttfB%2B1W3Odkn7BELM7nFjOZpdK7otY9jgcyczYuYBN%2BsbAsGkGGRtBL0qWgveRu%2F73O%2F3q96VZJ3YquW1hqYcH%2BDsx5F9WusWNFIquRbrmX7Ez8Yq1KPoAxep9oz38%2B316SIxv1KcMTCpO5k1qApkUzdAhy0%2FfQ6bizad4q25GoQlF2BirrOrE%2F1CNA3lWdJwEzpk76lt8%2FzXx15a%2B0M%2FZE6W%2BBgONRCxa00LHGCz7sE5ycKFgF16YgN5qyv2GMG7%2BLpRdL0%2FCKKVshBZLgVcnnCt5qyrOzEdc2m54%2F5CrLnN%2BZrVR3TuFOF0yXvTC%2F3lHWXCF7zHts7QEEQ5Oibm5rTL3Ziyiec56TfTOEAgqR94Tt4BFaNCfedAdB5N6UQCFhYbReGH85cRS1k9xPnaYDCkSgEJHa6k1t2tV0i4mj5qJO2pwQXp4FgepIscKC7Ofk9rSH1qtBUUatWqo0auJfPEuYDw9zT8dRsgm%2BihItLCamocJooYTHg8Jdqzu4xUkBjXFivvh8%2FlLgQ1QDK3O70eELoD80BeuAq2N6P9xrqfWbRBM%2Fdj6wKETP93vWNeYnsBbXszYrNBTut0vd%2BtD%2FXx%2FEUHEuivHgO1K5AVpRpTZctxd3Ojo2zlMNzHydIGOqUB7890bZ%2B%2FXZ95ssZ1mAPV5ZBxDbEJwMySjODXdb1BHWWZj%2F15qT%2B79x7pNiR1aXN%2B0WSbSA3qNveI6%2FrskB8wSR2APICjAkr%2Fn6VsVqPLjw%2BOK3UGo8HWyQ3%2FTL7%2FpyaUhgCo121T7kn4V0sCiUoce1sxA7IZ%2BFP0W148ksALYT0TZUkZizMJYWPNnUXN1OgeMEo8OeIOUJEC08pyZ4q0BVPxdP9e&X-Amz-Signature=91346ccfc3577e6c51fe4300c96a0bc59de08d71ffb963d96724876e10ab1ced&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
