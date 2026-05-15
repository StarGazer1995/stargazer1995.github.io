---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V2O67TXT%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T132518Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGxRAf2s7EiHmNUE0mgQH24h0%2BW448Kt9QrqXXamAK%2B0AiBqIf3mN7tLCHpghaREqAJdm3qWLRb3tpsDKoFyjUwDSSr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIM0Swd0yPTdEcwMy4eKtwDmVZh7yDEPMz7e891OW%2FuAks%2Fpv6wZFXj8XULlO7Q31tfMnXztQmW88bmTyff%2B0KP7WbxEvqCXK8jduY8frlJlb2lm0vBRQmKsn%2FNHiv6m56k4GPDOjMdkKADoeKhpHZufPHrny309hYsuEYtbpwW1phjCMGZepA6mEAIe%2BSuHVBznbFLxmn1NACafIxoEnJnAdOkpLSIN%2FsGRoYx1IVsuBH5MUZhP0GHekAw1iIQrg348PcZyNm2ueVRGp%2FCpkKCepxTUx4UKxhGqekRqvrLC0GQE8MXSk88tQmiu9e9JuJqR%2F5bcEod4lArMN6o0WHY8jjbzyDEEWjVsD6fLfoo4hyoDkIgMg90p2leurbV20x7ijBAbcxwnGWbox%2FPof68h%2BiInRq9PlgpGhs69FlzrWgRobijcHr2UyO%2F5ASh1Dgmw6KitDBiCFjWfE6DErDSqqjaj85apZB7wNAuVPSyT56Ak2noHYXYzt11ZYT6Y9UADcwR5TqsrCAbNmza2%2F2fV3OlceUbp9ifR1zbhhfLNuegDv3Ja3qp%2FtbbDeK%2FEguJfoGfAzVQ3nWgap7dJWc2WftQb6oPW%2F4uvNwPR0UNwfXaXFCVogavEaVAaSGwwJxaI3v51X1DhXKz3%2BIwtqqc0AY6pgFBGFzqNNE9YhBqFcKoX7%2FxjbtrBkVJhqwDIEdMBaHdAfHfLJtaM3tHGu8VttlHe9k1vSJYWqf886ARtDb%2F2qA1xMYilvyjQgkf3ozLx2ek0lLGL0Lja9FeD5P4A3PtQXxw%2Fi0yyDGcKdIM6tYUO%2FO%2BQxSIA%2BdgTeY%2BvYwUl%2BUIkRCo5zntiZd7EdCuERQdqbKXX99qgU3vY99FcPzYOqyFX9P4KTbz&X-Amz-Signature=a4186d8397210bae28f0d400730adbe8abcfcbc952b91eb23a7ee2ca83902d09&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
