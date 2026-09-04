---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU6JPWVW%2F20260904%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260904T122001Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIFdlzPj%2BFWvKyfF7bpBTi7vvdUDDj0Xioa9%2BlJOak5MIAiAWOSG9G2rX4BEitveH75ZaSJMnR%2BsyzANiJN0KxVCybyqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZyLiYxCNHlAjJ78NKtwDkx22g7nySwamP5RqPEIqpOBD67B2NosvAsYqXA%2F4DN1zi8Z6dSIqT3Zx2wolMCH3YGAPYXybWdudl43NsiO2kCrCErBQtVZJbe5C0rD2lyf1ZpZyrAdPcmWB%2FE085ckouSgCGePGLCAjphLIlQRwser%2FYA%2FJIdmVXmgouYvhotGrUdId5FTTMFkk%2FdfY2D4TSLNUl9WlNCQFlq%2FtM0Ly7eIlioSo5sQEuQAKP61xBQs4bqRK17ZpZzxhe3DNTltavGbwSXeXgbeN%2BbFEh1zkL5EKN4T7BjXQVw0f8afX0ie1lLTm4tLG0zVe%2FHni4r8EeifHmmmlihZA9XUELP%2FywwWjSp8EynxrpM824eKNuW4mAzWXKYWgXVUR7oUhUEWcR2nmcUtYjmljSrMMREHHSUibF5TcaALR52weE%2FYEsagY9RnWD9vGq7%2FRlvFZ0wLD4nIlh%2Fx4M1KxCF8P9KEFDcumf9YfD%2FNdQmRTuybCKFJZqbSgk6trvdsXS3FI48mCPV%2F75niy46pQmyHSLwiRy97Vh5Bz7iAf4NWrWmiA1iHyZJWHgR%2FNdcw6oYYj%2FLp%2Bcib%2FGv0Pg1UA76zJ%2FgJbEYpiZz4DOUdSHZxPGuPjEaZqyc6iWTVVz51DMokwxMHq1AY6pgFglHRnq4F8HxFFyhBXtHtSrSyf9O5Sw1hBtZBsktNITb5dALexwcSVt1Npf8CUvhqtvlh16cYjt0t87aGjxp8TFuH8CzV0Gfwt6TIGCS%2FOp0sdj7815urQsrknx%2BwiwqGNo%2F%2Fe0%2BciZTc1joonvdBOLOh35A4FiTDrC8t6qFEDsrEOgGDKxiO7xkCvH6lXAx7%2FAqdmsmGxqRmNyUhuL1LriCjpXXBT&X-Amz-Signature=1b104e3fc7e13fe563db36c8f27e6d27ae4c98820ca1c98838abf3ca64a6ab9b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
