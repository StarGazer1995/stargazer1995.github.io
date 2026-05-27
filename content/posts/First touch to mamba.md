---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMURWAI4%2F20260527%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260527T020717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBCsBnzvbCuk2meCy604yjgr4KT%2F929eOxjSbpcZ%2BZLAIgXqzso2A7Wu9XKcsFwJJECfxwXvEJNemWdi3lEmgLpdoqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO%2FZjXZAi5yHpCE58SrcAzAuvwjsOafWCE8KDBT7Wmw3%2Byi7RZ9B08ZuMWoudgBK%2FAl9oS0qDe%2FydEcQ8XbEnw2gPaAqECCE9eirtCwDZDwcjyTjKonEO8nuG5SGZ4hGBOJeqTHtgyEcFPVYfNjbSwHYy0MO5tcADrfoya5D80Wp5LuyRLPZI4gNibC7ygONzPOExUzap6waKhozGeKEVkFXI7BD4heGiACHzEJBhCItmbtFYqzIzF3Zwnfm%2BsClBhCOW8uvXv3ka4Bh9rk4xs%2B%2BZ3tkb3ectuFr2eCRYPQX1zXANHs7Y2%2FQcYvkRPvuznvzdV2Vp867PTHtme0A%2FKmYAv0faXsmHjJ5UtWrq1yHyE0OIv8C%2Bt4D%2BhdOT1MgXYL%2FTH%2FFyFn1f0HrmAJR5w6QqQEq5YezGOCAgUZCStBitIqj75YQKBS1R2Cg3x%2BocIA480hICroV3DlZrMWuYht86WQeWLjoOmm8eEMqpySoa%2FSv8dqh2QbGny%2BEq9LJcvjNtq6OiTgD6wZxk4OOGbo%2BoKHMf6ShTGvtDkqx2AewYn7QPWvnLSXSVp4nLZpKkap4LWMYMOmCjpTX5jKs9nK2Ay4ujFvMlcIi4NZbakcXwBuC%2BJ7VJjLyEMFxeK6EZrotGXZADZ2Tq6foMJ%2Bc2dAGOqUBm77GcAPuB08aLnV9Gy1fFguDrH5INUjkbVBgMwvAWHwlNZOxElxwxY7cXJCRW71artXDT5KW%2FHDfGUQykE1UV9AKA7tcByzlMH2HwUM4CllgfMb7bM0GaGponiJsGQoLe8rQWb%2BSCCpxHpcdTEn7OFTLZAUR26%2FbXDNDgo7JRRks85QdhQ1X5qC6DtBA%2FL6X%2BOW5gg2yci0dP9dFUO4MK65Sdmd3&X-Amz-Signature=d4cd4641dd49dbb4ea16b7f119d07a1ca5363dd260b7e2f24fbacc624b2a1dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
