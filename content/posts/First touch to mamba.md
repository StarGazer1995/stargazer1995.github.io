---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNBZIRNM%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T184258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJIMEYCIQCzwRrhu05NqqM4esJKc5zuGCP5G%2FH9uEylJbdELnbIagIhAKlysJXT23HLE2Ib869rTCnM4P534ztSVBAnpE2ONye9KogECOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyzeGLmEPmd5uVbpAsq3AMLulcvDuDs1auk5iUYKcpMhYmHOk4Q1duEl47c2ZnuS9%2BuDfXNEsSOzDbrpMflCsPkc%2Bzzx%2BuOnjk5SrW9OTaNvwC0NmLINPDYt3d7%2FpPPcN2jhWv1AR7AiIZ6o7SWAmr1HgLMxhY4ZBbEbCIdIxLCbLhUhP6lBCVNGyboxn7DcEFMALjCrv4DJhAyWKTPKDAnMaZ7TzneBhSPWJX%2FdC%2F1KRkHavhTsm91g0I3PFgwxWmkq%2FIGoxwgbovAxfyh8auy%2BmbqgCcsCrROcERC0ZISdFylNqGAu1W9Sk6vDGuEpP5FFbDkOUqE0hKZm2CybZJxH%2BrathR89BhCas%2FkwXmBOsXzNQPPDRDF9cOmWKjuYJ0rVr46VxY8YuD83Ws2QroI9osmpJVWkArkFVOuAQgNSkiHCZFzdxMOyr90vdqqfervqwhvNE7YGjnYHLVZ1hCsDg%2BrG9FShUT1BjVFKKq2NWAUON7L809xRyZ2HqDQ2EmomviBRJ%2FCEh7LJXf1CeLLm2uQ4Nxvxjwy0w%2FOZTcSMzS3LHEgznP0OPfIXNvKf6J%2BPT08APc6Ri7%2FTToX83OmeeFQsgQEf5%2BoGpWtrhJJQCW5rnlC9wFeasetmqeqfma8ZtB59ENRxyxVezDe3P3PBjqkAcE1HzdyFgjEn%2BEvV1lBcChOL506xUZTLSP7sWNOHIT%2FwtCvfghpzQFX9lCt0VJa1msO2ORjv6QSBAu8GyllQOTqcFmJU0Zg224vc9zScv96CUEFa7g8STrzepKKSdxug0Ae0tiTjGwxvwbANHwD0ZDL9GtDmdy1aSfzxhipQFa1xRYACgzD6mx4NFwHXKU4D4duX%2FMd%2BWAzooxyD%2BJ2b4x5JQre&X-Amz-Signature=88519a66343e9078c998e42a1d2d4209b72e5b36593992f866e91412153785f3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
