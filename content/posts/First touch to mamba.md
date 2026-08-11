---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665M6DQQLO%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T004800Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvOrk9A7i0Zj2hjW5YUIkupsDvwj0%2FHIxTnT4lXvz2CQIhAPCnanvc7Vt8j0glTLBwWqhOSPGX4pmQXOxRq4itAPAMKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzNTGhlBuE1jSXf2l8q3AOnTNoX4IhtAWi790FObYQyIBJH8F51L0%2Fn3wstgaoLbhir7DjERiHQ04c1Ya3Wj9rkGjpOwOEd6mgmuUfA0W%2BKBLvoU9FbBbeDWyhr9%2F%2BteHAcA4TQ7rkazIKIV2sJVsz3gDH%2BcoyK%2BQLHxz9K0LtSAjbVPAm1aE7M7cZSDg9%2BDJBKU7717YDPWRzcgGXz%2FiA6dyIqWmQkhJfRTWwwcltJyDkJUui%2BLTs7i4B1et559hnH%2Fcyf2cZtRKYUR6iuyCupBqOtv2yZBa%2FxLabecUT2Y5g5NYOA7aps5oOx4HD7%2BDZqsJBcoj0SReFxcnw%2FAFGmFxb9Wa8OQBQnGelzRNlOvaPTeh%2Fpj0g5A5yVNqg0mbWXCw8cUKzyp0DamEMtvebKbczJBna4i7AIJEaOipx4OezmEa0RAf4XyRSMlOuT%2F5x2qZzPby2not5cvFfO7N7%2FDih099iepYOvyOmWEFhoSAc%2FEbB8pqnrQbgY%2FYAa%2Baow%2Fq3LFpVCHg%2FJeBeXcAAzejfnX5NGtssZH4CODxnx64%2B5f%2BJ5ykWZyc9BOmQLGYCYb2ji0I8w3USj4DvQXxFNwDjenZOMYioYQix7snbBbJOzCIf1OLnkb%2FupSfNe%2B4JfaI748Ckg6hDniTD52enTBjqkAVcUSkSjqEyguDa1N0QY0K4tcfpYN%2FOLXHjL4cYG52TrVnIS3AljU54QRPtnNHcKF4X0vtYKisNytm0B%2FdJM%2BhqoudAHN88pxF%2FLls1ZCJNM24ZAmBMXBVS%2Fvv7i%2F79Ys%2FbCgn8II%2Fy9e%2B4Gl7sa6AIpiLRZZbsR5id9yqrZxjs6oiMIGLiJnnzlXHIs5DVvBL8KOLKTeSy3JyHHlupAYYSs5Bl8&X-Amz-Signature=e73501cc6b0fc8c82201835762044b6f7b4147a55b9d37eac19a8d955cefc17c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
