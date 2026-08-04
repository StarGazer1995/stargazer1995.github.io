---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YVC56O6%2F20260804%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260804T160533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJGMEQCIAw7ZMmzRi5HkpPgUpxqZXyAbfMMp%2F9DwdVT6nA57iu8AiAWehfMKwuG%2BJhadabqDKV%2F0389JWSHty4bugRlq7nWDSr%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMicax4Xj1DGX%2F7BBEKtwDzkQwXVo0ouQsuQ%2BKsWVr5CCIYdFkwNrb8A3vlrYSS52eDsZDLc71nirtlYmJyp9fdB5XC%2F%2F0Q%2FVGJnsRh8sbiTsajvcadKWM1QSotgwbZux17yzm%2Flp%2BSa7JhsrSNj6GAHfLV%2BIKcuhNNpmyq4nW7M%2FoYyE7%2BEhaCTGBiPHvpD0%2FEszUPWizWtrjB%2B4lHx%2BkT4xDiPYepiwFsmx%2FTl8HXanEvX035G4jqPdE4vJ433xMX0r9Yq8kaURUTGvA9EdrWlw5t1ODD3%2B%2FZYa1wE%2Fn3iF72xj5T6I8Aytfg%2FepsjQDBYZP6zp3P8oRV4Ed21psJBBuLowIi6kXvoTxOhwwt6XLiu0PS9i8HnK%2FIghxKgOYXLkxHIqtInL6oruYf1l2ebtN%2BMqYKyc1lZnO5A8dJmUF%2FYrSbGUUFmFnpBS9ISsKQegz7Lnk2jzTOXXr8FOx9m%2BMWbdAiiARARWm7LHyLlRHWLwTaQl9Je0mmAtyhlOeZP%2B6Y8eURlEQmFXHLbFVumUBKmFLOpoBKmistxMlQGeMsx%2F6nSdxqRZ8iGQD9gpwRoSkzeMXSQNYH0EjqLSvIheT4baG9s9uW0RSE69gPza4DXOASae655jZKtkxH6eMRdKNnKqzDLIU0BIwk47I0wY6pgGQBdSHSQsh1CRJV9ytsl8FLyhd8ZJBX28XqHZMAyYY1TqPYFBd%2F8Lr0YGAoRhTS5DHAEgY1Z69G2ov2VieMd7Oxa%2FsxsOO9RWPCkyhJmUUnpDan5AgUF5rjE5uCjyx3UIhpD1L5JYluad24U97ah962gURuC8Z%2FuSmvDJetJd5hxGvoSdTERe0EHsAc3x%2F8RHkrji%2FamxEefxMuhXEEp4221ct3wR0&X-Amz-Signature=1bb99b5098d9651ff1829a3b38b949d14082a881959f7f96941352aa1bf5ec1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
