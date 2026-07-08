---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZWMF42U6%2F20260708%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260708T190350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAMhykxkclwYm%2BGzBeGrsMStJI7jvytDV1Q1SuNQgTakAiB6YcDSgp8afd%2Fg5tbYNn2XskL8ajflCogkNO6gDKmmiyqIBAiK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMhjvtM5ahZ2VMAiGPKtwDWD%2FwJe5TogAX6Ip%2F9RHwLNro2T88DSLP9xL0FqjjmXA6KmVQCWTUBoy6C8bufhbi13fzGlytJzNpGF%2BRML%2FFr06tXBJbA%2BvVs54ABbFWJB%2BEQc0t7PRJxpHzWxwu5%2BvT%2FdUH%2ByzYJa4ZowbiZLMtafS54gSKfbUXFS1kbWzbdyPlknqi8FcFjQAuAqKf7u%2BO86qJXwswldLnk8e0wN9NYtYJFVV1RtQuhSIQhQ8tHB%2BW28cizLf17HYE7hivYsS3S3o2WGsr8%2FHuKCY9cDNJdhRt0VP%2FlFtaKsRS6Xa7o1q3IrKSqA2%2BtFsf5m0zmCt5BJHWOwtXPuVw1yirfWRiFYQRjgbgBdaecwg2%2BViqK7BAmSCaOFVw%2FMVgLWhDug9yK6ytknEMCWLfQ0LYhleKsmMMrJmojA2911V6o5tL5ziTJkMBVfbhP48pbosBbWQt8YIZh82xX%2Ft0%2FxvtT%2BtXTgOx1rakYh%2B6rQXK9G3hnAnIBW4sYl4MajbO24mQ%2Bp8kN7OZBWFqhTcEDfpfXD7JdfNw1HP%2BAg1Kn4HlapxC9P%2F5yM4xKE5hFi18TvkYmfwxqdHA04xx1sDPSsLby%2F9EOoWGIsCO4UtbZobuHMr6yC7eFZxDL%2FoCAhTG39IwgJG60gY6pgF0%2BT6at5Q6AcovRSjxb0VLUOJ55u6gxigG8AWPPv8x2F7RDHEvKz7EYncavj69gr20IId1i1X74drC%2BFSrXI3u74C9P%2FD5Yb29Y7sQpo4fI0kllYlR5mMaKSXAblIOKhyzo%2FYws%2BuoGKTWWwcL%2B%2Fm9G4eZMzcIz%2F9yFGZhpZ5Htv2td8fwZoiDpF2l2tHYZ1odB6i6qPu9r%2BDkXYOxDy8zHo8gFlQV&X-Amz-Signature=27228bfc092f0f29e5bb42c3ac2196a98490464aafaf369d2a9a29ddd28f7fb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
