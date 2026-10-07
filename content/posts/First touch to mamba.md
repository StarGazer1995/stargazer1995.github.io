---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGREA7TX%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T075055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAF9IQX7NutavoM7rqGS3ZujjAzPlohVS8UsaFiNrMpAAiEAnpOgBQPIohDmCrUxTZrck80jEq5BN%2Bzm2Bpg6WN1mJQq%2FwMICBAAGgw2Mzc0MjMxODM4MDUiDC20J2t1CzUgPqoiqircA6EFb2TnivxwkDVjYLgRXJTr5m%2BvOLO25om5eJXViZI0JCTT89QY8tAUZLjzXwY1AB56g5g7Rt%2BVGG1uMfS2R9ncSuw3o2CYLIw0kPK3aLmJhvffFXXoX6Cqe4G2hyeIVHwenBeeaqKDtf2Ne2SAW3hFrmMe1Ddr1FcF70tjc0FvVUYA0zLpVeCXQ2WDeoMnZDpY%2Bw7j1owAinN1INNcP12yFB8BSB1671FPqMFYMjfVUbrxqJi7IhcTfu6aNij%2FJax5yjjYotR61So9g9zjHR16ywBS3JVr7nCyqjrC72zxzy20iGeSzukHt7X58pf9w3Yh5TolFUOKN44jRUlG5CRFL0BbyHmC6J9oAJqT3R3L1hew%2FDnfVtu7Bq0urBLr45FXKMRluyMvA77RNls7fHiRn6nDKT2X8%2B2lN3XikTsMpTRgNq261O7FQXW5IcxREI1%2FsKBXBUbKoel9vefVwjPIzq1kzV11JmJC9VbVdpC48zhL8V9oc2cbCgsTCgWM5RZJsoCVMhduBEiro7Cr0vvGiRyvRwheTx1Ma3PYxzcTeC%2BVz1umAsVsSvF%2BC4dTH6UtKGf2obJ7Y24ZrEPQKuLNgQHQMt7v34UtQhQzbexLoGv1MnRz8fkz1BB4MN%2FOl9YGOqUBlMhNYI2sHwRMWgpkyIOoVKeoRtxyakQL9T7yzFOInkcH11HPlVYPlFKJdLfqDUh%2F%2BSn9hcULUu1hS4baGbghrNnW6QQut26h718PKJEq4Eadp1%2BBHsIjlGb6po52X7Gf8Lmhg0X%2BRQ%2Fc0GdnbmausSrLdJABwUhzq7cUER2g9UQCpF%2BvT0h72yRMGNsrPZJyKl4iXGaI2ZervPqF68wTdJfBIcAT&X-Amz-Signature=6acb4883c8f7866f2883d21e411bd04e2e49b10a43eb91404b9e1a64c33e8d7d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
