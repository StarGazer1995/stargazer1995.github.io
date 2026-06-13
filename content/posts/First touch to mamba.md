---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAUGT32D%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T020611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFkaCXVzLXdlc3QtMiJHMEUCIFpwXCT%2Feb9%2FlftkjWYyVQ7rybx%2BjdOey3nTHn3Cnpb4AiEA%2FCGAWOv9vfHd2N31klDAUzFqHjKiq2nxpHQvAWE29DIq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDJi5UxE2Dcrc6JSzRircAy%2BO45Tz3hpOpuYeZOqBzEec01e%2FG7gKR%2FmdOD1zRQc%2BOYackCALa4mTu%2BdpgnAveLwXKCiH567IJDfsjeE%2B4wCltXuxx80O9R6n4MxhHpviOFftTX5F21RwqG0TCqffSDYDPZ%2Fq655MbRPJGMA%2FC5MEYaOKPVzwi2GtBPdFXtxfbNqaTpE%2FZ2CUR15fPzSlKTVk6tkj%2Fu1fBF0LmX76sM6sPRvB2cnxfMwy6zCKcQVdXvpfSHZe8l47oqef9d3id%2BhIF0iuiMHVZWImslYB7kIP4yQaurCr%2BMVHJlpycBCJf%2FXuNhxv7ttsxg%2BTE7vp2f1TeW6FYrTC016fhoUkLrBVoFIMhyCYBhSv9WeHCJG8RF2WazBpQl9OUfQupeccjKbe5e2Ey00L1e11Gs7ZYG6f14VmLw0JbgiCIbxJE3SlQVo8kbeT7CQSZcRQRUC2u7KdboQbP4REXwsATOXF2%2FS62Lx%2B9sQlb27%2FfOlsvogKyCayYPEVhOgQ0lbtsau7vyk%2B720leBJc2VizG%2BNLLgZpjPviazJAleyUuHR7Uu88lUnSJ1OkyKsivo1wkz81Q9gL83KWhJzkapLUF%2BHkjmQYbT%2Bjs8g%2FRdWBvqvxzy0CiX4kdeI4rHlVyYVjMJ3RstEGOqUBWpCksxknGcsrznqkgAhoSG90XRmcADzPuWIuUBjMHgx6sHmax1Bj42OFGxqhKD%2FqPnXkV3%2F5VuKzrlNs11kv6d53GC4f9UQ841KKE%2BZWHwxyLTITBoZHwby74F2NXGXVpoj%2FpR9%2FR5Dk7BOanj6BAfTiC0xRtuRNze2Mq4uGJaYMyqFBOnlkUO%2B0l1%2FkTI%2FC14%2F0PeXTdyV4Cjnu%2F38iposnDe1f&X-Amz-Signature=2c3124c39e189f66babec25a150fc80aa854599d0c07ad02c542bf6fa3a28f1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
