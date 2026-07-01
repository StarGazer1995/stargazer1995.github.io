---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAS3YKD5%2F20260701%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260701T192808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDcXunGbjHdVAo1idqte0VXwfZq368ucs8C57cWe1dz5wIhANzf6v%2BtUOGNBe3qgV74hETk1A9LC7e%2FU04ZfmpmXuYaKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwsWc0IX0FXGXp4%2BP4q3APjkxzASZJTnhW0m7AY4SU4NIuFEQedgsaGAn024BODdm25faCxRUbaKKorDU9utUtnZUT9o%2BwHjqpNLsIlTnDZ3r6%2Bp5IUSECkLchhroGTx2xdFy1ducmxItWQtCXgnS9KLkjbw7tp07uSsa63tRdnQ7wjcbrTOC260Si3ssrM632iRJXcB2Rz1lI4BhmdXWUA%2FpwVBdH6vI4JMHQfcqVDS6kSB38n84%2B3S%2BpyzpXvPpxM2upYxQbLYRUWp1e4QnQ6sw9WX2q9ISRpEb%2BNTX7AZlxqJSpp1kbmFPs1obLfnAgrmNfw6t%2BjOm4DgC0PuKQ2StmJ1z5KSElKHMruxlUaB46YJHQHSzTzm8HmggIOmBM8RnbPuj9NZu6N85uJ2bKaV1XBG0HeUtQ3YfNHAxUbklYoTXPz33o%2BGYAUFkC9fZSwxMkd7jSfh2yC4rN8E2YTjimOi33CqE4yRRJ1FJ8cGo%2FlWr1U6UPqkN3N341C95MKWrcyMWKVyoTN%2Bhkur8eleUlN2gn4alHdxlr1LNBrnP7dHDGAcnWRfy76y41Z2zsBGZNpw06jvu9JXRBT6YgxNYPPHX%2FySM5MijSw5haCkjaBy8yXMwDnH%2Ben0AfquylUBZVUVifuhejwQzDUvZTSBjqkAbr698Rz63wpz82LoIDSjrsXDbBpFw9F0mddrpUridSmMh95M7SZMIZ58EJWpdMZD2y3HcY%2Fl0iCHM2%2BYBXOwDMDJLHO9OsWbhD8%2BUaSyyGvr8uNLKSmh2EbwFsXUdCXoaUZNVEarJvVk5XHEFh2WH7r3xI90kIOqbD0AnKTa7hfi%2FavURV1s%2FIzj2ads4iLDJOTwB2PR3WuiZAC1g%2BrrQo%2BUNm%2B&X-Amz-Signature=3a9ba7ee307f96c9cafea21969b5b856f87eabff7105bb3ad66f8806453f687b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
