---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQDPWNBI%2F20260821%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260821T182032Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDdf0JRjRy1EKvEXp6rVU5U5c%2BcwHs62r2N0hUiiMA7FQIhANgnlJNbbDOdTZr5rPsGMSZm%2BgG6xFmKRMYCFPAztdSBKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxsXrqTu6LbuzbHJhsq3AP5f8BVkSQW9P%2Bkz0PsHcWd6hUdTJ8BFbnLs1L4QvrnETtRj%2FF1FNCqIjPp2Ui%2FUC4grPGLFko4lMZT3KB72%2BZkMF%2FaIowtohjQMLNUieoycQGCMlapBQwMwaprOZyCmB3iZ5XPdySTgPSH5jMBpJlZ6YssT%2BnM3P4Ew6EKULinlWu0DoyVJmlWVEQYPiq1Tdy7TIKFPXWaf8PY3XghnHvI8DZYJgzAhgTim2cuRF%2FT6DuneFeTuwHPFUsVsdt60V%2F4%2FvejQVfS3rkonAArSdjtVW%2BiugFohVp5GvGE9h8C8dV9M6cbXtx01fA0smQz%2FBM%2BI%2BlZC9Qz3Zu7DTbW%2BUTCfGLMtUxtZ5gqm5IVU9Udy%2FjFfXXjl1VarQwiYMAAcxS%2BItyW2Hfy%2BI04xVmS3Pvq%2FvkWUyBbijRvD115s%2F5R2mVU9rEoZ3TbBdvkhcPQ9TQrVFPghkhmBwLNojNpjDQhag9qIH48E0wTQ%2FYXixumVedzhp6mEzCX2XO7HDgrmT2L5TcDWy2b8mEZQvk9lGUqbt3HckshxCpwzfQA20ZNVVgntbC6dltDAnjPmFVSGutlaVgQRIX1J30JQqqFne6i5aYLcrqg44ra90q%2FV1ZREelbWBXIxf8c80a35jDB%2FKHUBjqkAapmrpr7ihPdSRfHTcyRRoxaTFd1GdZo8e5qE95I5s1twnoZgVu%2FQv5cfbOu6PD9JBFA8bdK8%2BarK5iYutRBiy4Z3yky5UarxlZ42VjjEAZOGciukseBLGL%2FsH1XJFfFj9n24tjpTZLCKsPddcJFe3RM4GnZUsaUpI34ZNDDtO8860XPvrX7ANeWGGCVr6GLx4agZ0dG80xrJzEmPzyYfSWHdNcB&X-Amz-Signature=1391c76f24946f46625fd8fd34b072b5c69ebfc4df3af1d25a2507a456301647&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
