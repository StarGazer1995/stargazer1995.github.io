---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGZG353Z%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T230110Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDFLERdrIWk1rW3CrYURB0dJCHsf3PIbk67uUWwLLYWyQIgMBw7cAPeRJORGghITp15%2BXliRizGQ8fbS9oFqcV0ghQqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJkqKb8YkQQ04eL9hyrcAynxqmiqdj4MWEl%2BXDdPfECQcmj%2Bpo7llUrpaaM%2Fk23JV2sQjS2wlmMF9casq4JvalCjcGkkQfNGU%2BS0cFIyMivy1hkn9OBabyEeVqMWpUz%2FG1KlSv6KWlfYC%2BK%2F5pADDsIGNUPHoWrYPvwjDY10KVYnO4ijMAlI4G0NOmVs8HjRg1Y4LbMrvVOM4F%2BnquIImh3ZHYOoDVeTm2MoFIGrpJVSF%2FHohq5exlz2b8aV%2FXZBFsOYJz69Y5t4rNuaFBoZy8CTjDYKr0V8BMwF0n1B6Ji9pnYF6Xhfp7gHI%2Bkv0Rsqb6WxnZjfBOgZZc5PUMFwd6%2BFIJj3d%2BAAFoVk7WDABMPWs7bE0Tao0o4wMqLn%2FgdKMhAJf09NlNmOqLdjlSLZ7VkTaeHYo36khyC1IwxYCNkF9EN0Ipwqo1yrkQ1NJP3gpTeDx25p64%2FbGGOlv34kCL8gg7qtbpMQOf91%2FePJQgC45V14e5fMcpegcuoKnviRXm16AOKbe8sGqPbM2MPJKqt2F9prrf9XVrDcCMdy7Zlj02aSLvJ2T2Qr2cfjqheVed5VkgSkUXZjb%2F3068ThsnjA8MYJxtWRvYfi2TV8nRgVkLWbMS7km3XAHCDIhrHjRe8sVlxD2buk7t5kMPzH2NAGOqUBfGYpkdM8kFE%2FyN6IjkkIzq%2FofngVjrxE6p%2FTOdTLPAvv0jqTrk08Uau5%2BWcOtonUoJgzE9xBOepyutbDF%2BUY%2BZP2UrSDi6GvQHdmAbkU1QTYAA9EFc2V526x%2Bb%2F%2F9lQRiUjtKdQuiyMo6g6WNcq7UbXaSZPoWyO8%2FSjFHNY3zQzyBAHOcApphokM%2F%2BSHNeh%2BZJXb8Eo3EgpyogEEymYmepYjerK6&X-Amz-Signature=4f49051c32a8a835b227b59015ef16b2d58a1e1c781622799bd6b9dcaa43f4ca&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
