---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HRICQOK%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T162233Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJHMEUCIAW8sWWChLfGfYBNgBuZa7pI7XW2O%2Fp29BDTbr6r6cGeAiEAjei8YJPqjfbHnKFZxVL%2B58wMYYlh68qG6E90YctpYmgqiAQI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO7h%2BLA1ia8sXW%2FEaSrcA0lQ6fpA5abI2DBrZjSeCE8nX1MRuQ0RxF%2FBVXhoMzVbciVXGc8mcQ1XKo%2FNNfimqu3bO0AgF7%2BMcM%2FI3HJVcDkhvzzhqBjf2ztogLUCyE9%2F2iKthhrvjNAQa0q5qnkuOLManLT3RyLMvBAXZxrs0Yw8jNNWPpzLvcdqQQI2j1oCi1MOPx9FC7BNyMTtTmn6aSaIhe8KiilymfVgA3poTzCvb0YKgLs8zAWwWaoGx9DZc6HW6t0%2Bx9y1TrZlWO5vMjGm9V8pRm%2FAENC8JZ2dV0DzXR4BNZzTZfa22XbC7KTW5iXmfFBRkEGSn3Vz4rgBaKRSBj%2F8w7wDKsFfmmHfdrhz9BQAbeA15XJBrbeVMed%2Buu1L49UZJsGhLVO82dise6Zz9pmDdokik7uH2KGqpryrCP4ghpYi52czbzk5ce6NgCQ3X%2B5ZgGqS6FGs1vuE7vGTSIVBkQICRi9g8kb4%2F66EYz6xkoj3PZNBORR6Ia0bRfyH8kM2YBr4MAglMxYKBWMbLsw4oAkzPghelFvjHgleUEBDYB1z5WEXnsCGSjB0PBWkbMOl1WRlLftfIJb0D7WnzAh%2BuEHzMOChGxujxhPNys1l7K7P1Bf8B0dVyu9wEUx1%2BTmfqafu2kr1MKOnsdQGOqUBZlU2%2BGFICbg5DOBghaIxEhqLWqlAC76KngIxushxO6OCHhI9%2FpjpqqS2yZG1LmPg3Kd09KHf%2B%2BhWo%2BzaOexEUwQrT9hSpmgM%2FlZLQTkxS71z0Dy2cpQaj9dqlCUPGi9M0F7EiljkN3lnj8il50sVCJWR3swC3%2B7VvG1uY5o7FYdXyGByOdlsxawf4D0BnvwDmwgRSThzMMi2EnFhM7zZS3LYP0U6&X-Amz-Signature=e22b14ee52b9bf3450452d06532b27c0396b87c0d38023049533167c07e9e42b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
