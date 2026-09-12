---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXKUYGO7%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T214703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGPMB%2FnEw6VflTe6zQ%2BjHq04wkklHI5H1k0Qf9LMF10XAiBaeyEx6Z2ufJDzyXq13vtAaiEb0GvdqmMvIFdw1OjFJCqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRj30nPjYuPc4jhDkKtwDcSa0oWvbEPyDXAKTgXJKtYCbGhuHZQFkrABR6U2msxLk7cD6z7b8hXCxJNbdQMR1kp7QyPmR4LFYrP7agzjoTaqFxPrPMQcGOjApp3fQX4U4O4aX9sAam6D3hAo%2B4jrXLUaGvAGWZpZvewr1TtgzdZcXiJDiHC7whbY4KKsSGJvy2FNsl715y5YADKjFJC0DY8plDypFOxG5hkAUQcwszZJbd7JZs2GtXhaxvZFkylB7xYYo8tV%2BiAXLhIQPckcFVzWvvDdhaalkon0OVrnfl2gFgKZpfCw45ILxsUJ49RzqcNZD7oeyhZBCcoa%2FAvpXo2nkPYOaeFjcDh3JR1Rwt%2FqoEJqJAiYt%2F%2Ffl%2BGNii2FW%2BfBocbCvOGocprjI65VIJDOB3moSPgvRdNmQ9jBSXelEBLZm6gqkS6NukD109gZb84MWNfzUCGKDsPDA%2BcSNzdupSwlnVG3VcMsTZAWrc9U16CwcmBCA2PpUTAh5CPoTiXlAD8beV%2FpM9mKSmEiJa8lUdb5qY8eLs%2FwQ6Vp2i6vvQY8FIHor6jWuYP9yKWXR8DUgzNdSIYCtGW5E6oEH4bzv5i42SmaCApvm33B6WgJH9ZL%2BwNTOvRSpmlAe8Bm1wc2GcIzoOzXvzNQwyfqW1QY6pgElzx5dUUm6TOQFwsCaKbRSZrTeFCGQ3DsZUQ8w%2FFGQ7L7NmEn2RNx%2BfnPnwAyYSOCUB%2FvMgqFL17EcKGSzJCcG6fvW2vh18VtlFcbVzAPsRtQi9PFic%2FK8zGGgBsLjW4ZTsd7%2BYONL8oWGHPebVl0S8NWtj1906Wb4v3jaf9SiArWbgM64Kq6ss9q3tpDSlRxrDgosGT91H9FCqX%2BL9JnnskzsqYly&X-Amz-Signature=ea2db59d4d2c49faeb0bdb998e7e92401cfe548227544796d4f761340cc73253&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
