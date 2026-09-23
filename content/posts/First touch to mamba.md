---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XXCGLFCW%2F20260923%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260923T085423Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCw5IAocq7Eh%2BaMnnhTaFyKOAE4lZzjYA6feGdY32x9CgIgARqPIpY1QEOhMhELaSkvhy%2Be10u98R6rt%2FvtrgOhX%2BoqiAQIuv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKnib1oQdnNmAPghRCrcA2YPBxdnOj1GpoWdSIefWlU7q%2BMTE5XfFI0rcqTq2CzHTtrzIm1xLnvMlaSfI1Fqaih5xKDnXoiB4Ezz9SQ1sBxtDyUET%2B5YIMPJuCDz4HAzEVez3Y3fj%2FuvTigw%2FEaR8FkktfmUj0iVF4KMsxzrWHMJC41%2FFn6LmsSdbjXcIrppU88pgUAqeR7EK2tsJbD25%2Bz0lgqYXZAo8EY9FNpYMq8%2Bf3ovXfrX5998OUGYSrfoHJhORpgEOulNfwqR3af%2BhqrtdmX3DDiAfTWOhko%2FwuIEFAlzutKRW3djKSiyua%2Bo3eFoLb6twrAC1ztANNQdBEPYEEL5gvNtIQLMil4Svrit%2BIYZYw2WjHv1R88Ec4Gjku%2FaIWoaZci4ze98nYQSlwdcuwV1wVpbHmfYjWKa6Cs0JeSOFEB%2BWQNn0vZkzmkw7RELe%2BiQCSd%2F2QfdZfsU%2F3BVAbieqcahUdDEOmwqeqZhLOXE9sdNCQiaY%2BDJsI%2FM5m1deSbz69pp%2FhVWtGsZnWpR9jiWQTyhoHXRBXBLGQ7klsGYpFwDJDFpBjDVgxFBJT5HmBNhl%2FHaXYseY%2BNY7CCJ1pN8xHCZHTqdMhxb8rguWPV2TTJBTAgblC1GkbuTosfY%2FwQ9Iow4CZxPMNCaztUGOqUB767LxyGYUOuaD0FGeH7y9R%2FjkewGYHEUE1Xbe9%2BM17ZVgbf2YWWa95mQdTtIQOlfOb3jJ723VLMjL5dMlOKF6LpTSy7uFpL0YYGSskkmxtxiaKB%2Bm3jkSZhfGiadcNF0529VaekEOa%2Fs4s8hR%2FCyeAriRyYqyN9z%2B5g9rmE8mutYbOgJzUN1u8K1k9kMy2xxe3SVl42HlibeZnGPYYtH%2F3TONRDv&X-Amz-Signature=cae4cb97cde38928cfeb0cb03a1aad69d482328f85632f8b470c9da01fc422c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
