---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBZWJYGP%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T190141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgy2LFlqt37SB9prJAU5kHd9YL9y13U2d2xa4NXxJfCQIhALtOi1KrHnU%2BwjjyC3SZp%2BznYbMWvhNGr7elqYJlLvrUKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjNF0oPHKlAdvbKF8q3AM81T%2Bs0jDGRoGNMSHfpUkFJTNOEzxgbVY5yxsN%2BrLorlK%2F%2Bv0YSKRysQS%2F83eA5sKM695w7DGlDGWSNA31ykx8zcbBHkpCvb6lD2fdP9y61%2Bs1M2TwcJv4vlokLN6m%2BNp1p0%2FiweNTN%2BoA4vi3LrdUp8FLJkbNfN58QZpZh8D84v1bvddUZ4oiBpvGiM2eK1vERQ3gUO2h8VWK1TFIKgsNakKoeazhOrYYeZrOrKBM3m5xmZegVGiCVUQP2Y7TlRQcWTgI0xGPyJQqNyFLs%2BRvaQtqoV3mj16g%2BsWIHNx0Pjqn4WEn%2BIA7CvZGRQ5hu35M%2FTVgfI%2FbGB1t7pOTvPndq%2BATNclRtou33%2BdjjQa4pBKhtRRq1dcYZAtN9IjT78jNb4HNQR2KzT9goh%2BjIPV6xBE5sCjJzreYnuc%2FAs%2FcADFQTcqv6d6UV189bicdSxHSP6EUIhOSEPf5JvA279VSq8uBGDin0tWqVJ8JrkvUTJa8%2FBgRHW4uYZOy4t2TQ4dGWXJp0laOQVe1P3Yqd0DBuAMb%2FgXPPFn6wTRfXO40NuxbIAchwAwgzhZz1TJeWXyengqG3LIcY4DiJqt54S4TogSlHK63RoBSVpKereKM%2B5%2FTkQ5%2FtWG5DTlTYDD0mYDSBjqkAYczKuzfuWVdX9W1%2Bw6eU7bgHXKe9gRG%2BU5gVhnShEW2eUn2zlNwMDnxdjA2tjvv%2Btq5k%2BjqCoUHEsWPqochi5vm9IfwN%2BTW%2FryfEpzFDGTeX%2B8QYbLSONcatdfzwTWFZrqcjuF7tOTDH5XIMDp%2BnUhOr%2FMkai91f7oQ%2Fxh5UyHLrNBJBTeQtGUWTa7inOorICFF0096yxjRROZFf18P63wdJVoV&X-Amz-Signature=207b52d5b25a801b433f2164bc6e688241eb2bd9d6b4d4f73b4f1508fc3a6d52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
