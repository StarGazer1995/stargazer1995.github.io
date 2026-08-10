---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W23LQBEN%2F20260810%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260810T105620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2FzTIohjECBQ2AuZ8SNC21sCkrYIcLDGwsHUl70Au8hAIgMtRQBcaXn3y8cgVT1wuVDBDwZTVdDANF8x8K1hmVWsEqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCEO%2B6putMZ8x%2BBB%2FCrcA5nDZuw%2BzojrXIRN4C6%2FShAmYmqnUUfpf4%2B0w%2FUIgqjx8Bhjl8abGylXKf1w54yIZnhfaeQANo9X2%2Fh96l1QdQXWA1kPDns1PQZv7VfnzhQA4%2BLZPhOCAnxIZBFyXvy7cEjl7JcJ%2BTGGQUDBYhF0OjcdmyP50eztf5fp6XFTH3BrRcYwyNKkx3RJsGuga9dE1IT6j7qhXkeDKFOcYIdAVSKjKfplF%2BueY2A4gldIpI63Z4vFMwHI9f99I%2F5KauGbs1Z3Zsqp7n3z7We14w7%2BuPYjJ9jKvzVhpjNnfJtZ4r6p7l9UnxHUAhLkEG3To9MkbVBS8daKxhwYp5dvU7ZiPf%2Bsgx0WBVPCJblyYxW%2FETP1RgUDKgG7dwpWIfcwSuyNDWxu22Bsa%2FfhmZzkDkKIF4PnkevKsVi4EIAvKqz5vL0iGf1mEVOX%2FB0HBNHwQAI61ZU2mWAJP1qKUHLgJhmfBsA8jbB9YBFDk2ngy3cWIVf8rk8MNBL5YXan6hOTYNgm0zoIviUMPxqOtASPcjuK7chq3LFRwDo0fsX3tuF0lbmIUq0PuDvNgDbY6h4mb%2FX%2BBY3SSi%2BDc1kifC0A%2Ft%2BIHw5z%2FmYsf%2FiyjuYOQnQdUB5XG5K9Hts4iaEGUSTQMLC15tMGOqUBSodESuQisWEx%2FhBagFt6qyJnYSquqJ4IGxIpKpNjEvFuoysSLy8MfJr0YQsuJkpijZ7D0TQblRwLIHQBCMSnClUqM6w1XFeR6hhHkxOrs8kYA6F8VXQD%2FBeewquOzAQoN2mSJA0gxfFCz%2F7DjxIrYvcXWuv2%2Be9eu8YtMHmymnVJTWjaRq5oHRBSLbqSYKHxtsndiYM2cPo0d4SD%2BmSmwKWDLOPO&X-Amz-Signature=4c7455c6d598c73552e42749fad0f7535c2b35c7a3104a2cb1113404d3037f61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
