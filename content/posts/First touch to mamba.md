---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YD7CZ74K%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T142109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHIaCXVzLXdlc3QtMiJHMEUCIQD47iiLKUnKN%2Bv1Hz4u5SIzFv5UxWs8euUkBduoshvTAgIgAqEbRCHLN%2BZqwzdBdKFVf6ei8g20BB8yp2GhNhwEKI8q%2FwMIOxAAGgw2Mzc0MjMxODM4MDUiDHD8n7aa%2BzTilyGd2SrcA3qDbyIU0qvfbtOSjVYLRv5uNPRsSa8N6FX0Od%2F%2BqFHStT79MLJNLT0lyY4qblm2ghTJIg8XVKbxRHH6vEu2LpPqOwEPzoiPrI0wV2X8l41%2BeKvIDIJjCdqescrBUFNUcQ%2Bcsxo877PYxVU1cD%2Bpe4TGOyBpCHdr4eK4uDR7Q%2BEIzOJLsPswDceQzjP8akeWcuH81sQl%2F8YEMlvHLA00g%2BGbZysNiVfwPa3sZ5uj8Zn8u1hna5%2FaPp0DP1oG%2F18%2B1Z0b0XOP631H3URwgD7SsqpYfAvE8cvcwg84030acabpw%2BgOIXfuxQItEEyVh24m1%2FsynIgQe2%2FDDNspj57k68D7%2FaO4viOhkAk%2Fg5PTMhndVPi8ofoqjPzCwX3nHdZBCDy76oEs6spNtW7GbYnZbU3F24iIj7ZlC0q%2FlNYDxLXUaZ5rjhrHHlNHtkvygaqu9j2x%2BB%2FgKi6JBnYUUz%2BV0x85A4kED91IOfu4tobOKHziUvtvOQwC3MmS8Dp55EfooGzXaj9nAzo6sueqqnAMq%2FOy2lPo4M0kCrL0Ma6ms%2BMePrG%2FdgB%2FUB%2B2md2M3KorpIG4nUAFQYyo9P3cbFXL2nLNEEOgOppQEKQpia%2FCIAcqCDWlkdZVBuyDF0jNMNTq%2F9AGOqUB5Q4SKon9fAWSlyc4h36BMZyQvxrIm5LYFjh%2FajFHHiYujjVDvzt3ULUR1rNe92UZQMm0oeN3L7lwDAgDEBqiIYiE6uoAULk0zil7fbzJaf5I12vfdVmXvH9z0%2BaOxz0HkWhS3JPg6i92mgtxAmRLZv1MrI1lduZ8XJTLBhPRu%2FVGfI5pZLEyeEuLbOCSY02CedH%2F6iE2fxoZqDuOOY%2BUe9DrYB3M&X-Amz-Signature=176137a73991cb1d54002e780026ff3834500037c4a0e35a5a1e87951ab05e74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
