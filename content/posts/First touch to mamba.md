---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAB7MO45%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T140716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQCoK6GmJVrXcvRs%2BPY0QdvKK5DPWbv7kr0h8G8VEH2KHQIhAJGA3HXJQWM6P7MyeaiRuZDNI1tB7F%2BSxoV%2FlAxZe0oqKv8DCA8QABoMNjM3NDIzMTgzODA1IgxHqEGxZqrIeDodcxUq3AOSv7THJnfEQO1E5e%2Bg%2FeAY6ES3ysEmcR7khD8VrxU8MIzCXWR4rBgY%2BpNxCVp1It4Drj6a4%2BxuGp5JRF9pCpQIGLrn%2BvxP%2FzcnCFJ5Se0Gh%2BIJV48brshc61p1cS%2FGBmLcgygXfMP%2FuT3I7einSEhlWLRvXdCc6ddeEBxYGR1PdZSL353zYjhjMX2JjK9BP21%2B7onaxlMQaIq9uL55EkRh6%2F2qX%2F4jOuo%2BBTkEKLshJxNRn88gVjLQ6r2qtpUmb56xHL1pQCcz8V%2Fs7kS0R3QnnQxceHNjohIywrIrSfM4imbbMntPVPPKei1hMwkwhy0n7qACahl0cmIQbBfVOkciW3Qa3DYlPN8TuTJsbQe9nOe628%2Bo5tXejvL9Te2MehU7zBydU0dowfrSCsJ%2BGL6AyLJHzapjAqZhou%2BZYRFHPa6Nhf9ClgV1rMcTf%2Bssqa7jTJqcuRhdHQ8%2FJaLhZrOPomDnbHzEAodt6tGmpgGfIC4ow3%2FH%2FhsN8WJduJjQeiZzFVh9OP864gfZJW8cpkafjIxTFBkOoMwwP%2BA49CacV2cKaP556z28FVADA92Dkag9g44%2Fu4nNJhuISAwmkOB%2B7EOBNXdO10Fc5g8EzOzn7RMPe8gW%2Fmihvh4HrDDmsfDUBjqkAaXsnjkNU5X75yN4QPbst34TTAMe6WqjnOvT2F0lt8hLU1INSaB0idFTzBGfpCSi28ufTSpHc4XjYEnL6LYLVDSLf7yBzP5yZKOj3AMjHvkTksJG9xDGcKd21W%2BFMwkO0aVM%2FF17KhDwgehEvquJ2BiPQOfU3h3%2FyPCi6oOCKKAKrYYoYVWxM8%2BfnuGj6%2B5GKbcvdz2SfEAOztgB%2B7Xyp0qWBjSi&X-Amz-Signature=638dc7482261b9a27dba09c7af8c5a0a77aff7f9b8cb61d0520390c6b670e3c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
