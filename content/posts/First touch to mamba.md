---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6YCKMLQ%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T185220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDy%2BME3%2FTK4E1m3TqnOXCzzL5QMaX3cuenRTzS205pzNwIhAKwa5S7f5xhv6PZLUK7c3Sc9E0DEFqt2UAeqanScmg%2BKKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyykC7LAPTmzlSP%2FDwq3AOqzXC%2BVoJuhFzW9fJsbf00%2Fdf6VwvKNqdEmIQunA4JVXolllnwJ04fLI2xjrM%2BO%2F95bvBEyuzdBM%2FmlHNUrKj4HR%2Bs2ldidZ1tCrriG4MktebknfgNiIuMoaNiKkbfLOsb2ipCratGe7lz%2FnvdEQSUdf8XM2tE61WIBfnUxZAS%2BOZyPBtuwfEm1RPF6L4XCjLIvfoSsZpQ07k%2BqGmGLZlzjPR45gSUMVVUoObmeGukxBNguTH4gqXoSCGCkO92JiXTrzbe9h6Y84zPezRxuLr0qKdtu%2FTiLUdAj4j%2B6DztIatJCBcUvXVFIVKPHwOCsRDtxvxn7a9xiEuz5hdBTHlv0PXm3xzQKc8OgB%2F5w3R7LfwguNyMOtvQwKCyRzGKGdn%2BH7la98kCdO06AE7889R%2FOtckYJwaPeARJWvK7vnie28Omm34v00zecjrNFF5aXd5bQQh45x3LyePt6nHoO2GXwBlQvyzV8DGdKRetK%2FDODjJp87BSIf%2FrdNySMRcKDHg0aK9rPqeH4Y3iEb6mc0n8QP1McetZDV5HjbE4CclTXs9cr6kXj%2BAajP%2FvTMV4FDVs2gjNasxUZOHegkB4USWI7o9ctaZyDlAJq7yfTMuyPLBuXHSf2pPONBD1DCckajQBjqkAWjuN%2FWrAQQ%2By%2BcgN7DNnwmhzMRKe%2Bmv3A7uJtrTAr2OGWS%2B4xS%2Bs9ySI6fKsKhQgeG6Sz0gceWAJXER6hu7LmpHYvjICZow4cWOGMnLjzw5jxjkZa5lBDpm%2BnSmGBBtR8N3X5Tj27%2B%2FCXPM7moYwdgE4swaGD7LSeACM63yL%2FQr2v5CwlyYbNfTrl1Sh4Ukmm8F8ToCyeH0xBx1y1IOhg8e6oyd&X-Amz-Signature=20b76639a7720bf7a685eaddd2e194be23315e913962e438234cfcadc7c6d2c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
