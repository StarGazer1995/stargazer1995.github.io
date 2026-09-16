---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QIW63IT%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T222817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJIMEYCIQCPkKIuq6Fqs0j6gOxUo2vvJUBtU2t8R9Gh7NJOqz23awIhAMuAqcLed4TiDmkyepzpoQVqd2ghAofXTPf%2BHOu9drS2Kv8DCB8QABoMNjM3NDIzMTgzODA1IgxeRi5eYcHNAiHauIIq3AOkTWfUVAP5E0hDMZiWXX%2BbQEc451i97weooHU%2FuSGI7kpygEJhwiHLg6Kxn2lPRNMUGZcNMVgcqmr60bdQUzrsuHOuozaMq2xHB7kwh2T4P9jpSR4EgJlz2EczZtoVtUnSw9OnqRQc5xuTbHbgw%2FKO8oMYerFFBA5L3ORmZmCuMw9vGMlGXnssmbmjRrqF60mkt97vEvoYmKQx39BpI0DN8Xe8YSwUQnRwuaNqVCJGsRIeVqCr977%2FIv%2BPDhKMXt9Y%2FsQjba59ULZS7puVZeMluVKjKrPr7OwthsQ2EkimLol2w7LmnpYEYsfKSX0RFqU2rtmWJmHxF2J%2BdsF%2BSooR8u48LEpQVPamrIVbGtMld3I1d5BNE%2B8wS6CulmskHuwQgqA92w4Odfm7caOV9mgh9TtEEV8avkpvw4Jwfb%2BgozQ5%2FI77Jovpp6yhjgxfTLxyqBLtkYVQlvBvjFJHdB8j2UucaixmAbj6xoGNDy%2BKw6%2FOOsRpF7XHHlugNRPwkcmNPWbyWJjjioTShbZ9%2F%2F6ltawS8e7kp19EcFGAbIlQIoSYJ5SLXZj8EspcYXFbrSyAyeuJj0JvnFS%2B7obgVfKfHrcevltTD9IA5zKgEs%2FdQ7hLCbPTzA%2Fj1zBz3jC0n6zVBjqkAVCR71NbUQnz0lY8QgIivzTikmIsnPk%2BvTqZwYeyIB0p5MlrY7yCPleFp5y3v84AcA3WEP3UeL48WbkOjzAFZWoRcBpJKlsNDzagYLbMe8s90veGSnjBUKVifLsGYj9z12rXea%2FmEZG2dF53tidrWYMZ1I9gSwKWPJH9goq4DGAJKvtMKAZW%2FPju95HkgoRKlSTtbakEWj5rmmiiwhDGabjQJe4v&X-Amz-Signature=855db99483334d830b6f7f43df860b235645765fc2db03dd2e6883308446a7ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
