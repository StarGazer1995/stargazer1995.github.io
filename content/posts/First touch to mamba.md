---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLUKIWH5%2F20260604%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260604T081217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDeS6ghKsBztWJB0JdOD0JFnwSjkGQIR3%2Bd10XjULJJwAIhAPFZ5nIHQibudOYIiFqjWJE0uGMSdks2oKVh7%2BF%2F2CyiKv8DCE8QABoMNjM3NDIzMTgzODA1IgwrU5Tmo3hSp1lihUcq3ANVmElVDLWOUVPw%2BK2RA8xcJEXc2J9j9SVaZITJWxvnSsWvkQWHR0j%2FxCJloe08R09p8l1QKzAxLATsd3xsZcmGOVnOompPxVU1FNn4Faow6G3HKdunI8jNe4XZmhZaAv5J%2BJxQTfECAOOZSwfhV5kGRxSiFmSWHxDIrl%2FTg5ArCzRD31Qge1pLMuro0%2FYw3McfC5W%2FmqRSFcB%2BDqpUw5JyI39vfokS10j9ryTQq%2Fr5KxeyRr0%2FF1sWEiZ05WWlc6vaSyqYVoJdQkZlbcEPbn2O4fYhF9bwvkH4%2BZT9EmeKwCqcoqq8AzkJh2%2Bcwu3yqjJc7XUmrXeALl4du4mFHd0LzxswG0xNlY%2BMXssXGGwNwUYR7RGq9HVspAq95V9Nh8xb4EaDfpINdrxrnllKs5arA1tg%2Bj6wnDv4Nj0giUWo30XGL6rofVjbTF3CBENDzCT0znnSGRKN9JImY9rvBBtyppeGvC8spPvFe0OfJnexzYwxRffg%2BaudmWpafAAH6Lg9udo0p1HFAD8lXJ337sEXKHxNLW%2B5Q1BcqLVgYaaDYJp06YyeA92AXLLDa4rw63YIXa9tSPZJEIPFUR9Cue0ueluTOcA78l5MfV6GH%2FXTS3WRlsLk0%2F1e8dmdDTCXsITRBjqkATWRzEbWadKahzPJpr5WiZ4rE%2B0huuZAdVrUWrkx%2Fcb1yAupO9V08G4TUayC%2FVrnNJXxdgs0APri%2FarAjoOjkP%2FXP6ic%2FwsCVelu9Inft%2FOEEXuhzyUAOD4lS0NkS4X1p2cOG7xi81cFwyOwP6qYoLVjVTSRtesfBcn9ywRodeTWLUN0AcBElu%2FQuO3COEWkiRrb1gYJsFIWMBtpQz1lnsciCy0u&X-Amz-Signature=6f3241d58e52735f8ec1d4b90214bc0985d4af7194f35807eb725bcedb5d65ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
