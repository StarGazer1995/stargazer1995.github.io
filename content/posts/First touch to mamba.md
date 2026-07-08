---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WSXWU4F%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T205446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDaModJ6r425Bhtqf%2BQFmL%2FRotYerAEpDG200yeb2I5owIgATtGUY6E%2BTdgHCSXTowWwmZScgKhCumxEHhbBl4VFZsqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIx6sYxb%2FS4mFnXKBCrcA4KGfC3acVbutTUKTrDMfWMqCZELXJdVosbHJM%2BOO%2BRwBmn8sUaCuDYyp1nuUtfa0Pn9acDhQ6qB4jkJ1uxnZcJjdNqMYdq2BG2k7pWGctIWeCv%2BvovsmGCfZ0ksoB0SFhhW6eMJxTTzWC164LWMfKPk2oPz8Nbhzc9Vkxb%2FO1GtRN%2BLLfYLACM4%2BrnQhrsqlb8vSDT8rsmBIZR7smVahGpdqrhCpHu34HQhdVF8Cvw8%2FuyvEXCzZRiUH7uS1f3slRXvfgvHqs5x1Ee9dmitjPrmxKmBpcZkxn65zISP8N2vNwk%2FmGHmGSQysH54iUaRSwwxACGSWFU7yV9kcWYbEqEI0yGSqfCQPVlxDu2X%2BgBW0y0j4EYRyXDHs1SdtJhBhDou7zF90%2BSy4IWxmHnMjvq7HhbRX%2FLUiprBxVh1l%2FL6JpabBCee8VUZXc%2F%2Fwp2VPQz0KJa97lShkukqAzaZP3bMUjXWWBj%2F2QOUzek3aXMH3QLMRmMzcFpRvimKQX7iaNsOnZf6b8DiMPnVv%2Fy00ma1LrYMDaNmRH4m2BWRHrAAIIhAUiMFHuhPIxgQWEygp3nN1LAADFte%2BQMVo5j5%2BcUScmoQpwUrOpLG06aQrg38ORbX6HZ6H%2F4d5OATML7LutIGOqUBawlpZt0dHG6yg4l%2B3dANin5lbz0eh9RK%2F%2BEPnuAtFwto5JWlqvEbOUgrDVwulVim2o0arwIHyl6XgNNwTR72czggVuUmvR4FrO5T%2BgPbn0qoYz1NQL7XQ%2BfZPiZzfGXa7yCkhZqViDrquL1VVmqTpa3lbhB7wd49WEbkV19M0siT%2BOUVu%2B9vX0p60ib0W5u878qqFX3cVJX9Mwznxog6bNIzyfGO&X-Amz-Signature=da6774fe99e9380403587e736e39d3051f2b93dec84e160c70a118ae8b49cc58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
