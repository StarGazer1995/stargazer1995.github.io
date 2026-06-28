---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH7DJK2S%2F20260628%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260628T205053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCgq8z2hiAzTbo8gxlaV5MeEqEPcrfSmxlQb03aY8K5CAIgQITzL%2BQzbZzcNKTN%2FIoqvYDCEXgU0TjzK1tCujwHF%2BwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJnvFF6ysFDEHjpxqCrcAylE5QnlduYgHNH2I4k00VSy3IF%2Bg4fj4pDGQ7tgp9KwlCNekP7Du%2FpQsA80slfw0a%2BBgG1aI7fnE75o6LnjPHOu6ovSPnAdgFmK%2B%2FwpN8bWDKMA6p7779tQhCmKwVFB0Dimm%2B91fFamFPYZhbnTI9Gx5ja5Bn9QE92p4MQR1%2FLeTO9uTRlrbjqPTVc2ERh9Iopjqu7f0t9pdJ2CyPYbPwTbtv2vRZMDNzX6gCzg48mF7NvNgP0F8FQqT9G3uF%2Flu11YVVOsm08xKKTMJpQe2ZEYsIbd1hi9XJq1OeDDhBOeX%2BUSxs1s95G%2FcrE2AcqpiM6Ub05txBZeiufqBryj9Wu8AHf44P5SM7trh1Bu11ZcNiy4L6vztIWhQK19bgbmSmOAvPiJm4lwH53HSKlWy7wrFbujlyzK6AILPcFs4rRtHNGRzWbIF9WjYDubwhgwq7%2Fs79fHOiJrDi%2Bayg4aL8dqF5OviJl5suWuKpNPnUAiNUztA1bFtzwaph%2BD7y8fOSFwUGA7aFKwSQKiICeQjdlTou1y%2Fd3o7TBdXiK0cWJivPBigV9zrpZWtCfI8cgc0seiTblpTOtTj8IAs0xyn0zKVZyj180tfyItaKYnwNXabkv1RwA4T346IZQCMK2zhdIGOqUBN97QXvChU46y335Y8j1yUh5DWn4yxf9ZM7dGyMavkevzyThH6z8pA9AUYfKwe8y3XhUw8BQ3mWKjnNOnar5nyjOSSLZjzibzTIQ4LQmOwyFhw%2B371QCRdYGLUOIR%2BMc9WEMdp1jQVHsxD6%2FHv9Ix3tSXhxDWf%2B8WqGJuOcMhZinMZD95Jc7JcWyJESclfz2T4QZkaFrmSfgBitJlELFEYWl2KN3x&X-Amz-Signature=b1aebb5c51492584cc09bab4cac0f960ecb12bcf1f640c03ef39a05e5848eb24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
