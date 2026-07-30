---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZRFQNEY%2F20260730%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260730T011532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHeE3ZsywmM2RXgxfm%2FsRmsn2xT6V5rI2XzpoLK6FUBhAiAXY4FGSCBD6dc0%2BNHwHXrHS4Oiyrvn%2BxSmibEK0nfkhCqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlwU1G6POWv0pX8h5KtwDhzYDBkWJIwsqzEbg3k8DLzwjTO669TYGjKIUEzf4FTAKIpzaX6Ik0gyQ4BjULDYy06R2BdKTDyeASog70Xlf5OSKLt%2BmRDj%2Fm0cuVtQ1OuN%2FZ8kFpXrOB1ZfCns0BykwhcrbmXCl%2BZBhhlyTgSgWT4BKi3hDsu4S7t6K0RzXYUfm9ZSfGqi6xsriKJ7Q9JAQPyowhW0diDfvWJ43YZMooewjisvdm8JtpL3a8AANoDt%2BmmikxEGS52c3vNwwTfNlzBvvhse9472d6jAfyrhyCDcfmNsprfAO54WIzZpNRer6LwJ49fFEpkZl2HZhryBs4rBH3EkJpHdZQUeK13EMso6FwIGPkGcqr0kVA4xnedXqoSsiqEk6S%2Fm4reDp5gx1Iw64oGUQY8YcEiNb264fvWW0SSoLnU13F3PE8JxU11Y6T%2FhJG1SuURQRRuz7KGaKSBpIzMrGvkAQhL290cAkFNWwoTfl2ANASmfjF1Z1bQTSCGpWCmehohHpWUr5XdAsc4a1gMwzfeJyOouq71C3dMcPiAd1lHuOnw%2FUO80vynuOqVRCn%2FCSsVyiuqm9IV2e%2BRUDGNs4MO6z0vkZKw%2BmbZ75H0124dl5EffYt38a7LGsJ%2FKvuMCKND7N1oww3Kaq0wY6pgGT1Z%2B5gOrj15YcY5hNsKqKED3p0Xy6GKMI%2FhMR2cqzI92ORdFHwdJpUlbxXIme9MkT%2BfH4KJbZ3TzJBeD6YvXqpC5wDAo51oX2%2BSUwGHGvId2DH6wZGtW0dNXTtOymS9%2BaHZkkojoRG64iha%2FFQFtA4RTbvS%2BSsAGwkbLBE5%2Bwgq883i6wxmXQZ8ZAHQ4furfnqfGKZu4CJLuuMqo7WtRsUFi4gj4x&X-Amz-Signature=f869387b81e92f10263cae1216c002c2ad5430f3827a02dc0c04916aadc47dc9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
