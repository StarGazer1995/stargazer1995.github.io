---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7DNXMWC%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T081636Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJIMEYCIQCaQ6z2nldxNge1d4KUGRKXecS6o1JqUzpJMrgl2%2Fr5uQIhAN%2BSdB971Wf9R7wu3SDGN7X%2BkX4ClKzS5YlcjKzpJmuIKogECMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLKY%2BmDZsN1oFCS%2Fsq3AN%2BmvgQJF5tYbfKAy7%2FeG0AA2LKrHd0Lm0DRv30q%2BZtog3mXqadKns7RPUK33KFrzaiYMF0qKYdP2BIGytJz0d9F3AUTP55SfFzGcjt%2B3rTED%2F%2Fa8sTiiEHnC0ZvlHM%2FD9%2Fd%2BycPsZP%2FrbtiojGVMir82a%2FYcZ4coFmDAStm43u4HLCsf6%2FV5zQ0tAQmEEslI%2BWITP9Vg8V1DZ8j3RMLEck%2FtPq%2FSfdnENFbn4fvWBdCbausBbQ4h9fH2RQWJ%2F2Azn8lC%2FlGTaD%2Ba6zvDwVoQvYLO4pUI5YbzyUqir7nfDxb5l5JkX1oPKjHM0kifOKDR5o8faokuEeaeegYbuwfTrx29XTixXx8Xqh4DmnEICebD5qeCPbRkTjFr%2B922IVuqbMy75gQ0WElJ6njeYS%2BVuraUz8kIWU7tHSB8%2Fvj%2Bk3RqweDdxCcdfujgR0t0qsPPi0qrNKe0c61wJwrtWiWM8kffVURyCdlJqhsw7tpat0%2BuhfVPWzAp8BUpFCWPZjOmBBiVsjSkmB1gwjZIqIY%2FjfRB%2FRqnK3axDj3CD6be4NgpLdZqUESpDOoBy3epxUBZgvyIP0CR6MEX5LvNUtAHsX70OHXSmakdXcVv1v91CRwDtL0m%2FjgF%2FIuA9a3jDHtanUBjqkAflztH70T5%2FEReqXCiCK7wqL8KkAdsBJl%2BACvd3fwEvobb9OZVwCE0mEQL%2Bq0DFwERngincr3RGAxFyUPzSO%2B8H4wDYG%2FWdYNOtiF63LXLBqjhe1AM7TtCKRhZHUvujecRkXuLv4dYgH2XeJVd5vTC3K4yByreipkIhDkbDoVTMfoLobML%2BfMEFadi%2F3Y66q%2BchMGbcetB6wT4JxUDQoUP08MG4U&X-Amz-Signature=743cec55a4168f3281f5aa2a912a2114dee74d85ea559c84fe7d2f524cae163c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
