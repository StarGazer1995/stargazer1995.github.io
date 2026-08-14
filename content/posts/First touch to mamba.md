---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX77V2KE%2F20260814%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260814T005640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIQC%2BHsx9n5M9EFDfX9pludL26EuUj8qIpEiOp%2FEw5YNoYQIgRo9LKKEaZrQTnl13%2B8%2FjRTV2WM7wAywrPLbfzYEoBr0qiAQI8f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLFKBmwi76V2VjoMVircAw4TUDvXMnMf9OB%2BB8dgT3b5baT6mwoNIzRhioRBZkVU3uL5Z6Kr5aYsCIZ2TVOVysBz2JFL0X3ZYLenaalHi72WOL3GinaZ8JY3WQ%2BJPKBK7wPrwnPFsKrwfkTwZSkU%2FRWNaRb1CuXXFXnNjk1mZxZdLFgqzfAfaQTBWAHyu5LI2sqm30%2FPhjUQ8zlQttIfBv%2BqW%2Bqg%2FN6ozyDMhQVoOVMXMGyBREZJbeGMj4p81FGwAluSehHiHmDd%2FaTmjn9%2B8FT8ayDfbjFwfm6uUeL960rz%2Btgo07pv1g%2BAbZTH5B%2FBlQVsl2DoA6cY94uH54dtl85%2FURrqtBFBB2ybOygElR5K%2BEIWKYNpPZ%2B4oIVxsHxauZ3XTNvrsWKOjjVKEhlJShvi2e9EAA%2BDCr2Ceb4vS4cXE9aAMK6YwDdloHt7XNZPtm3ao9tDokVXT23coXHXuEaHt%2B%2Bvpy3IG1JKJiOxJ4UOAssRVS2Fd27RYOukqEF6vBtmYIsACpMr0O%2FTEkzUkN7eLBaOqG0GgdSddkAbal9PCWIvBjqTt6qoEallsjCbIlPmiyWXTJmC6EdduRefhTO9Tn4VQXo0IA%2BkXoK6mhsqQmcoLgoyO9c8TxGLbZ76KvW4Rc6%2BTiiEUTz3MJKy%2BdMGOqUBDA9Kdi4K9qyKw45M7aI1N95uzP4cPLOTguVfMIHOQQoWuthM5lTBKficVCavpx8XIelWiLb3%2B3gdw5aLkjDu4Wv7Cds20UqZMRY6%2FYULIs4PCCkzwx8oHdu8YJgBpr%2FPvwBE9RuauLnVNMo6nH7fUgIVk4LJ1XVM4r0J0CxQi9562U2d8ceC0h46u7TPWQKZIEzv1prM%2Fm37Y%2FlUR14hAdKyzio%2F&X-Amz-Signature=c87ad33dc2c7962e76a39d7a8d7f6e8de1c5f1cbdb00befff13999f5e81235b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
