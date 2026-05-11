---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFKJZQN4%2F20260511%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260511T224532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIAKs8NoJlp%2B3QKn%2BnYGt72FFJeQcypy5cPDzwW6%2BKi5nAiAdcM6kekkZzBhSVl%2FV50JCkslX4EY58tDb%2F10lrTbbxSr%2FAwgfEAAaDDYzNzQyMzE4MzgwNSIMfKDiZSyr2dlxP5viKtwDCHjx%2B3Y6c7FZWMsrl2JVM5qvZvXGBELCMTMR7GeMrMvCLQTmu7ZolwHzbM7aK9kHdZrN9eIb1AUI4Ns791ad2iFB58mU8kVVMULrzeL16jv3GziLYd%2B26L3y65Rgd9fiJW0qbaB7Ytju9FRBvfeBrGsawwAsEUgpJ3qkAMJjxjt62s7B8VJCiN3jLXeMnBg2LnKWbqOizLT0sClaX0994md%2BjYoB4uIQscs3nrECVOcZPvxB9536Qjkk8TCv848YwokYY0Ks7oQhV9dZetuLj1M9Mzz5ayJUqaIsq2CFTNiui16gDW09VsKLrXq6ULDLRmySlo9MkD0A60jqdHr0RAFJEudWYa75Wkuj%2FKlteTLxq9tRxg7ldkpx6abZ9Ii0GiYZQPXLYUT6x4r8vorXgbte1CAXnK3cXHaUZ8VcCQh1qkxFUy%2FuzRrucmc%2FrhcLdKbydLMrs4CY0TToyybpBSlDFcLq%2FXNBJyQ613LAHzl0KPieirc6gDrOMcB9DML%2BuQex6LwfK%2B6YKuEFVdIdFNPnFtkwWw7Jj8bpbkxsezONWOv7OWtEdux%2FL0KIAewuriX8bF9YabWlqXa6DxZKaUa09sy%2BmUDDZlXW8c2Mn4dC%2Fz8bRP8gH6CeEbMw5KqJ0AY6pgHc50p0e62aa8pZco9y2OGAghR7TU2tdi9OVFSfR0bhWrs4NTPisPWGJXkvYzeMiN%2F6%2FzAuymyM5m3r2v0SOW5Fy30epegFzy%2BRdGoUXrgLCAkzHucLirFZFM92lkEqX9vfckx5aaJvtIqlqJSFF6V%2F7nsHG8Mvl1vkaVbG00%2B6kFj7dimWReI10YOXRR9CWE%2FY1lxUIXb6umVteL%2FJ01m13wNMWBQg&X-Amz-Signature=1db281ccc18768eeed3a4796867b9a1ffd1efe6ea8091d952e10bd53a253ed29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
