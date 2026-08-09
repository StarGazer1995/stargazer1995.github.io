---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWYX3VJ2%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T063602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCosOiIGYhyh6d6tw6qCK1DSl3qN8TfC6%2FszOFdPrkoXQIhALL4X8x%2BH0H0NvKi5UzBKRUDIahLRJNZgnJeNmk4G89JKv8DCH4QABoMNjM3NDIzMTgzODA1Igw0kCXdyaTHZEPl2bcq3APt%2BFNDMd%2BD4CiBJjgWMLScaCf8xxrY6B9wbwOysVvnZAzrdlUarb4SRn5P82LsDjy7Hit75AcTbLFstiok%2BVdcDgOldq3uY8rY%2BuuK%2FaCPMB5K%2BbYrbjLZf%2BRQToPXMgsUcquMEUcf0iJjl450Lp7%2BT%2FCI%2FvxcW%2FDhenwfncK%2BR2min15rECO1ZuuY%2BGNxc1tXhWc6YtS1iwthZuMQxaxqWsuPiSTMMmDLYea3%2FYGujvVe%2Fn0F7rQxbPbDCFMspNT0SYFanWovTtuRYyKDXiYe4bsOJ2Io1rg2vCfzQ0V6txCCMk2mR1Yef9cv%2FM6P9k6kCdxujCw96CwtcisiEnrOxmyH3UMvYHrkiQ5wy4VIPnht7FeRGv1mqXapslL3rXRXjby7oacFjiZxzL4ufF90gxcJyvGSTFMSSDhZTmFodFQhI7rqDtkPLg2pCVxwnD6NZSfJ8rGmq%2FZLOr4lP2%2BRDcpMb0MXaF8jHLrBQIVOetoN6j4m1oOykvLA1YNetmmSTK0fbB%2BryoV%2FCixfFGp4bonU3l90JH362Q7FuhvUGaY736NUS%2BlChA40VKkrZipyphmf%2FftxpW9RJF71l3qAUvMtcTbyyzUMoQeb6%2Fr%2BbUhu8qYy%2FFJ%2B0TvjmzDGnODTBjqkAXxMwfNh%2BizZAZipU%2FflAH2NIpk8eVONP3oVq3zrWnahYp2%2F7efxYzgU9gY4c8nrzdq6xate9paY40PcOl9jTIrG7HzQIv7K03HJZHgc5%2BD6OoVYpwf9%2FgKGEj6GhJyVGt9Dsp8txjCM8oTcAjavHWrIyoxqphyQc%2BWkxbM8WlGoHcVFZoAqMDaNrxShf0YRpEdrnz%2BCn3VwHevfl33LWSuL1oY2&X-Amz-Signature=c05537ae496c266eb4841f7080d3a90e6aac71c2967c2d7c10e7dc8e58a44be4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
