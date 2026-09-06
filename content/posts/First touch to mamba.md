---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NCA4XFU%2F20260906%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260906T143140Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCID1%2FGGdjL6UTcbP4cRSmGZ6MMuG2e2AW299XfLguUbGDAiBSkxtMVj5W6suKeDpUIXNlVYpymOzskcjV21%2FVP6FbqSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMYB2L6hCPfvQ0NL2eKtwDgPMpCOEHr0q9AqoQNBK6%2B3fTzTHynlJftPdylPQh%2Fnvj3JnAtpCr01yCjrdj51%2BP22PmrqremeWwoOChSKm3pIMfjFL3yqzt7o0IF%2FYV2kCcnul%2FSleJkfeXonRnVmsYhjrqWd2ljs8HN3LM7PiGzz9aTW%2FobUabHU%2B9hDpy2cmWrW6Y%2BLTidiurczyYIUdS%2Fhnwz8PJsGRGRqqpLhemWZBPOszyDsGmVP25tB8Jx6V0sEoBVrBtFZZh9IiiWKxsP8t6zljkn8lXI84VWgZz7oHsiNjDMU9lhkwAFZyc%2F23Akd28GA2BIxl9CzmkmYr169GEVaDJ1uWuT1PvmupqmJT7HkwxR3SFnXho2pmkaa%2BKAJ79I4ehYhfmnYABBVxqiFmKHiE1TIgsWXeyhPBklKd4PU7Uba%2FvcU7%2BzqyAEMKKYC9Y3I7MYGIVYuQmHes1RXx%2B%2F5eog1rbGoeV5%2BGwv3jwQyKrSEmQN1xqlzkmKsvgWRGgaZ4Jk9FNMH6%2BliIB7CDhaNTXDeEeCg3QtpR3AEhaaZI6dygLT%2FhHuQA2TLjSKPsrO4l1e3SxdIGSfy1fK8lMoFp7nO3cZUqr5PMSNUZ5OGAIMiQn1%2BygtM5V9uivJidHXnZFtWfx39Ywi6z11AY6pgG9yHg7hXJymDMp7IWY1%2BYg9AVtYkawZJnQY4NfgkL5NPcjNnPIWk040m0vd2L5Csoa%2FVaFSOoDRGV07a2xrSG61fNzgP5LlXrmR1nShObYbFZjZxzPHup2jxCp%2Fi5kYUCoVna1nnRuRRH7D8DJF4dWldobtrPx37%2BJxvpEKgmQWkuV1ZTxr2KzMxY8XnCdvIvNSW1EdB0%2BN1nnDAPMbNxQW09uusKR&X-Amz-Signature=1ddbc01861ea773033bcae1af503f6c620e5a41daa7ef75cd0d7c65d6437173a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
