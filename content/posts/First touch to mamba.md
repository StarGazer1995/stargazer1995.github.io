---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK63RS67%2F20260808%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260808T221700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG6Ps%2B5TXMiptl%2F%2F11NnHRrHmPoGM4%2FzKjfXBGjey%2B%2B7AiEAoKAipqtWCPgY6R6fBOpSmunAQcp5Q5DkjpNc9Io5gTYq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDHlR1xGH3EDRMsEa1CrcA6wO4O8%2BtAUgKO9H0sUCqyvQzweRGMOnJ9cLsjBPWbrjY0xbj4hA9V9iIJz%2Bf8ZB7SUr%2FVMChGaXSymICoS5x2HLzuhVT2GFOwcmcSD%2FK2DEQ7I0hSS5DvXld1IYgT7Q2uHwl%2B1u8FKTdAuMbqP14e3HZSTXG9olQ%2FAbmj6inQiwy9IG36YjWObYrZGLs3l7pWXX10Qq7qkcvxaA26TndDh3Vyi37pG%2F8u3vJ%2F%2F2%2Fpg3D0tv%2FuHWPIMPmSr1vSiRIKNMWE4E9fYm43hIJgF%2F9m%2FpmlNJU%2Bz3qBlmkPPRTI5eMex1uxy27%2FFFpy2fUsc5lAmVNmIfBAvpJ1kxznVYL%2BoDO4ZuBwCVMCJYgvmFj4sM0EI4sW9AyOyIYXAQ1j27NMJ28ErtloKnbJojfvTnFMXTTTaBrpmNoE7mRRICLCI4YOgmQOx7eTQsTmCdipUSzYGZ0MVFz%2BRe8XiTy%2ByszRSZhpPgNIn0cc7z3ctYGKFsx4%2FglCmGdebTXmE5aASzOPrx1EyEEPFo6bU1sdbaUj5%2FNd2WEV6qELz9dP5WMsLQXE%2FLeTsnzKTE5X9zqVPPoxk1uoEQZdvgweI0vVkPP5TjSv4sZ3Kl%2Bc6CUUDNaSyGDFwVOCnuaMq0wB0DMK2G3tMGOqUByszas6eiKVvvEI%2FxbaXVJL0H%2Fcw1WBem6PEN9NImNffVpssgNFCtRayInQj8jYprnFUwyhKUZP83ZxdOX5cATpmmSe8%2B5Cl8qK0TuT6a254XHKQBv3ttwdnRgzFiAI66LO42Bxft%2BDl7HKCGJgeuFUoqeZxJ4dcXjgq9Z75nhNcGpXcnLY2XlgD89zHrdRsuotdm5aqsEQNkmwPZsjplmu3pwRNf&X-Amz-Signature=3604303f94cf9d56917396f0b9810e689f85d752188db84eb6a7b419239d94cb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
