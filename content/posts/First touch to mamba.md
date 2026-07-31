---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWJMJMNI%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T205200Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDPonORa6s7TZ%2FFXcAJB6jqXDe%2FR0yRESuXsuS3cFhuyAiEA3gO0NcR1rr33wnPefHzIRJDHU%2FE18tVbz2LRR%2BoOEogqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC7oeedeOujWeR1JMSrcAyIBQs2UO4cJ2XYH9pTrfbsAFhSBUtcOZmJzhMCkxmQ4rMKmTSxTen1htI9Np8YBYfdYnbnrrE9tT9dwx4XnbLBDATmvNPdYMzRw8zkBelNdc2TFV2k9rLZWj%2Fpus0pHg4Xx2r4irCHZuqz6psxz0hva6JM661DSQk3Yk8JHwelDH1CYVYYpIi1%2BI7KR1cbXGIh5W0NgAdy%2B8mASt%2B%2BnDkgh5fMA9ScmPDCDn9aIMnsiGteypW7sSHDzHOJqB9VsIRQ9os%2FDIkTFyVJFR13roRFFiZDS%2Fbfr8VbeKrPdC6QM75e50%2FMdFs4Rl9grdbJqTHf5fVKP9bjq5Dp8N3oxOkHznaiAnNyx%2B1bnErunc4EcSW58qtOARTkGnapG%2BIHxEB%2Bcbbg8qNYL1BnY2TCwXStIvBav6x2E4TEBzjOCW8bfWz%2F7r7xtqxPCrDDPx26br8%2FuGmczllK6QtHkzw71vzGd%2F%2F0WD9q0916X8ckCPzbKJWdmTyg58eXUzpps5jv7gkPzQuwU3rHNW83qbzn4lyPsVyCEQjfjlI%2BUseRsszNH%2B3FXh4gq3hlQrOGclNLljgViOEoTgkv31lkIDjcCJ6leJNuT4v5omR%2FYDS9Ap8E%2BbbsR1EKsS%2BnGM%2BOVMMSZs9MGOqUB7OF1a5lI9SvLILH0qRFctTjZzFlEO6%2Fkzad5UYTGSozO7jZHUFJDjGnHy04aAb74i2jI2zYMrD4B8D4GPqFmtvaV6DPnrS9OR4dU7BFnQ%2BgbLOSUttbIsWWSFDsXBfhDWEA%2Fz%2B751k768cuBIpqLof7EtLv9BN3NVGdgZMqArlN7DeNaBOp%2FJZlo2sPdOBZh37nvBnvEPqcc12jUe9l1t2xaSFBY&X-Amz-Signature=616df7ae1decc2900d3fbf28d7a6bbe9472313ec3fd127d1e083d4fc87aa8027&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
