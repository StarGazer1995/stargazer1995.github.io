---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4UYL2JZ%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T210108Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJIMEYCIQCd8trsiOcM%2FcKy4XVoW4D7%2B95PFBKucN6pqGD28mOwYAIhANL5Vf%2Bg6zGGFE2wupfixRrap2h8Sx%2BZhqjGZLigU4SbKv8DCBUQABoMNjM3NDIzMTgzODA1Igz3qt3LM3DqEAZA6AMq3ANVxTzgCZ7GADgpnzs6VQM7MyP6TO0lAsAA2MGzHX5FOiOGBjUwcAZLh1k0uAQkSLLnCc19h1UsvZSi4gGckqd0GrArfHuEycdY6ugUmIjCPLFQk2aeBGicjjEP7D5Wn4jYVNJKPxmJxiIPBImUsL92kCBmQCbo51QfFhuooxT7kfQ7G3spBr5QP6MS39KdqdrErXjaxc%2BAaNSlu6qEU0WI6o86x3MCWpA73XLDRza4hwwtxzTpBNfvB8UDFOQK3BEzHfLU0kEYI%2FGhUBNwlNnhOhGkVsKWZsB3po1QIp3rcw2%2Bd3PhaPhiBGEslEcnVpZTdGMVm%2BdiSzmuBGuKzce5Sb1MSfMX9oANjYP3qyikWONyeb1xp7RvgBfovUeQYzKlK6oVSUsj9gA2Qq5uwhCsLySft291V6qra3tpyJraH3aEabKtqjvLJGO8Dl12f2i5HIIlmZ%2BHRp3%2F1BQ6CEr0jtqon%2BLK4BwMrsyvcI2z2j3UMGw%2FKDTTcMr1EmcLtIOr%2BbzeLYqfT%2BDJ0Et%2Fzq0MgwS0Uw63M00Xse2j3%2BoArOIVDCWRr081pbeZ1yczEWHCngL1xJmqV58ky0To%2FYEgLspJK0fDbaY%2BRVSb6zLc1hM9C9WoO7L0MY2a8jCBkMnTBjqkAVGfF9a0GUkQbShOuXjHiZykRRojqADQ%2B2I3tR34cfEveX0hYYspYJMXXcvQI2Tq03mk9BogKfEHQUlDyBPhRFk4gXEaevn6bOyLwHGX3rfa4aWL5mWAvGnnyzXL4SAnUhUO3JFgArpyuSt2vLPEtJVoiQoGLTeqLLo9UtGH2weQmcRI9ojz%2FaggYxrr6y%2BxibysqqMDKByuZfR1RLKDONVBV8%2Bw&X-Amz-Signature=36fd745e630e03294084adb30a844010f109889570368dbd985be43cd9d83877&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
