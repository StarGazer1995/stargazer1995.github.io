---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNJ4B3NC%2F20260909%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260909T015229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFP%2BjqaxSqEWD8cpMmAQXAJSm63T%2BFr9s0no1BuznO4VAiEAy09Re54vvG%2BfX26NZ0CKfQ36maeBZ6HBynKvRlpAHqMq%2FwMIYxAAGgw2Mzc0MjMxODM4MDUiDGHhV47kf2YqaUlnYyrcA3%2F1mmfGfDaiXOO4Tqh73SLht2G8SlqhodHfu1S2A3DtCB7PFl57ryXtp8%2F3twWXAcKvTK3wtQeSOlyqetH77GVK%2B5g%2FbqhARUS9%2FJTXBK1bj3VX3yosaLvwqOPKmHOo0Y9UdaTMm1I2G2C%2BD%2BvqG54V%2FBEejqFb8qRF%2BQvhBOvtjhLgj5RvY0KxOEYF0NPzaLQwBw56Ynmm5v4XafoXEczq4rGxaqFdeE7eaZiMOlG5klbVycb4jG2YK5Gy8wcQsE32NVAJm4fi4ElY8MyFhAAPiBZq0H4Fh0bbxuff6jqZpfX%2F3iaPK6XBGfPFouKKgs%2BtrWfccFwVscGOM2PV4TYOdukKCV1sL%2FW7atvzkI7tU9wbiYsNKDmeEeZiRuTPujnRT8YSivqGgK9UL8AkXVVGSPwGEUuDGJeLK3mUHZgytImTtktcbJL8jz7KBrwb2CiVbe4f%2Bfxq11IOjFL0orUNqZcYi5AS0WnubrGqRej1%2Buyp0Q9OOUISutHrVn7AfoYqOoNDqYCM%2Bw7S%2FaaydUffZ2cuwxPjb924pVD8foT9AtsuueXLT1KJ2LbIoHbc0La4%2BKNJTGGM57e75V4ObiquICNjAkwz0l2tnGMv17JVrznem97lb7yyAnVNMKD2gtUGOqUBWOPu59tWWCVF3Ju1T%2FnKGYmku3XQ1HbsAOmjLTe43qn8v%2FyhQyH3GAnPFhxlI3Wbo5XRoz7l66pm2vceLel1zng2W%2BZqe%2BW%2FDfnbr1scV48a1Yzp1E6Zx3nrIpjQwyIHwqzaGhgNMc%2F%2FDgm47C%2B89HRF1KW0d7BHSEUWr%2BhjrXGHdVofhcn%2BCcCEpBh7XSarX%2BeA0%2BB7r5NGkKBD7IvzLLxxQvKC&X-Amz-Signature=5ecea4b0178b0f7136e0ca5a5e2cbd0335749db52966f889f8d446adaf7ef832&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
