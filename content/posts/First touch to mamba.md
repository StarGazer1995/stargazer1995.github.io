---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAP4XPPS%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T170626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQDtmaQm1erF1N4T52Nx0ofbdHIPc%2BDCj6qten7HDDDEbwIgecD7DkNqrzXqhENes3qBBMR8GYUdm%2BdEoMYX4ncSxUcqiAQI2v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIBnnVyvPZXV4n4LmSrcA2zX7%2Fze3AJNR1ZZPeADpQMQkd61e5xCRjHlFYIZithBXZqarRr5ferNHn7%2FXpb5so9%2BMOlzY6RX2P7d%2BwGJNYrIb3AoQfXEBlzbuCazBabAbdQ1XRydzNJcFc0mDM4%2B%2F1CmqdiGyGOS5EISVCfLbgXO4gKKeOu97IQczwho6R4vj04kwwDx%2BWSpHlgoCxU2HsCF%2BE4%2B%2FaiZqM%2F4Z3E%2BdyS8rW3k4%2F4JSg44PFbr41672XrrpcOV%2Fa59CEOjvl4a1L784n%2FYTSU3bxFaUmBouxoQoR4nj%2FNeTXrJP5jsmMfL28jYXv44ACz%2F%2FyVdtxSNoJ6YAFhqwLUHJS%2BDtGsPnSXLm%2B5z2dMxYAFd4D7uqshB0t1VLwcOUa7E3Rsj6p%2FleI54quaUxFRy%2FUd1cEeRh4DJVI3zTzqjwyBMsSjJwZ84OeXfQpYDYaLLMmCMhJqXWL8Mwvr6cxrktY07NuWz2PTmFVEo6v8OLYafthwSzIPH%2BMpp%2B5dp40a%2B16nlmPnKpfyzqYybyxFZ9XHyXsmrYGYveI0qKRShm4y1FCONd05xT1LmDkcJTN0FJqxAIyOu%2BwJkBIv%2BisUmzWahgWuC%2BHpZClffVdh2uMGHV%2FB%2BijR51KnGWPupd%2Bfe19LyMJ3ug9MGOqUBJJEaj7mTC4MctXCFw0HqeBZScRuqAx0huyPgagDoOZffVEX6eKVUpOlFi93AmW3%2FG0tihUXdAxNfMpgnqMJkegk2hMw8jw1BiXx85vTxYao4qbZwN7v%2BrovGFBfdnYKYfq3nAABN5H0kCAT6m4qA5agHBVD3GUVwOO4ostuPbotWAGXobiiF7FiMpUEOKUKdWnLeMyAod5GS9LP0Yfi3emRVYvKH&X-Amz-Signature=e60266f3f629b7f3230699b0492cb3c9b4e67125c8be6b507b38c25706dcdcc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
