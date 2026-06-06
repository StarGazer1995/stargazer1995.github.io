---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SCHXDIA%2F20260606%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260606T130450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHNBBAuvXH7EsG%2Bw8YyRE7YKJkx8ku4%2BdBuzXqMUIAg8AiEAyJAjd1s1ucKHR0zWRrFb6ZvBTCiH29wbE3ZbVyoogQAqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDjVgYi6FlkDSmyAmircA%2Bu7lxyKs5AofTLQey%2F7rC5lRcN6uRXRD9J2dWwgBAxffAFLb874WTZdHF1aj62aKxmRyFmzEuFDjoDDIp%2BKL9HHmH7OeMDmaa%2FyW6yLhMW1NWyQ1Emh1CKgxOBiyrDzuTJPvpikIGkqQ%2BwsR03OTjVyn2jKCwa6656yR5%2BnBrJGx6DjEWTgUCERGyOPsrEA%2BNxNY%2Fh6A48BNybHyarYISOWG%2FgmvHK8WJCu%2BXyZZBgc25G8WaBjUmEWbV99uwxgeRrzI0lDtUICpPW4uwC5GzyFNKCsjQ3lcf4bXVa3jnB2DWQHyLK3CPonQz4ah3AaodiuPZTkXaWpQtZyHW1s8NyID5WWyQS8t8%2F3jiVT4mCMUDS28DMacD8aa1uyq9wICQe6Aa17PN5aDdU5VEv4phX3DKM801OVqG16wHeUD8diOJWM7rFXkLiiiC%2BCk2mF7r0Q9hmjabdc6e51R5yU0QbuGWdoMr1YFrgqkOp89nvo7TO5uMRIr6QJVhhIsS8g27lkAePVNYnKWA4nY8iFqCrhTqEo2um8n3ql06u7aGjv%2FY5Q%2FheyfQwY39RjsqEPRu7FnlhgLTgNENLAue7%2FMGFRnrZvMH%2Bwz6mSh5BohcW7qeX00O%2FztBocQ1ZiMKmMkNEGOqUBRsyrInGcjcRIKN%2FX%2F0noXZVEN0xoijQDqLMFAyh2RjhHan%2FvYDZkp4j2SHjljKX8ho0U2d%2Bv5oT5HgwHYpJG7of3C1q39qCsE7Som8GLzuD0USEO6qkfp0Eyky8%2FcDbYX6r5w1ztJYnnXsBfHn2S6vhWGzbXYGnDBV1%2FBc%2Fh4R2qeL3rKFaX9Gx9MFjAZOkcQ27AcbhpsTH22o6UCEG9z6Hpae9w&X-Amz-Signature=2b01794c90cc60f1527654c4708652b61508b7df9a51cb3f2a3beb4a18a6864a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
