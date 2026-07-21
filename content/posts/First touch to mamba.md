---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6BWOUL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T080520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCfiv2ruP%2BspSG%2F8jJySdqYVlhY7BS1vvzGKKDfZzGbWAIhAP1BWEFB6TChh%2F%2BcmI9KKGxxYBhnbSpbRDAtyXTlgSCnKogECLj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw641P49oWK1cuKekUq3ANl0Cbe1RxKievjjRpwYesB1iYza4bCCTZwmfQMXh8wpOfhXxDlTEkSNj3jjjc%2F1Bljdgrs8Y%2B1kQmUcKCFyzOU8LsTcgXk0zixcpz7Iji5fInoicQ%2BqGJJnfa7QXrBWmx9iYXQXWaVAt0ecXBybcvK6hPhvbjtigKGkDyyJeaMSr2dt5uXxI89sY87vn3EK7QNEmVXMDCTq1Kh%2FeDLAMtwisfo9rnDW7vE1QsTqDW2rAAdHHlqOlZ253laPoFFeNL1XQXpSkP7H%2FZ1qs3gdLzHgiFhMt1QMypFHWVpBqzr2j91VGBXNh7GBFqN0mDYBkUuoX3ACJJPVJ5P4tjaWqkf%2F%2FGXAasfB7Ci40NGp47ekFsaph%2BHHW0H7nLdVmKfIIj1bMH0l9%2B3mmvMH8%2BTVFxw1YIjov9fAhlHXSCIfeNKU5k7BdQMBgAjWaZlNwFouyvJ4fS3H71QXBADw8mS3gW8UjFnw6OXVcP8zJ1MlNe6wW04iAB83%2FAOFCMxHssfgca9J70L%2FRZ5vSu4T8JJh3yBhb9BDipwrho%2Fc%2Bk5ltMIbZ8KumIf7zAhVffntB9SoivFRusxBi6zNiOxYWflp%2BbH1Wcp22h%2BfDzTr9bk%2BVFUEieU7QuWqYj%2BaB6PpzCDqfzSBjqkAcUGpV1QUktWI0X8ZumxHqAmuICW%2B87xqKheLPCQu4%2F4%2BQUhVJMPyOb%2FKgpawt4oAvZLdt71yQq1qzSaGUVOxGSYtOWsJMGZIGHR%2B5riALdXujmAL3RQvMc6N1wHOoUfgA1EMPKeW0OWxhFjHLw0iBnMCRsucPjGFEGT1Vz7GQ8hOcmxUltrb0FvRfpKwvAyMzyc7aA6HFS%2FjZ6agx33qTD84f6v&X-Amz-Signature=258c2fab0c7f577c9bccf12298c106bbd9cc2bf1534024c3f7abe133645cf8a1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
