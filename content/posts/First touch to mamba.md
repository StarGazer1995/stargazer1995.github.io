---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2JNQJ5E%2F20260525%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260525T125637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4c6wh43VLQaMRdyOKRnj1GHO0bNdWK8Pq%2F%2BdcXJMpkwIhAPvuKR9GVys9THqh%2BSh5LxM4V3Dz7gzTOgy36yF%2BdK1yKv8DCGIQABoMNjM3NDIzMTgzODA1Igx7bnEfjKQmeq82insq3AN2Kq0goCtenAVa2lAy3YrK84TzxBnPSUA%2BEVu36IspugTc48i56rKCxpuCQTk2FeF7T0zM0%2BSK6EW8hpUkK%2FI91UHjjj5MKzhZ0lkVfYMW0y5LqRL2lv0qLB1Ygke5GCCyjIUalUwhdwXu55eoIJT3T1v1Kgz%2Bk3WYSiNffA%2Bk%2FjCOPlDYMGu32JQ7CLucg6F%2B4NWsHgOZQizeCkZoBFPtFw%2F%2Bq6SRxMs7BuAwuUd%2FXcO8ieH%2FP725BdOnDJvPrRrt9nlmGHGawAmqBEzz%2BRc7E%2FX2OLjsHkCCTR%2BYesooK3t1MaOyZErpkxQMFamrmk%2BnOxNCd1a3znCVqe37wygNegj0Fq6M0l5krC8v14rEpZ9jwSyGS23faJjER1g0dpjkuwBR7BwakxNsck6sCZW0I1eTlJ9DUSxsKi1LmWQ1QpsYBEJLu59CKRXo4eKHs22T7pl3lhigh4AELM0XU16rDgl9xYanLUju%2BOVNR%2BCAPdqEdbaLFAhY9Z74MNGbWzeW5%2FElBF17IGepP7viBCpRg3bTg74pn6JEQ0GQHwPzxSjL354CRMNFhA%2FadozMzNZXaQI2%2BpWS5hKUSTX5O9GvXktxOp9q3Vg7hCY4TwlpgsxsvlFSU%2Fk9d2kLBjCUj9DQBjqkAUL%2By8y8d1Wabcjrsv%2FFi8I78zs7SkCWH%2Fx%2B9rdBVO7KFrsXN8dyqUQ4CwGJoAPklfNj8Bh4pf1yEQsdxegu2UeMWojo0TxqfInc0R%2FeYOA2dpuK8qBhmWrxsc7eeBQ4cUi9ty4NKtKpJymiBF%2FN%2Btc21VitCRkkr572FYNAnnPkrPUs1cAF5fQ1171YmUOdWa5lXWk8WEFAf0%2BWf63BUOouvAF%2B&X-Amz-Signature=30d3f72bb66527290e4c4ecf465d6e658b968f06e7acf10d59feab9dfbca4aa3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
