---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYBVHQDE%2F20260612%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260612T163814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJHMEUCIBGUSz%2BEfjDjK8cBiDpcTFYwfo%2BF5WefFj2P1yBkJvrAAiEA6%2BXEQGQDsNG2nn19PFiizmp9qWE0yPtiGFoENoqYQkkq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDG2GOjSXhOFlAUEw%2ByrcA7p2y0%2BERVEHikd2FoMV5tWTcJfIAcJs1sRHEY52HmL6RUdjBD8SQEHSfWmc2TTa94KDCcqB6EkvqHb3%2Bck6rtSdXEn9IihJ2Tsz2hAkI5lTAtkK%2BBYZqvTRDh%2BHeghvl84Vrmhjunq59qJJDgHnVSWzTGfm9lbmsm%2Bb7laDe39ytcLGng3%2BCYXMr%2Bgc4F0BHrLWWxl3rfNifOegbZ6TcTkeMAIddzGix24y8tWWiIbibFSVGup8h4dMK0TIcxkwJqNy65eRtuAioaCsqFrLtyyaB0FqSgaG%2BMWKtfVL%2BaCFCNQ0Z1kqpGR6oPBIBMwMsSfQY1mQ7dDp3KZNh97XoHNvE08%2F62jP0cWdVoqhxwiCGuJPqsMknoUmZjF4PvS%2Fni95KlOOCoCZ3Ir60YZq5XVGSACJOiUyOgDQo34oTxYf20xii6eb3MxKZXNU0mTyyWFZl1M5FYHWjlUN7oBWL6aa1JknTjKCpVcu6wZkt7mQ2moG%2FHhMAOujZGubbOVWuWu5D%2B2jBx2D8bfAa0B02HkwIzAjp6sWwp4mMKtlVtT42tBDxM%2FJuTr5N5t0s8LvPwrlliiXIRlRtkr9TIh37C6eI2Y65p2WxrHVMY3K7yN22PWA4AnidYNup7DaMNfmsNEGOqUB2zc0RTlk943Dd3dAJOutIEN%2BSrUceUvCSmYtOcP7vwqfV8gLzNZD5OPTGlzjjd1nXkcW6SjuKuhzMS0VMqqQ1wzprcV%2Br6rPYxg7N0UfsFbsRDFUe4jrZIbp5iL450%2BIpQbMibs5Qw109fua1puVEX%2F%2FN2IXuc25z1cxOEgJrCTMA3sMLN9fe296CMNVSa%2Bix9K3%2Fmwv64Qf1DCw4nn2pNYSemZl&X-Amz-Signature=848359f2d2f688e6410216de6597133736b1bc4d017d136590c420680b915daa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
