---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZUGBYB3%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T154411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDpmGl%2F5wSBvnVpaVzzRrID5CTF4Pqqrub7BairWzJOmAIhAK3lWktXPZjmVlskxdUCQyTsT7vKZrtjK9%2F6ftbJAI%2BoKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxK9laUrfU0UUUrHyUq3ANTQeNZXdMINYRq8%2FoxRkqatnRTluTOHf9IRETYwZwEJTiXK%2Fk7LfZZZ20AJSLx90CKA3sEwtrzm1wYMoljh8ZlKLCAB48ZsGSLw04mBYXdhj0znKmltUm42S0EvJUTWzxPlkxS8eZP8kvmOhVjG2f2hYVLID0Gt3841RtpABmb9dNO88mDmq0CcMElQFMPPMSh4AL0KyxyiMd%2BR1N6aWDrq8y%2BhXLywNNhfCY3GDrF3j9uszPlht3IcY2dBbcNe823QrNa8oUFcYIOmJnIgRnGlRyWhSy55uxcCv776qZwV5U9iHJBf%2BugPh%2BPA6W9mJ2R9OSGvVMfjZo4MNLIuKuek1C0sKfsRXRPPwdshO9J1Iap6sRTgy%2B8u34hlDPvv23NtUHGwKD5kOxPrdL%2Fzv3wrAab33VISxx0HEXqxzGHBnuTcCXUhmBliSUiEo6mpHEymxjffSQbjoEtJQWtxGXoRN32FEnBKX7zgLRew517n6wpDvprzSX4xd6ET90gYmg0PvGINaURnxMHZO6itVaCH8HBVMIgP7Q9mROXr5Wo85jiv5riq2KLpxUx8mzHjroFNoNqzp5Y6CUroeNTvneAzvJ8mmofhYfbV972PngMpeK%2FzGSoYX13B1eDozDQoqjTBjqkAdPD1L4GJrD65pvHj%2BzFu4pp9ppevzJJyXold3AfRG%2Fi0vo97YPa2s71w3xsDWE5%2Bml94bYPCbnlY3G7%2BcDofz09uxht%2BYEq%2BqlE4jn4MVDX1ocZEfqSeglQtmmILc4rBvV6aVn6Fjy6wSQHhOoBarGZL3uwykoVUoBC9LVPW05Ys3WZpBEnsz6whRf6m1%2BryFXwG%2FILdc2AN%2FfZVKYanVaRhPxM&X-Amz-Signature=992222f048fd9bde7e12cf09237d9507bbce08eff1253f5f7126265af0daface&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
