---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNW7J2II%2F20260507%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260507T081217Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJ2PcNxjTw7NE6jm6uWcBSJ9ItKA5dkqrobJXfschAogIhAMRRi0yNLOcOl6w4QwQbzo5H6hsmmaLcN7rF61b%2FWq7YKogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxecdOx9Z%2FcsivxOtsq3ANPkoQBSHhbkaTutVcOxYTGYKcX%2FYnjIazMwNWh49zQkbBTu3F2%2F7R0%2BhjhJUst%2B2bfFuUCdmrw05%2FDkOoog3Q3mEnHEawDVo3UhRHR2F8650B1Oo5nEDWN5aOlIqHPUX2ZsQIEOxpiR1l0s39VhzCTbu%2Fc3F6jc9Jiy%2BOZNiG8iWOQ2Kk5oqxHtAb5vvFaDUJbtcISuTAJjChA6fG5ZnU8RNifkAWI326GGR5CQsT70kT3117QFgluwpRWvhRu3Mj%2B5jaaFOVYKYFyyy9dicY1gvOoTTrPpS1FhXmpFwTg27HGKM11rjBEFmMgraJ0c1kY30pnj3kGVHUIsurAPZQ84FvX%2FIlbeKOSNooR8BHli1yYJ77XjlrtIuC4z8FH4omkfiNG1qh44Y%2B8KDYDCxi2Y8M2bPtWXTPKno5MVMXeZpTvf%2BowccAcLgEUmEKKnxXxYKwabw3xNUKGlduMlrjlhJpG%2B6AQH2x%2BN18%2Fmpb6C7Ae2g060bKI8wwGCJsQTeJoiZQB8FrU0RwYQXpMmOf66l0KG2XP0BKtKvQMfHXHlezy7mtK%2BV7887buP5eYL0AmMQ%2Fa6EqAs9TCOm9qqi5w4Zoj7Q5IfrbQqcIskB9Gyf42pPr5yqv59cYi9DCb%2BvDPBjqkAW8KMijAgUPqNw5%2F3k2GaEcJQ2SC8x9xazWuT5v5kN6Eki13zraLthC2eG2KTcI1CJP1E3RMxFbo%2BCu7wNw%2B2%2F5Fn7hTQLYM5SlN3qtExrsBfY95xaExyeTEVxR72tDP2P%2FJQeZDaqGiI%2FbSUjfW1T77K5uX6NEY3J4FQtMUpjCjGJfa2KIVqeyDxCyOLXii%2BiVS9P2xI61lQNVz2udIFyyY9ULb&X-Amz-Signature=797bc73fdfb67356269fc821f28f81a99a974ba7a9aa5a643bbad6eeafcc4f04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
