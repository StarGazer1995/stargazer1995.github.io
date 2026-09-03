---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUFFL7DJ%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T014808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIB1msskxzF3ENbEMHQIlrRs2JKG2WlUmn5GuXyg%2F%2FfE8AiAyIatCITBBqr3MWyy1MYfA%2B%2BEa%2BuO7WEgc15gzhik7ByqIBAjQ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPnWv8EQzi4aK3%2FPlKtwDhmmenYtuldY0ZtsuCBmfCDn7tufpRSScBG%2BoOk2sHyteiA56mBtPHMH68xM2MAYS1r5JT4Ose5OSOLNBpptb0KOZzTRnosQ8VPWLlp1%2FPqWmHSa9Ca0PId%2BBwl0QIkflOenO6kdOpyVWeYEa6H1sDWZu34qDVLy9VNk3R6fAWqqFRF9oDoMa5ulrXaCQY9Xd0UbN21xDcNZ456by4wylrKzxFQgfGFqafi74vxqLz3%2FY7nXmiNvXHcaTtEV7hPuHPBLK74QRnujvn00GvYeznc4%2Fv2yydkOnme7uacAqzrKwF8JnbeVWVULJWPHTVQml9r3d0%2BweAZTGDDOh6GtJCmqMTh1T9fqWUayGfq2llRB%2FjgZ01bMM5Txv0NfFyKoiqGpvmkPtJaDM8ckdKV58mA3fUncQxASXyUdiAEQnpeObgh0A6mj4cnl%2FG1kCl%2BLKUude6Fh%2BXiWuvMkd3gMK71UlhIs%2BKESXozkbv7JXKgA8Y%2BALTneqsOkG3VHXs4UQ2ZNSd%2BlWJjMqlWE5GGBMFDf1XFsWJJYBczOlTbD7ZzaxAbsg4FK18UKazXkTVfMHLRmiogqzf9tLmyZEDZDJOGI3bYgXeiosJnIA2Bd0P3xJh6n6BgDY0aJ6zoAw4cji1AY6pgGGxgy3So17ApibdL5U2I3M%2BCXxt4FnnTWaklmhqvBlnClS5F45kqtm%2B6w%2BeJxoJLrNw0%2BJomryCCowQSfuHFrSv7rJbAD6LNhz7ElKzcW4rXKHJ3%2FtRjp1Sz0%2F5E6m6%2B1lt1%2FrPKYE%2Fqag3Py%2BAJk7MJuhqaxN9kfENzgSLpZE%2FuAUQfpONp3NMw5rHcx7ELqne0Ut8TyBDzVVsNDtoUHcUj3Mf%2FP%2F&X-Amz-Signature=aa768ae06846694676ace23cfccf394d660f49ca4fc9c0cdfe4b3aeff9f00e3a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
