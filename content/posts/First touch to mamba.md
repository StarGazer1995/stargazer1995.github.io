---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466377HC2OE%2F20260911%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260911T014653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEaH4HTQJR%2FU09z5I5Qoi7QO%2BXh%2Bi4dCBWylt8eYfY3bAiEA6fQteeLA4K%2FrDueL3s92dA5HfLorPV57zBQMDnjlYDkqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHHe3HaigVs%2BVMyk8ircA9c2MdgSJ6yPq0KfxQOyaNNfTWUTs7UmvF397%2Fl6mhwL%2FbDMzgrfGnoPC6u9dEHdZktXDb9sERE37o68UpcpXRq8ZXeGHw7jLD52wf%2BO5rVkhIsPK7iEmX4kcifEQHuTm4EBPW%2BxkBMhAmArAeC0i6df63QqUTGBtMqyKZivFjmgfB%2BQv61f7HN5SxFifzTK9l4StPDsKo%2BSRGPJy6tnyJUpKEjCafDouu9DRla4RT9th3RidRJ6Xicp8ONtIWI9%2FgwVPiEdym793WM%2FQHi526o9Mzsl1PtHKpTHiresHQQglRvzHdISwIKrbRAuo8YVpG3jCnwNHTkjsKT9oe7cTtEMscDAYj5OSj1juskZiVKZo5F%2Btg4wLjKNAIdljw7PTYqewyNjUeIDRcl1BT9hqgJVRrVDCvHtimdy1JqZsf9j7jnfVt1jvkyzNrtYj%2Fi8v256WU80sfwK6lz%2BTbis6LP6NcUJ855MjqR3oyixW2bAhq9FNt4qujZ2AwGaleWigZO7BDJxL5B6%2FjqS7Prv6%2BqDc2eOrlpdSJheyNdng5mlKRqljZyMQvPrW2O6w45xgUroiZ3egPgVVVEOI%2BRwdofEhdmbE9ts7rl1hjglxyeHEtYfNl1R2kQkkIrYMPLwjNUGOqUB2dyLF1czwBYbUm5HkMYD78jmdyQcxFKYmJj3lt5WgyqXBLqdZ%2FDzuHDF1zeiQewRWJwA5uSg0BqpnWsANcnTPpe1xM4UhDMltrxwGO5UXloB9HovgiESq8tuXCxXNj5w66hS2aXID2Aou6b1CJ%2F0wgdgyCuNGQItKlJ7eAyU53bSc8kYN5ZpBWcUKU%2B5yt7e%2FkybC9nz%2FWo4d8uKh%2Fp%2BHwyuIG7H&X-Amz-Signature=86eaf816e9faa7e4cfd08ff51539d3e28868926010453c526f0a82f543af086c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
