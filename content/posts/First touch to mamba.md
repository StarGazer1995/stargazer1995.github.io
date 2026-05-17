---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QKZL6ES%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T015350Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDtBzw247KeMGOn%2BwgtRCViIprcXi%2Bh%2B5556xCTPIiingIgAc84KIBhPFJ8NtOjI%2BcLXN9B3%2BmhdO1nRApgEFvx6vwqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO8aT5zXZh%2BLW%2BBSDyrcAyPdyEGOaXOdJuHzYABZocNbO5JaghMYGvDLvGa%2F04UC5S6OY2hJ5VtAiC0f%2Fgq%2BJ5vvE4zMDHBnJ55xMWyFrz7XPD7c0F4ioR9v%2BFIeHI6clWjxBtBO0BfWyZQmszGylN1%2BYMZqZ6x9DdhvCztyvIHVX3hK5b5fo6M1s%2F8fquhxQOCVmz3f8OVFzU0ZC%2FdmUs5H9Sg7t4linDnh5jQO1sCPzTmIRpekqN7eksQtJLNS7O6i6VtC%2BkZm2oY6uPozC7wGcigxMhAfyF0mTkfjyynXe47thA6iYxitOAkX1uQ3bXCFe6pYQHmHp2JmTsM4I%2BacyJVa9Mq2fjbIv8%2FLxXsVhgTvGphodl6qREQt0KLwhcHW680Ce4ylPyeWdw3LsCUsmIy4QajVeeCx5EuycWKQKjeDP2pVp5xFs7PHFCZtOAVPxEhMVHKGsxYXzBkj1ASJYOyuaMvaNmdIaLPL5L9%2FLaGtulWG%2B5wKtNQad1Xs1vivCn35RMWCOeHmbPJGkOMqgINIjIMld5Hq7IUhjZmV%2FdZUc6t3TP2sluGImirDydWEVqim%2FTQAHieuIgYYIeNB63EVFbgdi6Y1pU7Aph6Q4mLY89XDyhRG06PTjCRfY%2BwiHZFrDodGiu9ZMJG0o9AGOqUBJd4D4VLvhxQdAfF3uGyt7PHuLBCXMTpuu8BkuyE8ALzBHMzJ%2BE09D9B3iN1d8A7JFJfNI%2FjgKpcOttZUukQJzCO6kXcRjEB5GN0jAOr0QYXc8oILPKtioKzvi%2BHIO9wPuRL8TcAmKkievS3hskutB9065GaKJ2%2BMzpmsrGq%2FDURzvCV8Ara5OceGmRg1lx%2FSaeDakm5AMeIxMjlAcQFfHvblNyw5&X-Amz-Signature=27c3ef04b494cc052be124063f73b29e1d1ecc19c8741c8e662a622d9a943cce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
