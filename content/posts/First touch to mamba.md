---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GHO6FVD%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T015611Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFGiQOsZtJaxNWoLFDctmciVdC%2BnY8VzYcisVS%2Btd68iAiEAscqRggYCGYryfb9c5sZ5UH%2F6Zo%2BYA%2FTdpicjhbGuKWoq%2FwMIahAAGgw2Mzc0MjMxODM4MDUiDAty9Stvd9vWUMUoxyrcA1RIHCIHV1EX49o%2BI9goQFU4Go5%2FaVp8SPE4bqZSDWB8lXBRvPdaElnVKcKk2FdnzPoQmKLZTQYPaEn9c1p5IQSGv8aSTG1USqJNX5m39WE4gHRZgdBjuae1X%2B2JXv618jlSpCZWS%2BuYABqV9YtoVb9brDUVUuYulhCkqUZom%2BXRkmyzwGEQxVgBMzcfcgmDxghvLpXlKNd2x8zWFi%2FkiXv1Bom%2B1cxarhgGwXkGQw2aOGbQNEfEFTzgrI7LXw3sg%2FKuvcuZQsdoa8c3i2kgx0ehySJEKc5j6l975OwuhSVC5pJu1KSkieQXWHFR%2FEJnreUJMwLN2mhrFMulVvCdS6ix%2B%2BEM46%2FNPLSrXBiFrCzVkvRElVht7jf2cTIXzT4CGPSr9B09nFowPuGifoOOwPP67dU4gERY4JdJicmnLTeY1Dg4hiLn0o7iWJBF66Xl8wC5iE9TiHjNU30zuVR4R5gqHAi6CKpysoS63WV1Ig7U1kBDBEH6%2BT9FlNw%2F4C%2FYA4gaJ2FyJumczpo%2Bbkc3hUSv1AaVPbTUVXxnzI4BulSrbQTMs7iB%2FjwcxsS1iABAl0gjU%2FMLZ28Ev3PisuBPDPXDl4qvHLvgaAGU%2BTSlPVjowqu1AnATG1peCMVvMOjmmdAGOqUBjGWW5ddYyDfu%2FqJOKa9udsmx%2BEA%2BJdW8NvrqG7edgM%2FlxqPP7jA18ofstRF72N8BsLrmk9l0vH%2FgQdDXngWMVTewNB8JPLVQPICVoQtdb%2BOCqe%2B9MyL0tlMRK9mULCFTbImkRjZ%2B%2BPtcnYHKJy%2B7eooG6QhaE640GV48wFY3v8n8PreUUVWx3rnlkMGNwDKRtaCBwOWBGmlE5m5TrccKpPRNC1BR&X-Amz-Signature=c14dc93be84bb7605e9be7f4f6fa3b8c3fc69d139780bb893e75030b2fd8d086&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
