---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USBJHQLG%2F20260807%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260807T202749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF3Dftm2Gy63me5Ej6cXaevNyktrqQOLB2DwcUgaE3cjAiEAxhRs4rMQPdwMvGIuxKdkMomTenLSfrbLNmu%2BdZqTpcsq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDFVq%2F0Zhm0M%2Bf3GIWyrcA8F56C4ya1kzA7aczfsyL5uN1KRPqlj787EFrA3ysGQ1FQAMOkO8yrGUAIWk%2B158PeLVaUSQ883aj29WaAqYHNoO%2FImiVdInPMvsixRU6y0R0wMhksJL6gpZ9xOPXYHsFrKwaoJeYFQo3%2ByJ98Rti29%2BfSmLP6lbxxLyV6mWwkV1AAsswQSYWRmDc2duQvp1VbCvYwpV%2B%2Fi%2FUGdISdaoq0jxfkkx%2FxRFBb0l2ZIhyvs6xWZYYExay5pdps09qCXnksi5Y5z3tWG1vh7GfVjcRs1NpflZOG26KaBCHV%2F0scsLReH6%2FK01E6Edo6%2BvcIoPqMfAAZEuRR%2FcoddNhYVygk3S4sIdRlc6FxfJgmjBT7KTH%2Bjcw3YKDnXy5N1EuCh6YzoJ8F1QqXdq3gR3r4P3oUTBYV3om5rMU7hOo3F3J%2BxmnMbQJdO85m5KTOo8LsKLXw1a4Mh8uqB3%2B%2F4S5MxOLlXoww92Z%2B%2Bgbk7nRo2nLoiTuCKgsdYpfp%2FLLo%2FuUU2DUw9ZvH4xujy%2FM9QsXoiTJXApmhEvkmrRyi%2FtUSvMcN5RTOEr82Mzz34WQt1BgqlZulXCDK0Sb%2BJydmTPURS%2F09OzXgAdWj42NpLYjKvivc1r4RKXGDAyuzgARYiBMJv62NMGOqUB6vDb%2BDVrF2cQGJPlzVhtrn%2BYAPRiBaMD07xOPUmfVNCfLpKgsipVrBiX4wyzlqhpRrXPBfpjk3yWWxQmnNozS9uZ7fH9Ltg6akNughUfwhLmkgZpCUKOeaiZqHxBYWzhtUBT5P4ftzR8jjM%2BCdF%2BdGEdzfoFi6gyUmoLSDXrxejiTl65SysiyZfWOcH4Vym2wx4nkyCcyHWzCFSrbmYhnXK06G6d&X-Amz-Signature=396f649947f38be2f2b6e7804257b65ba6b64e91a2773e92ab1506ac32090980&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
