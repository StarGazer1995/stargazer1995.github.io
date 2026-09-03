---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SMSVPRD5%2F20260903%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260903T063723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIQDbolHQoXtTOyGZNecrW1bu3vrTFLcKf4w3m3MIa3MFsQIgLaH7csAnzQ0ly%2FJ0Wm38qiQJPKxiTsxS9ncy4p7ZuGcqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPmOJFwPaYhj208oUyrcA53uG6hdMjzyJajhIRdD%2FvwSzFY0V%2FgANIdAJ0wkwJZsKCKxi3Jkyf7hf8MLoBBgVQf3Fu%2FzPP0HZs%2FLkimp27HrPmwd55xYzxLR8sb2thVbSHizxrCzXAjQkPst7a78tu2uQpBjLuMItyKnJ7JtvwWiKgtof%2BESR9OSNYZlVv%2FuiGRiokwgWEgvnVMLxGBQsL2oTeCPiYiSpVPHl4K3MEBd%2F6Up0qYwh1mHn1QospvX4jZ2Prk%2Bj0flgZW8qOeUNSQ15bFzia3cVl64sd6x63msnW%2FPrFmrsFB5SLlMgXOEbJNUJXTGNN9aQdf21cYYtgjm%2Bxha5iR53i3HbA5tjOxnOpBgW7%2B0I5e6wK4f02aB%2FsNDSU5N8DTBIVxNZdUcgsGTesN80ojiQTEK0qZ20yLJiOWWbhSV%2BThJd82mf6oD62xelbpnj%2B8UbZWpnh2%2F9VpBUzr5YJccQIMC1LWItBFQJTbjbyyF6Z8aM5Ys5Mbek8dUXb6YJmo2xqK7fBSuJXnkeRwwLSLcOREjadanwG4GLk%2B0%2FDVKuzV%2FDpyJpdhKBVhqXDXtjQv5aw7cQ8HB%2B4s4N7zoSX9beT%2FTIPmY6Qi9yPNDtlRtfxLM8edk90V6QxpAP62zHZ32cOdnMLO849QGOqUBpcDGkbIuDkUbtOdOjoehooftOvM%2Fy4wr3Je8Ve69WjjvZHrpYYsEglSQiyMLTIuXxjQJDFjOjftw38o8AorYICxjNjbYj40QVBGfMS8fZNB3MQOaRF%2FbvWP3iNbCqqFuhPP%2FOe72rixMrvsky%2FbaDLd9IvvkVtl14XX%2FqRkSRNCmEYrf3MtZfCohTwX%2FSWTG6Pr7vPwu2WgghiRZz%2FD5IbTNwSLe&X-Amz-Signature=288d7dbcad569eb5b60775820121ec2ead9714e3056fbb8d960f2cc8a5892c84&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
