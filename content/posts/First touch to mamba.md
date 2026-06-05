---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JCP2DKZ%2F20260605%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260605T112434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDx8ses5twXKFBNZETyfJgr%2B58k4wBEBSYExQs9vYx3YAiBHSYIV7cHZdGC4eRn5Bub5cL1lSofHGA%2Fu%2B5tte8IYpSr%2FAwhrEAAaDDYzNzQyMzE4MzgwNSIMiH4ACd6RGQY5lrlTKtwDSGRmEURYTiIgtlPln46678FLhAUxzmQHF4aAc%2FLtxBICxgLIinl6lJla47b0MiIsnl4hDJDMQdaY13k82Nc%2FTbwlckKquTgyyjFBABivbyz2xRhysHV7AxUAFyr0J87NWbAo7uBmWN08pS5ZHTM2yO7w%2BFj7jcjZSweCvwORxAZK%2By9L%2BQcjHwSu9uGjkVye5wOxhhhKeVxiDkCVKUo%2FAfxv00wLBv9eOvcxtUAbU8%2FSLyknogV8fy01tuA4W2hGp4XY3LLfZzlJY3Z3YwkgJZGLsX8W1Hj7zv2vVzTLCcZ2NokbIC%2B5S52U2edPrtbuhzwRphhSyHnAb3rooGlIDO80FRVd70QGBMP3%2BDyLNKX0aeMwuIDUDJJDXdeJNJsuZZmsaONmXTdjJxa5zLNoqNAq0SVERKElCV4%2BiqOcZgo3TrX8qLk%2BSa6wDk1WJ%2Fqer3kGRTQBT6WfbPwuFTMAnf5eSO3yPz8OoTihIuIwDjfCFtrHuehIfnusoSwQQK9VQWPenE9CaL0k8sjh3CErhU9MRUJq%2BGKVSI2mCTJXSTl%2BeM%2BWnJDwAm9c2FLHH5OJOjqZGjZnsy6CxEO%2BwzQdVuwsm%2BXCaH%2B7oBk3U1CJZM6COMcjq6MM7KmyyKAw67yK0QY6pgEvziDu%2FAIJHIeVBrXvI8i9fWKBfeI%2B4yXValR7FC%2FvHmWbdmm%2FDbQwGg3Y67rjQPqdfOEIeEIH3oeN7%2BHX8OWzIgPjpyD5VT2VG2%2Bm0hz4eutJtI3EPKg3ldrFU33r2Cx0o1DzfJr2mVXv09Uk5n3eTftSc50EzB1ujA4pvMTsPU2OC7I9vyRcg4HeFwq79nJwaq0IU7iLPfaSqpkG0gy0a2wLJ1im&X-Amz-Signature=3847aa729adf27548e1818192fe442af978ee634f299529a91416fc17fcba298&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
