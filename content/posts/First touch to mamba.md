---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKUB3L33%2F20260705%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260705T055411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGkaCXVzLXdlc3QtMiJIMEYCIQDIOqD11D3ycZxHECYz5qqMvcCcf2f4yqdqFwYbVIrqsQIhAMrl%2BWYim4ahScy5HHzar7AyY%2Bxk5sCHzA%2FATmmHEXuXKv8DCDIQABoMNjM3NDIzMTgzODA1IgyjcfYp6HpzTosgrWcq3ANn0eDHsaMwJIekqh4NpIkmzrE33neqWmM6%2BB9tNrQA602Zj9HQyi8umldqpK9hZNzsBXf5OuXrjBpd87Jy%2BjpjeScNyMikNuZ1OYKv891qJYGWOaEYNi7%2Bok%2B6Y%2FXLldf%2FltgjRVowflYCLQe%2FFS8aszYR4Wcql432ITJ1umJV87LAjyZVJSueWB1R6n1HeyqF40aEhu5cVMJY8NI7D6r2b316a4YTAoyfkQTekC11sxDVliR6SVfkXNbmw75EfV1jyVfAk%2FGeCcb5lrrUpIIVaYP2HR7R0%2BOjCF%2BxZVl7RAh3zpKEJlCHSJ5c%2BBmlOmTJmw5JT3wQjtK37eRCzzWpA%2BIreSYuamGosS%2BpT8NZhv22Jujr8jbbde23jbNWJlgimNKMTM89Cf%2BCzZ7yXCkwZlxnPG3j0ON2dS4UdQCkGTy8dcW54gfMSGccqLmgUn0Swd2aPvbIG8xCWOXf4RxwZxP2nTcsgopYbVco3cM%2BawKwy3xswXG4hm8Cphb39%2BgAo6%2F%2BvKY8DNrDuTNSQC%2BADK%2B7kMmhqz24WTbHM%2FtmQEibhO8663qG7ldYX%2B6lm7ni%2Fbyb4nloJp0YIRNHZuVWeA7AVDlQnzv9ESwIfGu2SYTg1Owu%2BuCGB3PKEjDV2qbSBjqkAVdK3mcRsdVhjev2nk3kro8ifdbnaDDyNz5Ve2iNKh42qr%2FJ06nGSxI8bUBsjChddAuG4OM3dtneY9zvYjOiOgoj3VzE93fbccQC8Aj%2BJviGohAVDvCriTKz1iCE%2FSs2Z6lqXzuYTJDBaKQP9SFYhsgovbQA6DSHsPT0h907kgPB6e2cy0HFIp9lXrFQt5CtEHSedZXLXGbKN98fE3d0ZnegmaRz&X-Amz-Signature=a5290f8c6e8e4377f7259bf2e0b3dac9ae8b4ee0191566677db66eebda8fdc07&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
