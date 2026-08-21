---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2FYSNFP%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T101857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCcvWKpmb8Q4XrNSPYCqj6wM3TWpNFDboV3R%2FXh2yu8AiAij0Us1vhc%2F8DdxQ6HHscEpLO%2FyuC9OWpgnI15uHiBFSqIBAii%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FIEhoB1TfqRmhCSIKtwDiomu7%2B8LcIHBYyy1Q6dM8RAT7xSSIQdiXhEJh7NpdnLulDk2ABJXxiWk8zudPWDoQxzS1k6VLfituMsTseViXH6dlRUwLItDjRASay5IF7Eix6kk2Rni83CLzv6SZ06NcQtQ3pc%2BacOvqzPYARowboRDcla4vYzZPi63%2BpLeMFZv6clKdKf7NUn5h1bU7vc3mpthLEWvo5zVnBiq9eusojSwYlRMuWZCoNqMjKQVJLCwgqqOT6kHczYlsNHXu6%2BfpIf2FQr1vuTKIyQc960Qk9lVADdQIium%2F31v9KT0GZhzLS1dhEHb9d8SXovlgxwG3GOj%2Fsj1dsECQJlKvGOwmJ8p%2BF014SxiF%2FgyavuCZzzEysDHj79VHjUlH1hDt%2BxRrHDIFwmSQTIkuWhg8YfdYIBIF25csvxYOOkpnZv67zDDdbwe1m6i37dHFA8nxzRtblGo3QyAdANvUr0mkR6Q%2Fa3x%2B3pxxy%2BKpDb4NsJPp2PtmVuBZYukQLDRSHKPgKCzxcVOacQt8%2B0siBI4oU%2BLnAtXeZkfUtnAJ5nVS7n51MLSHxt7ZYskf%2BI2ZgmFTV8jxeqZNPE73%2BPnhQA%2F3s4CZn2BXFvJgeLyrBQ3fl0ki8BNHaxC9SzgEJQxqa8wmKOg1AY6pgHB4Aq%2FMnKkmAdaNHIk3Zk4RHeFmyU9mmz9i95fbGQH2V9t1ydm4GXELDOeRwrtWi9vlOJRhXeuRGjaGezYEz%2FbE4HbtUekEOZUWmvQOuEWwWW2aqxFZZQISAyrXb8hvGo74%2F2v4aBHwQ8kcsKLqUvuyN3NV19wsF0O9rxycWBLN0mVyioDTESe%2Fxe%2F2x3H4hrkZYOwpzl16DhAb8Ae8ITBqSDRhVhr&X-Amz-Signature=426c0b3c5a7c29dbdafda44bc5d77225df24bc06c12738be8b4f4c66b9fa9dcf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
