---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666APOX3YC%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T203257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEjT5kK%2FT9bNsqFQIKjsqwWTQaqI9N%2F0qDmnzmqLiCYrAiEA4mX%2Bg6ey3fxCZ2S%2Bsicrrq8jaEK%2BG11T7N2sF19FqWsqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNDxc%2BpX%2BuRKKO0aIircAxrMVfBcb%2BmYSRgKJ71UcRmCtRPnaid4iKkeWn6NpJIEJZr%2FMAC2GJr5hYbqP%2B%2FUgsfbWdFdAesvPZW7yp08YmMZhtTxTuPtGTnTQWSZh1YVxYeTQt%2BZzGWJ5J0agPRgaxtzTZoOJWWyPWXZPwHUWxq5QuMS8rAcfthJSwz5Ds9duwBf9whPjYykZeh%2BS%2Fkeb6wMKUBtTWQf9L5w9FVC1%2FjaErQed3TJQCn8%2FHiCSdJjXRoGJG8YTmoziX3m1783OwuPx%2FNI2Q%2Fr7yOFTgAzbKp%2FoZHVBoKMP3xY30COc%2BvD1pdfZqbQzVGsjceduTnPpQ0C42ZJD5WuKKRdVrObUXP%2B7wp79HdL7TynMi6pcoQPBLnOEo7k08fwXslVrBp5JEiq%2FakVIlsB0mclUl4E4SUPQ2XVoLiwFHafA4TcqZ5G703WLeXWzgtlhZwZJ5GQW4Kyr%2FRekRWCsjEmAzG7%2Fx%2BDbH31VaapdAhACx%2BQw7BmFZQ2shrV6CSfHHtzphpT39ZrKxLc3zK3LGnwiY4NZ2edhxq2Je0YvOhpqNtlPR%2BE%2FrKnWi6xP166%2FKNx9UGTGKyeWVqy1g9OdLHbemqMQWcjlFLi95ghwdnPJwflXgjr84MxMMaBMs%2B5pSHeMPHR7dMGOqUBxHADEygCukX0nwZVDFanuzaMMa6isGBsQ3XovZc3fI4XtIT%2BFWlILJByAeqIgEJWVUcv80DP0gv%2FDUunR6jr%2FhmlMxhIOXIJIjA8n7V0EnWdWs1p6oo5ROCTTV4OVHARveu6waJClucR2eMaALJneat8NsdjI6tj86QgxZOalTen6ajGJN%2BqsB3unI6bGYPYrFY7BpJ%2BorK0ArAmtDAEjgyuyjeT&X-Amz-Signature=a69fdad38f61772b585234593f9fcb5a6f9e1618231598d76a03adb427629ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
