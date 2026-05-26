---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6YHH2QH%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T181642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHzd3FjlWRCxaYj1A4GpArrzNA5zIJbJ64Canmyy9sclAiAUJxdVupsBLWoX4M3ARWEE435AokxR3bOGuH8yb5qCAyqIBAiD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjOSfYY2fLaDaSRJzKtwD0%2BzTdA7DitOiFvZ9fMJdmXJ3wq6Kh9LHYQ9zhf41JKz92yLNuXGmyKgzJx02NN6T5xzvNyyho%2FkcUIYsbdyKGrApwYMfq4xUStE8yIudOCymxOyQ8qaLrUPP6DHs%2FPc%2BUkWrjFxHdpeRxt8F%2FRBTRE8NaOfARgPPEo6aLFRT3ni0%2Fz6MDKvxVp8oQaYFTQID0vmFPkMHzMoWtMrnKXGv72XeGY1sEy8dcG5WWe8kM2sdIVE410O%2FjgLyhhV%2F5%2FRUuBh8%2FkIK8KNMntCxruFBYpFS9YvuRdTR%2BOpdr2EEryuZEolAo3oAM0ILLDyKien7K25%2BhqaYVu2cuvw9AjeyyXCU%2FQsG3klGFUp%2FhTHy7ZAMX4pyVbcdFH8FXVY150bo8mpP1wdWs3qWUknzgI%2FewSdr4YLO7DNsWFEqBJAUchqpdDJrCKmvMt%2FT4KidGRtjr4E3gHQALVzgv1oQV1XzIuHivSjRC4ROGXtqHagT0%2FIgS8CB8BXoX8OeyX%2BYdyd4UL3ygPDWIRVCcb9XBUPuBy%2FQjIL85L75sL%2FGxLthGImCoaJ1LsjRnzlQ67xbBjqMBX3304Tm4SaTDBz8Y2hZPKkKuK2qzmL6C6dSvB%2BzRmGeG9eVLTyh0haql9kwmr3X0AY6pgEY3L0jX5wrXNGPql5J7egyudG16%2Be%2FL4pj8eQlu5wmbkaA5Z9ck1VIunE66Xgrg4RPZpTJ9DR5ucDmZoWEcNBTbzAtAZmekEunBmSLyavTyw%2FlfpSbjyAGbmqgD%2F9Ck0iedIpnMPvuKv7YEUolkvu0tzVl0RiSSpWMnWbA%2F4bIyljG4%2Ffn8Nh1D%2BlkhK9tTMwVdKyYi2xaMeVeBfC8mUnG0pwa%2B9Ql&X-Amz-Signature=4ffd15d970dfe9dad7a0dcbe7a1e4e11c9e74a525e81fecf532cb912d206927e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
