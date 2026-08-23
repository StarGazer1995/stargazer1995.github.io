---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VF5ETZ5A%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T181232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCID07GMYPCSp%2F%2FCpGu%2Bvp5svbQd0NRjDj2iMDfMiwWkeFAiEAzUH0ifE2BWC%2BolftifKEbr55Zt1CjSphw1kQ7xeqmlwqiAQI2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOdRwTyfVmu2jGE56SrcA6umm53r2ezmIohkZ%2BUvcXbJ2Fqtk7FFj3sBGGgPzPDr5nLY12N1fPmbw9DVhLOrk2eh2YEoZ2DU4wnGn8xVORWxhH1WphxqWwfYEN1JPZNYHzm0moxrQBWO8%2FA3ezxETEvlYH5m3a%2FmZNZp1mazYumITq002SlEu5ZO0Kyk0FREQ6SpGYeEixXB9trudNqm2iSl%2FaSrGHXhsYTKnWyLPZ0trfRW0WmGoAu5EiW42botZIO9YeoQkZQ3Q%2BjFOXqwV%2Btc06n%2BowEcXVzDCtAiKxXeAdMwHV6P75Sj9OOm0NDwMYjuKziWyGLW2ILt1Q0BsN5nk6BsZ%2BV0ok8rFpwX5FQKhfkOiWwAKHYCMi85XMe%2B1IaMxvI5jxUq4cTTzDpP%2BOlzbW6SdhGQzt%2BIFXg4od4vUVfiNthqRVVGq2xH8DflYxzcP%2BstwwJb%2F6ozz9RucB8LeS7mu%2Bs2FAsZSyb7IXXp58i7tXfgmlhl39cBvef%2BRx0eUhDDMxpHCuIas4MiN%2FuxnW6vu9pDkgRebydEnus6tbB5Xb6yFxlb6Km3ibKfJR1soFyZVD0Yu3NeYA9TJeenQ9kw4CUrNDT8GEua1WpyhZA6Fo5TiZZ2BkWU%2FqbRKd8KuhU%2BmY3FWWchMJDqrNQGOqUBSBtu4y9A6HVdrLt7tajyxRD8z2h%2Fiy8OadosvPjRGo9J%2F%2BR60E4Mm6dVtNrSYrOY9UE6LbxQWRZ8LQG9iyXKS8zf%2FmCJHt%2BWZeZSq0rHiL3io3iFMSMHJLYwxOv6rFGLQ3hu4C1QMOezq9THmr1wH1KxcQLz5tfAc1Eo3XuXcCfzTj6t3aiwIoxQYBoJYRmST%2B1eL%2BydSNJW32KGc%2BgyUoeiHTkx&X-Amz-Signature=7aff29b113b39735995987bd3271ecbb6fdbfb29cefe7e2a47658c9598eb23ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
