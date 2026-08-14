---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657CE3DNP%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T184555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJHMEUCIEpFXBjAB%2Bx%2FiMMAYw8YU%2FeWgM%2BPHmdOyjv4fHzKgLUrAiEA1NGM1QYevr2lxxIfqplls%2FoNDJ8kXQh5%2FdwZwsoTHmgq%2FwMIAxAAGgw2Mzc0MjMxODM4MDUiDJTBLPCFawU6c%2FXpnSrcA6exHoKc563ucbh8HapsnYeVvzsWGfM3ako%2BmZpF8UuXjdIuzoTvQaZTSGsnL3SpOuQVAM8WypRYd4cUsYTBwPbSkBfDop4MyleER5GsHcYtG4rmwJ9qlTyrqCXrbTsv7I1e4dQ1sB5tvB2Alf3Eq4h3F8DZh3ckuWqVaKRk%2FNWIRovK3N1JMytKVLI2aHgEqzhLOcjqBhxbWomF6NuEc9mBLUh6WpngApiomMT%2F3zfIsvWt8nG1aG6ymUE5ZZCJ68ex190UImbCOi5a22ponafL642JKf6FC6YP3KiIi2ZBrj4CyofdEIOqKVP5fQv5lTIMgPJfJ7sG0ul0I68NAq33%2FrKynrYFPGNJQB%2FBTpXj43oiru8y%2F05RpGIakz%2BubucsFtY2oI00cRSZEqh5H5Hh0wersbEKPEZ8%2B4hwvbI9Kq9Tj7w6n75U5KscNCRFmdIH%2FFY%2FT0nXEHkhnzx71EQvGzHfTnSKvzxm%2B80e4sTNQB6rGNezeRCN0z3OdPsJIoMizmMyLMwwiNFXxiqBSYBZCELtyPkXPe2Dli%2F1mHuDNtrMJGmz63Q%2B03GiC%2BIHJDlQ1%2FGfUvmZsu%2FJhhPBqMy35N8%2BsfZQh2S0NAmx6I45ZEoiJhx%2BzUWj570JMKm5%2FdMGOqUBEXLeRH7IzOvol7WyCS%2BBf3uF%2F8G7Dqkzw4r%2BZZUtOodLxRW8yht0ckEGu2cZMQ4WEyChfSw6Qlnb5A6ZhFd%2F3mT1hilOrs7ufg4LvRMwwOSNB0Pazk0l6Z5H3eV%2Bjd7VjcxVXvYfXRnmRHlYgTR8xbAccfqFvVUju2xZlMdxZIP3OIhT2VXmBenWy6qANvmVRL9cA5PpVPcxBVKvnsQ67pRe9EYl&X-Amz-Signature=d13254409e200f031af4169936f17f381100515a256bf1fbbbcd73ff96cbf454&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
