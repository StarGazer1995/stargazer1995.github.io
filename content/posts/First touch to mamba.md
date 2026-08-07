---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNGCHKCO%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T065824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCU1f9fx%2FG%2F2iqLiEF2DZxNX%2FstbSx2LB%2FmTcm1xhyQ5gIhAKHjckbnsSifG%2F0HBq5ot%2BhHWAsogbE81GYhLo%2FrpoD1Kv8DCE4QABoMNjM3NDIzMTgzODA1IgwznojMRtH5WcxiBf8q3AMqltgje6vAxqFSUkFkLvGpxZDu3YWBUZaGpm1GER3BlJX4uQZsUpzM%2BN3OTqYgJe%2BCKLlVYk8zOX1y5vQgMzddvffZa0eozVmccXbUoPjfxxLP%2BlEj3erroaGCKrRt9M3TkGzURw01FYiRLm8bHYYlEkT8YdYd2uQCAMY%2FkI2oAdU1eOFS2NcKGX%2Fi0qorZ4WVOpMQwPrTAnwXyFlJAEKN%2BbnDQDze%2FOZXVjW%2F4AExWRVcr15bD6QdXA9HhPt5xlS8iHC7vfQj7QJ%2BLkLVEpCDRmUQnTiLjRO7c%2BS43H1VNqzG4sEK9LTU1YDbxwpt5pytk1xuzIpTfWY3DDd8XQyr7Z88N7eLMDciJDjqoOsJC2gj1BQ%2FpSV4IURa4GU2HhL9w%2Bk6VwP5N17%2FE%2F3mN4rtmkodlJ1BJ51zxz0Mjo8WsNJpOLp311Zq9eYLU6jGqjRbSjwm5I8IgADMgs0W3OyINbURZrWu%2FRdVS2Ph4uGZ0rOGxMAfhjCPFELhmPoRckejwJatEoDkcnF8gp9uByBpW7aAk9%2Fsx0KIyHUKr%2FAq18fxYuEgMoAZZKNb3SqxmHw0j5rABumMNNcD14N5y9bAjE07eILCFEV%2FS5cZegHhReGjAhGUtX2vJfOjlzCE0dXTBjqkAd2OZJLi0FaKYto%2FHWr26xEP6fxm%2F9UnVTYrmzvFWAFak3NKmrUB6PhRiujtXz%2F8xAMAa3NX0WiUQydbdDvORQaAnMwVU2Ult0LDXJJTW5i%2BiEOBTboel2AjB6UX9kBiVsyZRPUug5NWHPoMFbQKOviOkz3wGoVtx2ckuFO4xzdtkEe8FNlMwdQ4g7bRn5CEMHfKlw0iRuOQViB1Ml3EEcFF%2BbMY&X-Amz-Signature=34116ea1fc4b34d6f15c862dc465402ed7fa2a3263bdd7210360104ff0c6125b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
