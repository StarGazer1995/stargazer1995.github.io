---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGZLSW4D%2F20260925%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260925T021210Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIGoCLMjTzrt8uMr24xIjmf609nsF3dIcaCl749y9DrySAiBRV6jb%2BXL5liQeOhUUE759l6cQXQSi8pBLYmdfg62%2BlCqIBAji%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5aOUOwoowYWaLpIcKtwDF5NQjKZF3pgR0bl9OenOeJdXxHtL%2F09ySl50T18HCb83ssk%2B48ERbPnAp5ac%2B3wqw7tWmqU6lDs2vCX4tZvfRYNlYdjj6juqLWZKRqIWbTsT2R7YzAdvsIaIQ%2B5dGLgjLZ78sqEALo6cMFHX19AI714iNknUFuybEWe5wHGQFvYE7MbVOhrSuL%2FddE3Hz1q%2BFkxWC7hD4GZz1vL6ugn7F4I3s62NG6bR2196J%2B3McKzTZqH9lMFvfdE2phJKSLYlkSDmo7jN2EL6gKpmpJAZhO07azZlFIgfhM%2Bx5az9E5KODD9%2BV28zEQ9GjxO2E88%2B0%2BzRmgJTkoDfbi9X0cIAJs%2FmV%2FBK11vJ3DEWTZQOlxoirqHJwzM5N7DicPfqAg8OfKgoNB2qEqIj2adDV6%2F0CXfm4YXWYlopPwRTlqe4FKKMD5zyAvMZksk%2B%2F9N912dN9G6Sys7xU%2F4INtXtOymg%2Fb9hlpo8LOfiARp1ctTt07lJmbDLm1WslZEAng8CH3cpweVsEEYFobtNVVhG6scSMd6THkrYZ1M7Sj%2B5CQ9OHJfqEzRrq0PyLWyvdQ0OERdYdyfoRKYky8j2WpNReKJQKG158CIpmZfcBPnvXShCZrhPrw3NmPT3rxWzBjIww5jX1QY6pgFN%2BxikCDr5xoDicAMqPcvw17dNkIS%2FDovLdcqCeDTeTmV6vboN3iBE%2BMFUlPWiGAtveyFKmr53547596jfIcJ%2FcEK7SjcnZyqVo0yrGG3xC2FvI9UTtmQ27FIphUgLqf8W8l7AFEbEoyksHZuPQ8Pfy9JtzHvEKBKRp4skqZXAJVhucpHJgmz9DXhwMYN%2FkqVNkDLhJqUr8x8tAtLHqoY2W4Ks5mVi&X-Amz-Signature=686d6a1b364ba79a7e26f7779d2697cadb1af6409c60b580214b667c4cb1ef49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
