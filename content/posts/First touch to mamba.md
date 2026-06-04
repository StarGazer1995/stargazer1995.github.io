---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOWYIZSB%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T230052Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIr1mPNPh39z7pmsWIPRQhdbTYdCccZRC%2FEckFYPgWYwIhALDyiP%2FSrfAPkL6Wq5p%2BNn2mb8SDzvV1SW086ifPlIvvKv8DCF8QABoMNjM3NDIzMTgzODA1IgzY75d9oH%2F1jt%2F8h8kq3APY6OKpHSymbhphKzW8kysihtdtJLkTcHl40jsfLD8UIb3bFgHma0N2NccLAWEx74u9CeM4QCLzUWEwl8FalydM3DMIdvYKAABBNDYVZaiaaq5UztJttP9LfYh10kAE1JNJWo6pYOzrZJ57f1gTDHl26U9r3nHUe3j79VmKuYOgfrKSFNSK85ImTfi0hbdl86i%2BFizBZ1faq%2BIioNGc8o5Hzs6%2BD4tEa2yhg4rbgZW3vNuu5uapNpZCrtGs0PW3umDcOydyz%2FTHzCAWaOPahXknMdL7R46q9rWmj5uAV7I6I6aQ8p%2BUpmLwmVPBSsU0D30%2BZw3Xp%2Fva%2FPcgUU7p14ljvww5ymmiAZIetqIxYhrH0VNXRSLkLWYfsn44MZuzC21m2s%2FDtSmrjIrjdjthI6wbXCgMljVy8XrrMcSV55zZ%2FRB6wSLfxmhvKZVZQKCq%2FhOzuoDfmEy2Pv7HuyjwUmpM4ZhoyctLWzHPE79yDrjpx3Al%2Br%2FgeXBQ7uD8jEhz31lSWpR7Z4fVXOWrOdnSV80VPusX621EwJNHKvYgGqeC%2FgrDN%2FSek7HpiBrtLjZ8qEZ%2B7DO8QJa7cX6KIsB4cbrYVluX2McNOJAL8Qczq4t3%2BJZHPrfSfFlbvNGpCTD454fRBjqkAZsLxkkSOKQA1uIPup%2BP%2BK1tq91jsZCbCuIL3lWO8Zi8iCixxgXTzrQ%2F%2Bh%2FIqFWytKmkaq1l2rt%2BJU9ikAFJzcuPjrE8kxIOMPJZbl4N9jDwkp8xRVSCDBwMSasRVyRyM4p%2FcWXl8AZBC4p3dC1DSV1ou9I0vG%2FQaXuYi5eZdGOcIHjWxaVZ1XggSy%2BUJ%2BW5ilKE1D5lvpvodEYeUVWpjQKJT%2BFN&X-Amz-Signature=efc258221280000f78eaf1ef2b32037fc3433f649acbb381a0f13eb48880729b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
