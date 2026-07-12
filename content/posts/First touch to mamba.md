---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR257ODU%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T125058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIB30mTFiZ%2B67coMZOEguKPEyAXPRXR47n%2FFa2egG66gtAiA0pV97SeRbEuLITUZ%2Flio2V3iRSaGE1wJQTzXNxXzhGiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMOLcsS%2BC4BWxhXXmzKtwDHVAkBRSWiXFpjbDTxC4UKhjZdQhcmf1tmfaWOEpP5707TFlZkCrKP1UGe04K7a4PoYKts8%2FeBfO1gF78%2F5mjwksH6jm8PmNNo8BhxDxIbfjfj3P%2F6TwXebh8OUpM%2BMqdlIwDcwz0NNDdyC1x10klJH1dWVJ3SbX4whc0UsGr90LLeXXiye5RVHgyaMlfTe7%2FRLWcUNRv8Wex%2FCK2EGzCphQ81fJf%2FnKdYugpJk7RydgCCXPQJXsdM0q%2BFWJ%2BbQetukzwHvwJBNqS23hZt%2FBTaQQIxHK%2Fj7mR5N7bkMJySixP9wRlKtUdzHw%2FIOSmJZpIzUJrTlfrZsVcR8sTTYYSDpjm16fUhafnxd2bof6LYo0sqW1YqGjKamlbqzxUDUQvn%2BmX%2FiYqVVHTKU5X8L3%2Bo85ddL5eHhIqvsCtXW0Y0aMkk%2FOKka9PMeASt3u7jl2CC9uTjnDg7FCIu8Bww5Ii2iUxoT7pm6KvmsXPAZ30%2BNs%2BLBuozYWADW2o9S4PDhKCuPfl5JBmWcwEHIBLhARHr3bIW26Uo%2F%2B2v%2FpUjWAkVXCgt8QFj0dkTsAX%2Bx7pHetR7MuCkVi9XsArISxSn%2FcRBhXG8CYNZFQvcVJoq0KJ4wS%2Fehv4NEh3uay2ffswwYLO0gY6pgFsJ1KLHdOqeyWiD%2B5KhtOUx1Op4QFktw%2Fm%2Fx7ur4GHsiXNqQYYE4PVg5SuJcHjydBQIptsgEPHZb40Zr%2FHUkq0QxJ8a6%2Bg7jZD%2BSyc7gBvEbdT825rfS2HQ1hpR5EpRPsTLkGKnv0TB0tNzhaQ3CEIBosGAbAWoqmIQG9dxBck89rGvctxxDruq6R1fHZZdqwGS8WKWe2tO%2FN%2F%2BaZQmQpq0WaQkcbX&X-Amz-Signature=29ed35edb715bdde2e3ec1fdef3f08c39059526e58d133d0b08b5db726fd0475&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
