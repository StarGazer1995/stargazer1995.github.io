---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRNKW4Z3%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T143151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJIMEYCIQCx7Zn3GFWm4e5%2FbMJfyU0YlJRoWGQMK4XxfYOgrgSq6gIhANyhIw3%2BwGiauKq8MDhngDgcJ%2B0dsJ0NwQrmgWHb2odYKogECMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfCDxnSMQhCs9kILwq3ANculFWpRYkE5nOn%2F%2FCKDS%2BiCBCxhuG4yQCLdTLwmPnNgtyhk6AYiYH5DGV8PoagNWZzhyTzRolsfNCZvlg9rOT79GG86AHKbUgRcm9lqJ%2FcsUm6caUIsxDaDSa5moVlNIYL5crgkZAZ8Ir3Zkm1BrvA%2Bw7%2FVhYgjvdnJ4IxtsQgE1iV3IjbLvUB%2F8JyhiS%2BSERzxoYpegk8KR%2FNwdyIjy7mb%2Fo3I2tYjUl%2BbMWqdWM7KRY6F%2Bm3v2T0WwAanotQF%2BYGevRnaV6prwA%2F8crKaVJEmp%2BDpZKZEPtjnJiyaAdMi4Few1jX8Wq4i63WKJh9vLGh11XQSePv9FsAxFhWJVZn412oLK7xXsGWP2buhR88jU%2Fjq%2BMqsywGKZwgfO9r5935DakmvXqQMkL%2BKBRzQCbmjgQI27alSxzZj58WxcA7enPynVS2T365YOCb8dtJffaHEuuZn8Xr%2Fbt%2FqMJWtAILshhHEphdin%2Fs2VFhyPNkdrHTkavmz4LstaSRvqEo6d7N3AAf3rUTVomN%2Bth6j7rMfV80v%2Fz%2BOtOZMGpyajo%2Bk4QVgi%2Fv9g9etSBaNlt7LwLLEQjpnSADNATTzLJlaNle9%2BdZbspWdG06lQJhdEsqHJXcg%2B4us7o9uaA5DDz7MLWBjqkAZC3gJR9Osgyjhpi52bBbfoVNpC3ODqJnpv8E7rkXo5OlEDT2nAtG6IPxH3daSU6WCgBVbOuBYLx1nCfIWQ2R9dzTW8Vmbke7KnxumAtWuPisYD8ckThYE5nIWGZCRS%2Fd13C4muxQQpH2apXUsgxwZJcdggcH6a7bmbZWlvImx9zjhv5tH9wvapi%2FB%2Brxz24lArBqSsLHLtBEyYP1%2Fiq0bXFk3F7&X-Amz-Signature=d46ce50078c52629aec8a56219126c64c411e0bef0d0f021b42c6f2172a3ac5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
