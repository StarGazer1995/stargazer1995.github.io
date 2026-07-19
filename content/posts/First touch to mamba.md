---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAHE7CU3%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T012335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCi14lJ5ygAkd36Q7%2Bq7F0ODX1GGxdjdN8sOkQyeOEFBwIgQEGFineCC7YE97wCN%2FYJIgwjgX5MLJEK2WSBsUGHGXcqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOEwKH87negFiB63gSrcA%2BYzSaCd6y3%2FhlarZAAMTrHtDpYZxC%2BW4ibxVxkrev5XQQnVTIUR79XIMCZTYxuowsULVrzQ0GFoBmF%2FXvCoXOFpPjNWT3h8A5iKZRRieydmoK75L4k%2FKO5fgvWEXfmEKKHeXPybN%2B%2FnBYQ%2BShfqaZLYmgCISNA%2FI%2FDqITJ%2F7yAOescBmB%2ByP%2F%2B8JAXvsz0bmltozWHVXziunyZVG2p1%2FDHQ17v8jge8q2HnvxOuVcDSuVMI61TmO0UUqN18uL8LFm62yFwGJ6kjvAcyfxFbDmp5Rm7StjTYbtz5YA%2BXPyAB73%2BwCz69stM%2FWgBMOUPxw7Iv2vxAhR7mYDShsQfoYhrX86Ywk9FfGpDJCSEoHKZoUU29waD2xpuFiQTb813vtoQrX10WSA7qwegLH5ZqNtoti98KGy9Q%2Fj2bOKVHiSaryClVVXDeuEFpRXarPBhRp%2BgleBZlEg%2BbCayrKR0yNvVdAj3FOJLmgaTMupPq1P8yEjhFeoFDDma7XZ5ZqY%2BdODqFGQ%2F054Zu4evW8Vwo9BNfu05PBR0Bu%2Fft%2F7EPIwj5qYNxpdXW0s2a%2B7KmlZJf1BQXOygN2Rec2NFuMnpzOyJyfGMC84IHuZGQ4DHC3ca9i7HDCZhzNGiNBLJaMPym8NIGOqUBdwyUrYKQFPcYdJgYQ7g%2FjU5HR7fS%2BDdrIkLHhn3gs2SKEKw5SwWeAVlnJEb%2F1ozLGeUGKzK%2BNGuc1YG%2BZfsClQU37lP%2BWg%2FMw5JXBXXKB7IdYeh1Q5E2Xyv7%2BsTnnIOSPotlkRzsfILagO2im4HOe421PYgwS000ELUhf4A0TwCt%2BIXQ8%2F0KF9v1y1NTkDUpyIQIvUXupHkGWNIYxJiL48qwJcwD&X-Amz-Signature=f1ef703106645b11a930bfb181cfa57dfc2a835c32f93d016af26ae4df67f79e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
