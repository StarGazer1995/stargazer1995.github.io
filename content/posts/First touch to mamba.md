---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UHRDO7IM%2F20260920%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260920T073013Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC70FVobertgG5os8AAqgy8CJPuEeFtZAyvXKb5IekpYwIgXM4bLFloWKIvFWZzFT%2FKW5kN7y%2BVjNpyxtABC4sVfOgq%2FwMIbxAAGgw2Mzc0MjMxODM4MDUiDC5KXEyuhRq7D6A3dyrcA6aAFmCpjHFzx3CoUWbEsQD%2FcbWdHAR28CFbsZcKP%2FYxcATssBbuWEk%2FVkNfhSezqrQyJmY2WotWxuCbgrApUJFKJSOYhS%2Feq3ffNZrWiitoKm%2FwL2MsQT%2Bunu5eAX%2BPCBy05UXYf1nGVJ3EPCXLGOmLeANJKZurdEX%2FBNFOxgbD4kUIXLuLHda0wCmZ%2BZ1akt4R2C71mELjfNoObaCf3GIQSs%2FiyFEjXekotM2WVhMvHs3ZYGUS9hbIbqJLs%2BG2m01skOcQk0iDhmJdeWzSvucdgu3TqW78YpNUyR4yfFHoC4er5S6LMzZf%2FKAQu32sMtsz8evoHIapKWIHcEEJOntk%2Fx21%2FTSkrnCUwE2edbtp%2FAFq3zO0DFTb6lzFsOUxMKAGniSPZV04FpIIe1ZclUfju%2BRbNPElbnaE3VdyooYbs7SQ5YubVfqrxZQYaVlPAfIh8V32hIEfff%2BC%2BWsdZLO%2BQp7fO3t%2FNa5iVUIfxUgmNv7nbmToAsppJ%2FHo%2Bygl%2FOLDtyDeM0EnheV0%2BdWdRVjG1V9HTUSyHwYw9T4rLLfjqXqGTrwt8%2FpkQWxHNeLu09OSGE5tGtiQghOp%2BHb4nNW0VozAoY8o0aR7WTM4%2Fbnwvv%2FEGAvPoeSCnKs%2FMJz3vdUGOqUB6qbs0U5gEzFySd%2BqR9%2FkAV8Y8%2Br9TQHp1HWGiA5byFGW%2FMsujioRXlMDFd4eP0MbyOwrOgvCfTGt1b%2BeyfUrNNBCdDvDHb%2BCHV%2F8Yr9QtZsDCv7uNkOLaT6MD91KvLQxh3%2B7zgN9egEOYVxKBdc5qQD5RBntn%2BmymXtVxwPKhC%2Fz86qR8SKLSZ%2FCLC2QScdU6UNOGnqrVW7AMU8W7JEtHnHw7hSK&X-Amz-Signature=793c8281fbc9860d8706497fe6e98db3672cb28e06b4323af9570d1554729b75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
