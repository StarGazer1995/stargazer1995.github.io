---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZ3VOM5V%2F20260620%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260620T020651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD4GIU%2BQ91uGtjQ2Kx2CBr5rRG6lhj%2Bmn9HlaQYlWftqAIhAOI5DOTwUWWSfS7%2FuIJMqrnuTHabvOsn04Ka9fzFJ1uxKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw7T7UNv0%2FYE%2FsHvCQq3AOEk9x2feRqxZM%2FVI0ufEplYRVHmiYf5PGdZEtVWxpxEmOt0W18zwxajcnWKJ6GNKX3X8eQ6zWV6Ov%2Bl5s71U2LUnvkPP3PpG%2Fsb2brU0Pwaw8gGCyNBDMCQWUZtWJe4T3i7dMasdDf8FG2W9Qrg%2BJhG4P1SS%2FRO3Ahcx08oqPzrNdTRZhVyDahj4yLIiRdlu5ecTAAmSS9OGKbUcGIWYLYYrhBekYulxC6N4jbdGP4v93W%2BcQVADNGG%2FW6C8rrPylXj0fPdpI4FqYAKSUka%2FkUu%2Fr2GxX8BuoL3bcIdlgGVCjmsy0R%2BWLD52VSwWpdJlNDloZQx%2BF1sP8MX3%2BobQeGgh6tlzAaIQVI8ub2mJFos8B680NWaZD6f2pppTioEyVAS3Zc63I2jy37CQVde2QtTbh%2Bg1IQmKRErLN9oJLOQ95I3jAouUJR5JSU5IO%2BigAGB1x2yz44SMY1zA10ZbCaJ3iX8jZ1YHR9%2BkPnjSTgq1xKBN%2BYYj1LchdJdVF6VLkSeS3X79FLkNXiXux9bQ4PBy1Wqa%2Fs1hoj920rveIi%2F31FRzMdy7nZn%2BZdR23Gm3jqHV8m3AQWWudum0Bk9nImlQaquCCTQzoWY5zKtH1QZnwy56Ic0%2B7gj%2FLGzjCJ1dfRBjqkAQ1vAQHhUKxhPMasl5vhJO0rRSyNxipolwsu5HjOJ0M%2FIp58e2SKD0b19jQvt22Fo9V75Ulj0inSwMWBqLo05Ncj8%2FFWGZUL6ldePttvlhK4%2FnW3PJarTfNBEeV3VxFEWvrxjT0sJtCK32IOnd%2F8cKfjbpNCDYdvadUOAF7ONEdZ9SNv6jUojeo%2BolYuc03wSHWVUuX1TAiiJhvJKclud9Yr6bYK&X-Amz-Signature=c12348f7db3e0f35d3dbdd1eda64b9f8fe8e1fb326fc1c35c337fd8a3715d594&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
