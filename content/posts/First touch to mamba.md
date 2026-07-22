---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YL7KWVJD%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T114208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAsaCXVzLXdlc3QtMiJHMEUCIEjfgPQaQ7irzF21LVEga7jqRnzEMAzDggDDBM7U7w76AiEA5xmLU5QJVu9z1QQTb0uHN7ZHMRp1V1DYlGHhCIDojnYqiAQI1P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2BNAlfkHQWiPXyzQyrcA6i2U8Cc4pJeXgwcgNXrtUySpZKpMCqNYTsEEmUSCw7YJ3lbtReNfOXwyR7kxuQhXT94Lr6supEGCe3WpoZC%2F8dGV%2FlLwFu07AeKfzb4%2FHTf9Wk7Oo7jBD8k8bJdPTtPq0X7wqM72HOvPmabdwLJ9Moduzt5PppJrqRTmPHFi2Y%2FGchmpDHBxmg06ElQ4F7x2yNiIct1jeArZFJhssk9B9wCufdhbCGvSusLZ1EXiSLN%2BNXcXTS5PSLCoy3dQqiim5mMyAFlT0dvKvvzIHixHUlQftNyBI7sOepklA6sdYAFno4CFFw6ORfnoe1Jp%2BBCVv9B9LQRptRAmRdIs4QaILIzOAFfClqX6yG1TamDHwiZPxZXRTKkYDLi2oL%2FiE6wHNz6hhLR5%2FUpTTWOJuxBzM%2BLxL2qlErjukc%2BW%2B9X4tw70dbinfHzkjt1U%2Bbn1Q5Py8hTft0lsvV%2B%2BNlNTe9KXrDtEsdEdl3MWKOHzwJG97giBEItWbN2aU6r%2F2udS7EfvgP3rHcHoArVd4ai0VJz2ZEfyZnE9H9QfQe4ca8kzvYaqFEdh9op79%2F6hfvxGUIrqz3wuXnQpsFpVphs5IWERbHVjVhodTMJ516mOmk7fsWOMrcPoYHYLzzQsFrVML%2B4gtMGOqUBLK7unDeszOI8AglYL9ilXZ1OaDbKgg5KQX9MHqvW25CdRyFYTF8sDuEV2Mi0Rq95nEP%2Bf1a2ixwMeX2%2F%2BSFfx7ewe0vflwfLewvE%2F1uFNAl6Dii0pV%2B6pxaRUktYZZ%2B8bRylXgShwqFNaYw9gJGcZruMO9rXntJKuHRRcsxRBy6vj8kovoCEsc4Q4wwwxfzl3T7ULNwGTCsF8g8OYQpRohgkZavh&X-Amz-Signature=ea87340861a1818234fdeea88b51954ce279c75af55e2d7882a3581ca6f430b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
