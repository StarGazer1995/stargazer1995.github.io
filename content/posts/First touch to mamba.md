---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633EG7RT2%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T141209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCIBH8AGLE6mQq0gWM2%2B3bCqDKNondJGOaCkKZYLJLVijWAiBAZDvP%2F3NYz38b2ji8f5iqLC%2BL%2FvDLyW8qBm4KYIuy2ir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMxv5MX3qfK4znfvqkKtwDE%2FqI0yGBOdQqjoEJfl2k3vFlqjtvlEYquQXWalJHrcaDXk45e3NsmwsY%2FjVhr1t3lV%2B%2BlLO6XrlT82ZIoT6C55xdv89Hsxp2V2meSRXozoSxEqsYU6Cc4boVJGyjujVBpSRyWQq2G7lGxgjEv26UjICk4AILc1rCDqk8DnkNRv0Vf%2B5VCnu3NCKx6RcSKi5hX93RcVM2yFK5G%2BilnBg%2BmzqPnXl7Kv%2FwO1tmKrW8WAMW53oVQ0hd4mIrM7KFRMGgthtkkGgmQ2qOW5i1Ky2XinqVWtST11pZhvhlzCP2cd%2BBjj9rnDByT68J2s3q9YIYv5PfdsjtCUXG5et8bURxn5FNK%2B%2BuUh3Q89DvSo7h0ibr1SdLUAK7YWLEBJIYHuvGL8yMIAo6QEx0bdVWDIxK6OSthQN7rukbEL7JjWCxZJbz0PZrKbh1DWp4FZaqVZQK0GqPNZFRqUDoNR8AaVNAQrz7xhyo4aDTF7PqyUKPxAHB1JT110%2BtRCigVoA0%2B5JzFjevlkdSHtbiUOd0KB9QRCYT%2FhSxZC0frBxr0kzsDQ%2FwcrJfHxCd6jrrNBOV1gNvHgxhmNtSIVcaWLd%2BrryYmJAZ9i3bx94ubVOwYl078ceSjd9huYMLOrgCz0kwvpuB1AY6pgHBKCkSp%2FA7noblEx6ebok79m6sTkDwz2zjtZ9HiISH9gRHeeDO7cPet6RPaAj6pmSRcFCzcYgIXtKcTUGYC3y1vhiX%2BHbtBCy1aq7I6M%2FsYVjnDpri1%2BDBifvygHX1%2FjQmtMApV50PC5PtI1Vat10lDTBGKxnRHyNzxiEdmYP%2FaSlvApbTzrr1EabeozTQBbkDHa%2B93lBRnWNlufYcl5BxX6baTshC&X-Amz-Signature=ca5af4874f2a3a8a4d5f793ff8e9780e53ea05691996e2d4d2c2169aec0e79ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
