---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXPBIQTR%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T230925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCBHMyNM786R%2FDxyEhH3LTmAHdE4eSCxolJURakyldmcwIgM6%2Fznl3PeJXkqrrczxxz943NUDdCBLDX5Yp%2BElXqSJIqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC13iWgdha5iwaFR0SrcA%2Be8V%2BHXdkxWlLrf0x4jZ3xXe78wm%2F1J5SgMfub3ibD3MSeNNkd2FaiUVkDHJOnxrOhh25xJ3W3%2B5AASYu0YD9PWuP97%2FK11Rq%2BB9tgMuVqe3xfg9XNIAnI9jYsp5tAWKyeR4rXFoA9vNTQKIae2e9ItNdgkhJOPBwnoF3BiCcbjcSDW%2FsawOGSGJkniwXJXCOkiKo320nkmaFNIP2477f3y1JW9KF099gy5I6LvkjP%2BwBarIj8k8pdeb4oHJxjzoDXSNGiDY69Jh6rKcpuY86Wo0eBTegpz8gIN3YSLwJ88NUNU2fghSv7u54R0rsbQROxbcHFEwOd3%2BnEPNomXyjMqqZxc%2FTsmpRom6Zs6NXrjKgPEOR8Yv0NUz29XvI%2FH9DVcJegNgcBNUIWw6Y8PqyA19fGFtSK38b%2FPZQ8Vc4V6BBzETOnEmO1zs0AbhTtd3Ob8q9kzVy%2F%2F2sHAc9MdarulGErx8xFLoIbS3Lv0sguhUe6X2WVINrlq5Jw7v83G5jp3083B6EYMcsbXDut8MozkP8pfV4ArsL8iSwMdvNr2qIufOmlfaZ50%2BBuu%2FgEaE%2B6XW0JaSTYBNB94mLbc9olTV60SYYkQC5%2BFp3ywUql6O4fchdGvQCP8QFm2MMqfotEGOqUBSww1lnB4RbbrusTVKJXBFe6TD%2Fu5fEB6RWVlZ%2FzIKuUGJEfpXr0mo35H%2Fvc5K9S8dJestrQkxroLRnNhuMAtcQKzaIzBZMzaLHMC1vhepeDPJ3USeOnpoo9oi5qFkyLz5ANTvhXQHB0LLG0zbzKdUjSs9IB11NV0KbnfYZ5hJbGNEAghSqtRp61FmPgBFNOIpG7Y1uJN5CjOC8shfpV0ls1jxT1e&X-Amz-Signature=03bf6c93d6a3afb1e1fb1619797be2096c7c1e45e2466852a89d3230ec48aacf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
