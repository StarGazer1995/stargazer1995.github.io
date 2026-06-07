---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5ETA7GH%2F20260607%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260607T190409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHF1j1nYaLCuSz%2B9blMHNenO9CDayG4ooHxsyB3uhaPQIgc8qyTRmqUDkR%2Fh1%2BY2Tr%2FZHfh5wrqBbGH3p4OAjkfzIqiAQIo%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJZh6Aa0q6OKj372BCrcA67gd5tjeNLL01mcC6OFWR%2FqKwz2K35CpbQ89I4Cs9tqvItyvzoiz5ueCj2DhV29YazJXFetiHn0TwzdqV9laZZCh4Dyk%2Fcc9gu4zP7zYL1zzI36qC%2BFBDIIE6XPNEWNp2Knl0G3VGb0%2BfFkQW8fb2AZ7nUrip%2BsmvG8qFHaklkAvsqtaYcOi5peARZfOCgajZnaAhwC%2FSrYJN0CKcs88mrP7ouJNIv9lb6B0Udymni4kcezTr1aeeU%2B1pXUGRm1F5LA%2BoRF92rTR%2BiecTIsB4xHteNglDq3lzvcOzN82iJZjAvu4gMAn9fX4sbe%2BFHwdYA6oQTFH7k9gB48ni6cEWQwwPby7k9u03tID7TPn%2FYw%2BbokJ8EVNbQf5Cza%2FcGO76QpONoqSw7saDhAESe5l4EB22o5QKfDPxnr7y8oLnSzKftvyPiWNyxoQWiTXzMTiRF8sx%2BL4e1dso61RBVo5Sh0I%2FjHzKVTWMwGR50KSm71AawWylpKrU3%2F3d6%2BlyhKMTJ0IxcxqKXmm7JUDcNOrJmBx2pvtBKE0CTa5pfjAgre%2BtnNr9jEWQFL4RA7g6%2FWqCaEbz%2F5cV9jNyyzbtcZ%2FfSGaa5CN%2FR3%2Bn%2Fki4P1fsolHoVBpzHq4wK43dU3MKDhltEGOqUBggjkxEmCdXkrN%2Bk9nTVFV17%2FkuWCg1EYZk0vRXCScO%2BGcUZ50aYFgr449uaHYw7bopQ2ZVVTZnE%2BQLzL4ufklZBCbKUtej%2BO3cUuWDhGzVZckq3KFCYkPsHMpYAFSonsiQsZF1Ci4YLxWx4RMEFSF%2F1MWide18r5eCPpUu0pktc%2Fs8NMRs9qJkEfoCj54b0tHDvRwX3bSn0zeiQ%2FI6Mlh4VsNWLa&X-Amz-Signature=497d58c6153787ca20bbe4c7b82d634c89e0db8a4e9d6f57e37c615aeb6d5eaa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
