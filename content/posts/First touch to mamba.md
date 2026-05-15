---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TFIRZEVB%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T204938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFxXymkWeqFU0l7Shl8ifZ%2FNtTctRj3SiMBci6ZgsijZAiB9PnK2yGDHkauaAP9ZErjlzh%2BGglQX37Cw1PssaaWzcCr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIM6ByOvRDZUtilTL28KtwDc77YgbLj4sEraLM97m5dDgL7PlKWn0YccNawh7wLs08eDmvvin1KAh4nfcjw%2BLTi8utA1DkxYO1uLKRKmvCuJaMb5jh2xRC8vC6l3bD63ZrNQ8Kvj2zNHEjDTa8OQ4X94iCFauK01%2BMljS3cpNYerJ99kK0JAVI7S4cVePuNBJ5eK7XLXvAWqKKPjSEBmCWZ14CLN0WjcR%2FlN9yhfzV6m7cVpgcLHZL6vWlFPolCG1fq%2BMEw0Gm65kSaecmrvEaUyWJAUeEC%2B0%2BREDuobDnGlHz3EjlJtEzbsOfJv2pBbtSZXwQf2PLuACGQ%2FnHpjmaUGtiENc7bWqVMF5gQhACCRMK6ageJ4eNdmTtEwRVVOzEm06NjeGyak9PACe7ERUQB4bJghBsyN7S4ywBbJAKJ5ZJmivK2n2%2BHERU3Aw8uuwpKygflPI9AL9acEvbN7lEPd9hfWI%2FVkFkdV4IhiswHl56BbW359fhCsBC5rlCMQs7XCVR7mrc0Ebc1zDb%2FEmqwSJtPmRWR2fU5t7UFIVoN1%2F%2B6f3C1ItLxobaIkYRCzthovIXfE7ouMQduJAZ2JYi5PeIqapsuWhkBUYgR0UpkVSo9TOdg2rotCgzOvToZL49frQAF4td27Y5UjRgwzfGd0AY6pgEkv1H0QRETd3uEeqAvdi3ktk2puQk64BRyOdioJ7XXZ3XwYDOuN0d7vjzZnCv7CjpExNyx5aIpJRz1T1cdM8X4tHJuWMZP3H03Kiod1acF2kKKsayONQ3gEe0FxQmeoeKhKmtY%2B5HlJGJFOdYku%2BUi52nGEFhpmsXce5Br%2BhH%2BRVV52ABFRbJR7s63WpiY3HEzcjVszpbGjzCEnectPPj0ydmTt9bs&X-Amz-Signature=2d53adda8edeecc027af999f7d70b4c3192c6ea24f436d87720a60358eb0e960&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
