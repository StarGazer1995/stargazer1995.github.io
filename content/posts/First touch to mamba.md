---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ZMJIYOG%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T232637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE4aCXVzLXdlc3QtMiJIMEYCIQD2ZypN%2B4dPg4SEkFPHtXHTDXlJEYyjaeCBMdgzaPuyqgIhAPO22hZ0Ztk8mXMoAR6xoJOGSzZZ3hNR7j25permQW%2BfKv8DCBcQABoMNjM3NDIzMTgzODA1Igx%2BGx8ENYEW7yPyyL8q3APecsdmj%2F%2BwiSRRq9GNzKEqZsVOeXRHGewb%2Fgnu12hWstq8DDXkuVN0aPUIMBANwaVHAbSYZ1EWZge%2BvCt%2BwVXObOv1534XSB5k26j%2BbDP37xVYM3Jnqox5PVWahV2BokXvjazfJDI0CvlYgB%2BUpNAb4WJLK49tjTC688XSt2Rq0VaHPMMSaAkiU%2BLnzRqTsNCqeIstr2ZUrDtVoi%2F5kR4VdDmU6mOJ8IaCa7haB7lgb3mwxHaPye4mTDkc98yxAEWANZw85WWRnDrX%2FxrKrA8SbEsFmHVf8WXEBaqTVGDLcWUcyGkSimik9yINrRLcDkFDYgL3fdK%2Bt1aAmQgFQjcHuEAk3VoAZSXbIrnb%2FXGxj6BnKGdkphi3hyd%2FHTvzN7wC9D1lbaz4Mhnfy3%2BeLZVdjWCi1r3Ka%2Fpeb9SRUklxf9TDKuakxgJpvAWRaiwSQK%2FkiXuCYKMbbqVrcz9wVuwdrZWrJNtTIl2aj3nJCeu52IEhnSKRbo0PMZNii77s9HsKre8LhKcNyZxyB0%2FFLUhc9DaxzGGlsynZYhGVfw5BrS%2FL0ZU92OXOs%2B0Mcy4rjIIxFtvtE2c7i%2B1kGdwzqHJ8hjY5Zl5xsAqL%2FpIN%2B85qo1BnNLZEjJckjVWVAzCjm%2FLUBjqkAc3JZrJAz5S0zPa13tfZdolT6hS8fwHr%2BIHBfNByHd2LARyqXBShjG5%2FZXyOuLh6YkX6JM%2F4SMwZoqI718BfrxVbAilffn6Lpowig%2BSCZG%2Bml8xtQcrDXtCb%2BRp0lmjfwAMz810MwGP%2BPqLkhWdantEMCJ2Orw2WB%2FUGduTh8cSyppxGHNsdXqijmHYA1i8xptRStXcSXgA69QmqjSve%2FWY1mKxG&X-Amz-Signature=48dc00f728ee8129f90a347dd3125123906292f3bd97786691032adb9ddb0d37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
