---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XNSZLN7%2F20261003%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261003T125005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCa0OLuQGR6XNZQKcruxOUqRMfIcc9zbgs4FufAU%2F%2FL7AIhAPK4e0qiwfUWdgN45W3Cxs9Sx94%2BuA%2FYt9xgPJjvuxr%2BKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzeZA%2BlVwcZ0%2BQPM8q3AMpJB8%2B4zS8rcXsA7pc7I846ldAoLGA0WLbmVHUDzEI3OjVc8O9x50xI1cRHZ9xXU7uBuiwu2f3UyEN6kPT3EKXhEeu4YnEME%2F047qlTSLCTTLtE7Ex1o2xpnZ2WQYQ0F%2FAt7plnV21dS6NwqcEGdbcTIw1BAYRQScCXNL2y2x0c0DmW%2BuOM82UZbdq%2BLoumB2uSUHz5LJp7v%2FnepggXog%2BVUU2vSkpuXlt5LX1HWlknbx0mVa5m4B02S2l8baIfHSmDnHdFEMFGtFgLVBYNZqC%2BK%2BdcqJ57kRFERyy%2FpqlUKHTRMMBdtBixPCThEfuTGf4NMK2jKabWRd%2Fhj%2FaAXqUYx0%2F0jdR48cc8k6W%2FOes2k0tACh0j9sFwaQ1i7nlZvw%2BZzagZIpF57EH2%2BlW8bXtw5a2U7DxnOoxByb3gQACbZE2bgA%2Bi6JfMMF0Be6e%2B6CfoNOtg83S8VNWC6%2Bn1ayXKLxhuPZKY9HRMdwD18lPUp19R2Ui1X4kUp7NGujgcWyo1KwR%2BDMmwogkMAOc6Sn01Yi8A7Wy1mMm17ub22EX2l%2Bf963%2Fy8TrPFTOA1hFUzhCRzJzFH0pMi%2Bmgi9X1LmzKibuBnPAwUFJtcFedhbukM1t05AdpCNVzYcv7DCZtIPWBjqkAX9eGuPT5gvF7JZ0YI1cXndjj%2BFkVsCThJyo6iOxdsAA8Rbsr4FCRvALNr1ll6bbBWpIoKomUejyW0eT%2BHteTYCnxU8BL36PIRx15uoJsBVSstNQF5MCX6M1vtvkCQkpR9dX9%2Bw3unqidbe2EfZrMQ1iTYlR5Ognv8FMiOIyQK05WQlA2kuTod3LNSe4NPx%2Bvi3V8DKXQvTR8JpNxP8HrO9KghnB&X-Amz-Signature=701f53de321ba06779d0bb5d1f38a801a5ac61613d4b5e792f320eac4e74ac73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
