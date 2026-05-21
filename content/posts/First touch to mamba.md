---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664U5YOB26%2F20260521%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260521T212203Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJGMEQCIC8kfWHCxI6804bVMiss3DcuYwXV8Xhxe3FODwjIVaw8AiAWgwzIQuDl7oy3XDpTteuzJ5HBO1SYqaDMPg6KMR%2FeNCr%2FAwgNEAAaDDYzNzQyMzE4MzgwNSIMrHNotW8rQnwabtmyKtwD18vTsQ9JNv2tPHFW4QVjz0l04b%2BTMvbiLmSceBwknQVoEu01bJAIbCeIaeNksn%2BjRjSuD5bboT9O0cmDn0RPJQALtjDliKzL1VEqr9ylF%2F%2FZBMu%2FOGUdUuIL6FfAH5ejrUTwtdNUanTkM5ejIcfPFfehRYVKa%2Fmz0BsItiT6jnJNnvBbdBz76USQQym%2BCYlVSNVuFqKajqu45FAz5JsDW5T6JRJR2V1lQ0qk0Dr7IvUkRNXiXqtcm%2BLR5UFjaJ3ZMNQyCQWQATIbGJXa%2FcIrxVOsEicg%2BYNtkJtFMVm%2B%2BklhCsYtIT3wSTqjAb91VzneT8kXEKV%2FM%2BR0hDJbTAJwVtVr3bYw6Rb%2FiqwT6p2i50yR2E07pCzzFuqK0QLFgyY7b4U49y9E0G6pXadD1fimlLjOHxQPaPW3Noe3JU9EMPF84U31sE%2BPMU1ULVTwT4Od71Dm1RUJXT6Kat1pR3j%2F2nSoG9dtNK%2FOrauJBx%2Bf5%2BkFhFeScrtTEUxwnIj%2BxRif6L3vgua15dlb%2Br%2BiPn%2Ba6Y8iWXWdAkpbXpe6nYNqNwLdMlhOBWjevIbZ0NDWe%2B2moSo4xLkwG0HBa1Ds%2Fr9TVoa7QMbpu3cc47wFc84SwuPiB0XbcdUpawJKfj8wps%2B90AY6pgHHc9ZCq72j4Xi0K9r3q9253LdmOEP550vi5842AZ4%2B0%2BwrKfE5RKPvNTnNA1dYSPt77zCwWAX3btdYvhWw94fcT8BaCNDfoxEv8wp7kV3XfVdYCI2aSEbC71uHkMjpqYIJfSLvrLBMH7r7ixC9ANp9K2qiwezSzFQ%2B72GAMXjy65YtfRHXU%2BnL0Iw14QSFSrlgjE72ygm5t%2F5fLWStcz7bdZbGPInk&X-Amz-Signature=69e30971d21f4d25f9f37dfc3bb61f271f6dc9936d207568c6d3d3e80fb965fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
