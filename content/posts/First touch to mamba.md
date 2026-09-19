---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPYAEAXG%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T065425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDQjV2ywfvR0fks%2B0wGts9LDTQkkjfK2aqMA22c8SWGOwIhAJBZgBlGyG6N60f%2Ff7ItjxBD8xNPGwuuJ7ZcfHPi%2B8OVKv8DCFMQABoMNjM3NDIzMTgzODA1Igy8yu7M2ktEsTdYoxMq3ANyd23bs6SHbd6cLdXcAScDSRsMDFig97waNUCHcgFvrZrTl8qqCmeVYPamveybbFxmUZ1kRcAd0Ydm7OuMEYXbfAUGXl5Ev9qzMNjyVMh18d%2BiRj4ulLqtBQ%2F5XpCP890fn73UJCZ6KuXRv2gYDUH5Wda1DlyXRaIHilfwvzuMWvVqUuG18o6Xw0TINYIddydyyv9zspUEI80pLYrWkrk0jdpF9ACTA5BQY%2Fz%2FKeAzr01lgdrBAqnEkUmTX9rmgp3RGJyfFO2oFJ3GzCgzFlu6Np6iUeYL1Nw4qVF7mcgNCyKOwIAGrdjoVA%2FftshK98OXHXH5lAdlAir0C%2FNZHhOmBoMzfaGGz%2F9sL8S6nAtpzKYeIWhqu2bsjU9%2B0j1ldLp%2BFR78Fi2YRLhMnqAFF1cbnC5RSIb5Qnd7rd0zHHciQah9TB2x%2B8%2B%2BCfW7hSC%2FrVT0%2FV6yZy1EkFSyhk8mJ4%2BkmmAb6%2BZMjoPBK33Kv3Gzbivx25PPPLTaQEZDsQDDlfMriObttF9RDDszofz%2BIbQcEP43B3AQ3SgC6Cj8TfIfBtK269P4dJZYrITKycmh3ayY8uZtw7yse6FPZlWQBFGdoGVBtFb%2FniW4d8z%2FepOsriQ1uAF7a26rnck55zC5y7fVBjqkAXQhyoR4GubXEzcXR8GNeAAr%2BKVLrS2VjgMlVWklRR85zWhQU8SRAo3LrgqMLOXRQAggfCF6sZ4BHGP3yDuenwaxV8xyUS4lHu5vZ2dajQglEqDigRmDjITNhAzwMoQ6l%2FxkANvZ%2BrmgY2ZILmg460%2BCQXgyu1XOmBcg833RzotPAe3KTMMueyB6y%2BI2Kw7lNiCRr7rrf2BDOvWDUe5FglLu7PwC&X-Amz-Signature=3d923e477b8125a05617fe1469c76b71754caaf2baff83e48ed81075568910fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
