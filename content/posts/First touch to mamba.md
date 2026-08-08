---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QBFFW6YN%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T063207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBrSeYVf466k36XXRBWSryyOBJjUdI3smEQjrdkNN2q7AiEAsudGG58rvXcgFs3X5R%2BtXzSAG8DVXIsAXY06ntJNGEsq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDNQYy0cD4md7zQJhaSrcA35iSLHcFVKYPQUDmD0tnPG2w%2B2aF3OBc298AH2fMKaoYTIDSgyOrjME%2FwNd2mjanfBuyYKeh5vujH%2FLjvzVZF0RD9xyVlsQn5v7mBHmgDhC1NHjSMAK%2FX1HLGhSy1UymPbM22gpwMEXts2XhsCOdMlB72d2ToM9IpkSTlpXnH9bPfS8asiXIFZTXOVUWwbm7PbWFtfgbuYfigeBanLSNcIemYBXCpF9N%2BTb8kdVKQasQrYdzl9vn%2BbGY%2FttECfKE63%2FjNDy%2BEGfus9sTf0Y0hhHlNhw0TRfD3bFheFj81aSYzlLjYdPE4bDywFBbAmB03LriEll8PdpuXckekbUxQ4vmg6z9op8wBxOLB9HQe6DYoxUSMmi4gGdxgavjr%2FlWIWtErfrqjYn2Ppn14e2HSEqPrda9VrIkEhXKamEL3jlz7%2Bx1Wfo7ySjKFgcAdOLADKtYjnc%2FDZpYkxy9KKMso781%2BOi6GCfh9XkveltEJaTz7VB0v1iubvxhsu52E%2F%2BbcjzgzHmvSACX54SsY%2BWtOMWtSAANd6fnZpFSRLpW0acyDZAd7HPXpGVDgOLb4lxLBHZvgM6EnyY9uSQZBfr0G4WLLOE6LO31n4CGEUgWOqVg605Lg9NZvLQMrf7MODt2tMGOqUBsx3Utbr6D1pAyfHHuPi2quXnjefTjvR5cDTLm8853PXYQKqAq4I%2BlmyEMwX%2ByKZhuALvysZ91DA4ZKtaqfHlF%2B7IFO3kx1Xz%2FvZgMWO0mXxZHXqCDX6kzRlN30m1zhQ0IKWG5UPAkvdoLJYUAurWHa93k0uLrnw8Q%2FIHqNWor0Efu%2BOQtsquJl37zahvt43IaikBK6dxk5PwjVFfY6jtVm5u8kJq&X-Amz-Signature=258a22c6335c0a65e6e0b13ab1ed8790594756538d2e4820eb0235efeb05f04a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
