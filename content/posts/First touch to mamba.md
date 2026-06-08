---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GOYGF56%2F20260608%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260608T195936Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrPFTXFtwTw75Wq%2FkIJ6gYy8Seb8qTQstKn9H52ka2FQIhAIpHNeNIMe%2BHpClnqfi2QGE52A9Y8Tmd55wEqqA6IfpBKogECLv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyTty%2FhvJOhv3qeuYsq3ANFlLHwMqt3dofETiRSvG%2F%2B0dZIvyNxBMSx3ScjnOOooKjyY2lrDQluZxaTdrrC%2FbDGnDeyux55u8FcE2Ei7cSMQCz3n2rVUTP745BF4n9lleSBMGt4YaXJCNuZmlxwLB%2BNrLPFdZefd%2Bqag8HfRvWlFTbS%2Bp0m7WW7wc6sKSDkY6f14SGmrmqHhM%2BuSkyMeyl6Rg5YuHopl9eJcjkBjQHHllXhsjTKr344gQ47kFomi3SVDdkd82DZfxwA7Z%2BdOsuOlVlcc%2F4JkKgVMUmhjJrFX5hiNMFbWRzJLbKgoEZjcRVKM3e%2F4xWbi3DqsZvanFIdSG7%2B8RsUHPk%2FPXqTMamqFaV9T5v%2BgTeQWO%2FzepuGyUnc7OiCcsnd2G5K95xYlMbi2s3KjEy69m%2FeYRkbN6C%2FNv4HgINiMp0UFWk3%2Fdj31Ij%2FcdS4ahMLFThwIggUUjQ4wy2xkTVyP2IYrZeVheG8bK%2BNHl%2FwgELb3Idvmb82gJInd4Br3L%2FI1F2qG%2Fte4QHMsePjY4zX9TqdUci9WlOBzAIhZx%2FtMgk6bcHMhVXxeEnqbPlDSlQi5owP%2BpZvVErhPPoNePOb7aY1Ao1hnEVaWJC0%2FsnW1A6Qk%2BIQWW%2FsWstg%2FMz5rQ1acLVDSzCb%2B5vRBjqkAfsVVjzzFV4f7NHLTi%2F4FBJ0VlUliE3BIwsBr5SG2%2B76otqhwR5SawkuvTw2AcwdmNAuW66a9HgNYtmtqcZN8onBi273O%2FGMRWlUq0KaT2tMFtmMwIH6o2q2NdXdnQC0nIXKaMVQkXefT%2ByOrkMpktksOlU47JJ3C9Qf1BlHFp%2FRaQD3or9if%2BoPsnx9WkgRD9nexZoEBUB%2Bi%2FOJAgBpWX0HiwpM&X-Amz-Signature=a3039002b743a6660153ebac31ec8b1a470d7a02833c3e29e5e1191425801ac8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
