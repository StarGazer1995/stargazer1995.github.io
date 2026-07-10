---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XL5TMJT3%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T205910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBTEUQpTkMcJZhIGjAB6cE%2BTnQjQPg3kg9j2NI4glm5wIgDCJ4rVxDSy%2BUXwEQ%2FDu0vE7KmbOXMSVCP91AVpYTC%2BMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGd0kyemnVxtPA4CKSrcA8Wm51aupyoXLTlw7579MwMRmu1IHG3RbkISpvq53Y0rXv978qihO%2BZz3ATag8XPB2M5h7H7gxkKqmRzERaCnBi%2F4ouE4vbulpQsLvwHuA%2BR3souVVrSRAudJ%2FLGz7Uh0ZVlYuf9uWsaB9FKNUZfIoVaNmt%2FsZ2m39ghxxwygD0vPpDceaFIARVQFguFm%2FnfhOKrkwkOQ%2FaR6Zz1wO%2F%2FWEeR9tYqio6NmOC3Gu5%2BmSlFII0IgqpxldcCLS%2BUZ24TCENvzzTq3LIon1W05CokzVxj0u9JLzbipQuAYqfE60P%2F%2FB3y42p1BNMJk3ZOOKL7csu%2FSFMRzQely7EQMzwDdNTmAu0ZdrepSRNnELonL6itfhEk2cu%2BbhtlMBf0kc7DJdbfub2z6P3WSUL716f1G7slwgSX7EfVBpku5rm4v7MhXbUZpRRUvsmQALKH81TE%2FG8qIhpDi8IztlLJyPzlKBRtn0u9jg%2B1f2yeWjTT2G%2FSN1DUIa0IC7nqWKmJ7prRSf7YyMGFHvBRFGxpkhvCMbzUefA8f9z7SZEoAgLjBvZQbre6RCSvl9uQ54b%2Buu7BFkiA2Oj%2BT9%2FNelFrqmxB75ro%2FmwANABuaeDnrT%2F6DDB7Ndl6DXEKjMx8vP8MMMaVxdIGOqUBZWP4aHm%2FmMp7N6SHOV%2BHxqTbcvcdPgrna3Tp4bRCWNMK4o47ZGKjCd8kj%2Fp9KFuPXrf4DRH7gXKPvogR6m%2FGWTJlDxq47eg2%2FpsrjTEHGkI546pFPjeVEUPYLThyzdLoxCBIWZEf4CFpWpK4A%2FOrjhvb1Y%2BCHWvGrupglDhoYFUZ%2BuJkIek%2BThWxjKmBeB%2BK2F4oV8R4yBmEoY%2F2te5vxC0NVVes&X-Amz-Signature=8122540cd6f1940fa1ae594bd37a71c073afc196b20619bf5b171ebb23f4d8a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
