---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVNDENU6%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T015730Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJGMEQCIC8uxulFw9N05VQjUhKijpyjdIYLox%2BdBov37cwt88ujAiA1wC3%2FOxHc8qqKmmuukvRR3n6yMWL%2B8kX4PKOMOwKvDiqIBAjZ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMigPc1UFj%2BaEoRgPwKtwDqcWfR1wKyNer1kL6uZonioGmsHkKVXylQJn9KmVa4XMNgO67xPK0lLx79kXWLoRo0AtZVwJc6grx3THYYzeeDoexQ%2BBiI0y93OlgdCuatm0wgfPJS54RD8CpTAPQiK2KZ9iL%2Fi8dQlRgiSFTyHzzkFwleYNvoh0L9aW7TAE4UQmbzEhNkVERMzC3wzYZl3Q2r4pLkldLzWTPV4hD65zes1H2dC15kQg4D69RTggQoTfxXQ0VAg92%2FQn%2FA%2BgHZeniQTPmnUsH6u7EKQRpeJaoEPPuqd9zfsjoCZdthpxF%2F88m3wkSfqL9TdzFWEXZMBuJ4T%2Ff1qqm032SCyvqM%2FDkFAXJ9xD0v%2Bzgx3raAWbueFyNW1EXVL0QgfYQ1dMvbW1GWupwdec7jv2DJdhEhG51GOZIzgO%2BK%2B9u6Lsj%2By4Xn%2FvrcepEUk9jAMk413QuDby%2BPbj6Axpi0xDhGGe1Aetnh68zuqC8ywUQZ9eB038i%2FYfC6zMp5LdXDfWSD8qi90G6J0D1oZiz5YeKfShWWEXBZSxtQc3CDqTeje%2Fk18%2FEEhs6AT3uwxR1Z92JRwO18kt6zjDnpemB3I3dd86wztqbndbewfgBb500WqNNtjNtA%2FPMC48CEnucrefAnY0wkMrF1gY6pgG6%2BbBBF8kiarkh5m7GMVUC15xiz83oGmgikcSYimW7fV68CtIRpImCllBguSYjNh2QC2hOwu19CLISWsnpw0rJwVxrRZOLCmJtVGPWdVhBMy6Q1hHiAgdwJCJgDfLdp29hdD51Crm%2BQHNVDIPJVd76sML5ZK4PtAQ%2FCs3rCIH8CvEAjXjaLzEU%2B9uU5EDVP4Bu%2F6%2FqeU40gDpUNNulmI6x57dZvHQ6&X-Amz-Signature=5e166e94220e44485cade6de3fe7d688d84ae3a80e4345ea46445bb9b53d7624&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
