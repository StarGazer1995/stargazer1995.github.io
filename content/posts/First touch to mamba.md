---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWUVVWUF%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T080000Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIHQ6ZgFia%2FlAVsZkJojHfLcUlak3isHp6rn5CuqMNzGRAiBGQXjnUAdpskMB2BAnDS%2F6keirAvBRkwJn6HTvvGLZmSqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMagXafPeg0k7HW4pJKtwDZwtJBXhOTRw7VxDopgvG664WgjWuj1FBKFVSzf0NM5j6KvLdFDL5Ri4h1eWRScY1iSjtru1hsPNgEjjut3VbBIrrgLfyjYrPXPLD12BMo37H6dxX%2FL8U%2FjZN0Y7SP6xSHGOzOv0SFaH20ioYKXxrl%2FeMSuWa0q3wbacPOrY%2BHi3zYn4t69ymTkSHHLkcw5%2Bc2cpfKJtbUARzaYVbgJpGUoWzFJnvk8%2BTwhzg%2BQNEeQbovXeFnFEFpyXcz3NpWhOGOfVN3pSfg2g15j7kdhBNeHk8PlcQdVp%2B15hi6JOw%2F%2FmEr8pydiMhsyIhBe8hahA%2BUa5pn5moh787XYAcDCilYjwbooIGPkJymUhH04ePAhdMF5KRAhE9uKqfg0vYDp%2B%2FkA09S%2BKyvu2Rfo8T%2FsAD8mY74qWOQF5DpqNA8IWvoJ2oVgSLcWVlVTNgT1qc4oBLtcg%2FvPM7kED1hu9CtZqaXhKjiqc8R9gmgiUFyGb47n0Vo1WYMTUhItER3ExxcvcFD3AdGZcz0BppcGxF5wIfXRJmuu9Rygkw%2FmAe9KoqjwTbevEsqRi5Q%2FUW0ivIInAFj8S8deaiaMJU%2BwtXQXqwTGHHnASZVop6v5s6YXeFqVDsCiPpGsxKeUu6tXYw46mk0QY6pgGhZ6tUdr2DgwR1MyLssabAWUyfZGa5ubKAFhhbDNciwCAw03Do3pSFbs0Ifh4TPE12beRx2yZmcFLdweY1dDQtAfsdDw3A5FWUrPmp7inSBrIQ5%2B4rsLH3CHURocqkyh0LMF8cXiUF6uZDrv4iWJyI3BEMW54Gj4QgpstSvVo8V2XBmmivUT5PG3XfbOusOvQs8AWzyWFHNXdrnAmQyzufkpAsO0wf&X-Amz-Signature=b52a74906288ddb3a34716e0d7ea36ceafacb6a4feeb52ef6ffe98e93191e154&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
