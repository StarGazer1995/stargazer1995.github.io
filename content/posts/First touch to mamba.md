---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466225OU4SX%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T164552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYLmM59Qu2XPtk4fFqHLaZy26PSoyQy6sAHCg0ZnfreAIhAN2FpR3dMHW10jOIORe8W1OdNaN6VFB41hyL35yghWqYKogECMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxvrNQHSl7orsN74lwq3AOAskN8W8NMUbj%2BhowFv1G%2FGxkaQkGUcpF48p6Uy7I3ftMVnK6YRgfIdYUbRyOx%2BUdiK0GxvKRFYmospS0KW14WJNrS2SqecE8iwMPYtSwUEeJwJ6MWjZPL1KcDYDWVfndil%2BcpU1b8GC8yc9VLsPvlIMaPqEgvy6g7TEoTDlevDBBfqhvVij8sdjTSR7wV1aeFc6ouV2hyLy3uJBP4s7uvVt5ZB%2BB6NahvJoZfRjBuVQfyJL7mSgCOxwKDBqXZx2Tqzkuzui1f168xKv%2FmVsUXLUMDkLKqhGLVbHRQ%2B%2Fx6k90Y9IyY%2Fqf8WBrl5pDfM6VoHe0wALNHhgkkGoS3UsuNCme3WDBe0Hf8iBN%2Bc4c0N6DeO6Z%2BxMaTPAChibPMhn5B7XvjaSsZjjA%2B1oh3igxE%2B4hb4%2Bjbnar1ScHu0ZfFBlS62mvkUKuKpGU9cwk9fwafwBeCKtBrDc7t%2B3Gb5kiFmCb%2FZymqs9gNM2BMBBpBk8jkocpNqGrJYtPCvwpg%2BgcaWUK3QitegjdBNMigJTYUa3fJhgUVbomOZkPDPvjdWDl2hkfDpN3ZydtzDw0HM3haI4Z4gRUz0a2embfSwl7iwqjDMsPmZ4r8HOe8Fadh8%2FF7ODYlE1JkKCfcLTCbl7jTBjqkAev%2FjELd8lu%2BJl1%2F4h%2FaVgYySd3gkGNWjoO%2B5ffZoKTo1dhPAFeSgB4DsZ8YIgyy1or3TOWC7YmID6KYTck9jQVPeMkjFaDXUZ2GRr%2FY1ZjX2VaqNwVV7N3rW%2BWD1dpG1T1Zk8GvJpVI8GlbRNMGWKGH2qvIsridbmbL7OSGiLKMjoEiA5IE03jn%2F1zW5Osox2hmkZ%2F%2FNZmWObmRiWUYj%2BcroOXg&X-Amz-Signature=3b58d87d872dba6e4b6c72141a24d153848b0e207368361a6da062f47f1f3d61&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
