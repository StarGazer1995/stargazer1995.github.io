---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SETVZ5XI%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T165808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVYZ4P0byXZZ33lCfoa3VwwF0S1vX%2BMfLyp587QceaLgIgMGq3%2FcCOpYonPq83V1hOsP8tZsKxqNgItwnZHFVc3IAq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDC16VQsuX5otJ73agyrcA6Fi3FBq%2FPxdCiAcB3SufxOSC14PocHVA4VMxO6oi1eoLMHFUnGo6jnUErB8jac47ONIG7%2Fb%2BkpXM8YK8k%2FY43z8PTCX%2Fgs703lonuZ%2FfjUhJw61I21rqTt%2Fh7mswtapQDuA8CjfkdIri0UD8eDRML8%2B0TVM46DaWWkrGh6sE%2FYNgegbyu1wnEvMIN1j1FeMtakLC0ML1LYVDA%2BBffUioi2%2FpaGKIO%2FO4I5R1%2BQuTWih6KqmW4UArRRKEBRfZhPMG5RJs5uHJSCKVdrtVWC8t0za5ykS466UtRP7V7qV9JST1b%2BGKe4yT4Xj1fAvLcbq9YGs2ayvVmoMS3fvdtq4wqvJk2d2G4cyWJjCowoSXRHMA8hpjPU%2B0G4RxGIdSeWiBD8wbJLT99j22wX8nH%2Bjr7y7z4Pki%2FHXE4FYosR%2F%2BF%2FVSOxJCkkYFFXrp8qXzCIpxN0RxNA8E1RYlfE0xGk7y4FHOt%2FNe8GHwVDpUGI%2Fbj52SA7iWhOli8IFtPAMU9y7lQWn%2FALJKD8PDwVXP3zjs71qJonSTsv%2BIFTtgVKF%2BavNKm0cS%2BPEjBC1Jy%2FG91ctQ7Tpwvr1wglpP5SMY4FVH2hyh2yGRIJVb9odowRRMMDwAq31D6PFp3phlPoTMKeV6dIGOqUBxYwpgAQ3AqjMm386hIrLJwhH9vgZA7onlWvuYPiUqt%2B%2BfwAbaHrJfYW5WSKaF4ATamkNg9iaRqkMBon0BXGumhTK%2FnIZ37b3Z8WJ0AI05%2BAHkm12icNWR6WpbCJjX5GSmTXoYsttnKJtWs%2FxbvjA9mim2%2FucmfFMpoUxe6TdtcZVGW53Rjs0URvXPaNtLBkC%2BSMDOUYcbyBOFV4CnD31YjNrSnnw&X-Amz-Signature=553e40cbbac8cc715dd4a10b65001c7dc3e7770c592d5d7495bc40c3030e33c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
