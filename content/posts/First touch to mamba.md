---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MCFE2R5%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T052301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID4Iz6JiILZhaZLPL85KrzXcrxJGT55Uxj6VARmjlTbxAiEA7o4kNElsL%2F81QZC4hfBCtaE74zVYoagpnim7bmgYx9sqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGw%2FGXjseq0lBID2uCrcAzVSOJcETxxL4VFJ7ejYLGa4OfLT0K08wwig0FhXogmoTlA8jTAqfG6jPDYACryOmse9Mnu%2BrqHrKY%2BrpwsyQf2FnTB1mVjFYvkDhOwF7zU9hyFg9CcLh5jY1i%2FfBH2dSLWQAOT2cXWRt0MN6zbsI4XHUSZ%2BEOArJilDVF9THpNrqEqLf%2BylP0BGjXoIiBTNB59Ou0v8LUbRti7dVFxwF%2BoZrQlWyuCnIE7vpUG4PrVlk06HIVOJtHgqWOm0Pd8jF5GkOtYtDv7ZuKeaHs8IJqveUk4TYT1zYEeAU4mckHNeIfMjNJiDSBTDvRfjnr%2B3s45gUwkg07SGJqrEMj0mcSAA48K6Cl8ncJXTnR9pILxauakkLrvHfLtKRuiTVXiMR3EMZNP4%2BSuMfsLXnjIPtUlcyE5gptBq3wOpUfUlJ1TYUJeAgwxr3YTpdWHd7imfevvQx9mCz0InfsZKi1ZiQgptabQUxgPsG1d834c2ydRAzJJe2%2F2mEow1yxKNQvpwE8OTODDFsFTFmMYs8mQlRSim96qEDR9BoyAJPgThXZMFIgOb3dkrre%2BDirTeYF0E7JmPJ%2FNxzy7djaGQ9lyPFOADnCGUDmZRglQNPTf8P42L4h%2Bdquxup41xW8DNMPvc79MGOqUBCn3qE%2FiziFK%2B%2BQO0RemJD%2F1XYJLKdij0svgAyXyXtQfsQLXQ0YDS5RvixW31AV6aj8YQrMjZuVVrHV%2FKo6qPhwmQ%2Bdh%2F%2Fal1Ps0caA6Tw0JLpODdGwSHNoI0VMrZMyPKzFG3iYIijIfteqJTq4e3B3fkqSNSORZcz1hWqqKDhgJEhuxMTjHT7ZiNme%2FBxIQWe%2BHgvwjKzrgskwOkeWoCU%2Bvfot6i&X-Amz-Signature=79b80dbae9f4ebd40b93e45ef4c47fbd1d79d8e86f9c97551f7a5e2acdedb3f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
