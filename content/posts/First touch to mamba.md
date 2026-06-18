---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIWQ3SXM%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T083012Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCjhipycBaqEUHKT2J%2FUMJJKLEhxuCUaFOrzxe6oM7JFgIgGYrzH9szmrs2aYHmOjIkSemecu0VC3eOhCPsimHJOYgqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB9Z%2Bk6sxuEZoyD0sCrcA1TjslwD4sVjsmviFDkhhffZZ%2B9NIRihfNB9yo8snPkKaZ%2FjRuBeK8h6hpyBMqN4abAfZGLQh9GPVKs%2FmzI%2B1Zbmgdlrdm1UNrRu2MHE3TXVni6uQaea%2BaY2ADXs42qwSdzmGYX9pBbEz8FVzP23fuD40fuUc%2BR%2Fn5hZS3mcuwmpFFPVmBflzIzQlTTDeDJYaNACr8yNc6iKRHkU%2FQkO3Jjc2xoypuBjHrq01VxwYmM8OZyEnsfTmxGkeP%2BHorY53qcuyFn0Gg5DrLFRv63CFcR5izLFFAO9TKKcAG1EBUgQy4iX5jcsC8FFJornyydzMvld9xAiO7m3vquL0YbbdGEG3hqrSjCo70yZ%2Bzz%2BjLi43092Ebt2vzd9AInp%2F%2FiJwWvlUOzALuadCXEFNEWoDfdrBZSo5dJHiPTn21Y%2FmN7emrHyO2HpRnuRJsxAkBK4shAcZJaMtxAKtjtTooin2FtII6TSF%2F%2Fjo3H16Irb4Ttj9c7UNWFm2zwC2tS%2BhMByR4yx5TvqPacVsNuiXCekz%2BLJ0saSlgB%2B4FR8RtHkGRXE4wH5blD10BOTIiq7J%2BMaZVPnFyXt%2BonwSABzsVkeNeUR8VtrufdKDedMC0QyKB5TxyO3v%2BzcWFpvJKDsMIW5ztEGOqUBX0fgrlpbFmyCSGTejDLe0tVqYl9GPy%2B8sdxg91QoAF9mwokX4oB9f75xWM%2BLZpUHoLSDaz5ZbbESxF9yJCFwq9yujJdYvThAE7Gjop%2Bejukd7WJdvOtgQ%2Brk5Pfm%2BAZT3LZtjLXLOGkqkwOMudiUx470ljR8dxAGrXsZkuipB%2Brz7ZHbDt8u9wN8P5ebHc3aFIIjX1UCVAd%2FkZoTpBjHqjTDWgHD&X-Amz-Signature=43a29b2094d27e6f255ad7ca55746291fbf082de4a4f9007df0ecbdc857c87ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
