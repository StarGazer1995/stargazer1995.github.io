---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7AS5A43%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T092024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwneS8JGg0nKWZWNRODnTIbk9%2BeETFw5ZqtAcWsxWjGgIhALbgOWVYWxyQZ%2BNqBzLNzz3%2FlKCZ4JV3Kz4ALEkgh6pmKogECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy86nnlkRwx5feFwCAq3AO1cfksT68YMnvQgUUvW%2BKVNY%2FXxIUsHNN6azdQUxSxjGNO0s2Kzoho7j5NIx43OFx1PUsKMkzlg3tU%2BHbeFgFv184VKzPc0PA8%2BqwlKnq63lduuFZw5v1kJyCLGsVRJMqu4SG%2FAKrAeAO7UC%2B4p%2BLMlBjJDnrLJwzUgHYwp%2BwCjpVnQwr2WH%2BJxMSQPGr3o2fsT7xrbMej5qrnyPYdIgjRFpZq9jXG2MXJJEd3ahP2PQ5SSynAywQHQ63hbVZ9pCQUqFkpDk%2BhohW%2FZQszP4Bshf17mqY4jeemhfJmHW4e5Zin5DvboV8w7aUsSv2%2FYXrBG%2F9L5f1DmrRAR0mnFAjcyK8AeDAZo7bHZkevwFxjnaxWLdzd%2Fr7nUfn63KkQduEoif8vwebaFC39WIhoARyn0fhieQ4Ql3iDXoUprAvFHG%2BZ7kLcNPtwSwAxqv%2F376NcBJZdjfCIRqNtU%2FCSbDjLlKCUuMo7%2BMug8U7qKESmBeD%2BMsWhcjUiSpmF47ih0%2F7%2FBJ5oK2hjvBzUdB1NYZkmEy2aN3oGGKvx5qw60PaATDdNhEpXOOz5Cd1%2Bh4SL9dC337srK%2BgmkOmEi4woTj48RVetV6%2BCn5TazN8LdnM4GqnZ7w0Kj5RJNpd0WjDz66DQBjqkAbewe1on3WJxwmVq6HHoQKCYXyYTvxA4rnGYzZ4aYy8MDVCD2sibCvs5nR3CanhJQdmciRw8Rhv%2B4zcpdHMc6JEwD389MgAaKXtOKypIG%2FB8rZkCt3RDNey%2FIjUeoVtmNjQf3u7%2BOX9pfrANcIUmqmB%2F5R8l9HLnGA%2FSxX1PS9n5c0PZJiraVifE2xrUxZdAeeJPToxoP8sgm%2Bh7YPlAk2gCmAyo&X-Amz-Signature=c8eb1f46c5f5a78e4d42610977afaa0746c46a5bf10880aa5140583c00d064b1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
