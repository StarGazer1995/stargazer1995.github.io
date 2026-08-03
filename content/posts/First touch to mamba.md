---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBKQAHXU%2F20260803%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260803T210005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCIBMgSZFUvm%2BgNRyQ8eNhrc0N%2FXhCTkvD0K9NieSssV84AiEArOQ1L0brf8zsyS%2FfTuY4NjhD5uaxOXt47BXOxvC5iSQqiAQI%2Ff%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI37sTGZM1u5LOFA0SrcAzIZ0y2rpVxJFE3veQtdb7Cb97u44yG63nWLousZwXUE98LxVxatQKnp2T3fRFVXvy2EdcyGrzQATEt0nn7tQ2W1Ma2fYmXE6oX9HK0%2FQg3OYixGgo9UnF9ylbiAI%2BDtYdqeCwq2ngtMrnO71EXu273E7K54kB0AROtLu18FjrMlEeII6E7GbDTjqbs8Q1EcCtAaeYyzNmcBNER55%2FV2iuriNaXVDTMaC8PtdntPhSFN0LPPhGYgAI2iFOlS9sC92zkKqflyghn94V0L4GZ%2B3ydoQ4bsDgJFaAP%2BcGk1cv%2FKAxJkF02e3EOJquFrNshiyk%2FCKw4XhqPtxAVJiFmLCuAiHaIjOJx3mTH%2Fl8aqtVqYqQxttJ7R26xUBpoDvNbrLOMzqbsfD%2BpF%2F%2FECEbcV8%2FuaYwB8XQOZaw%2B1OBP6n2Pyc2Rjm66TO1iYiVx%2FGf3fOwAn2NfUKhkWtjpVVSwo3cCKLJwfm7SQpfyPc6Wiz7dFBlykp9YP67xCX00DyciRAnFvvtoWkg5MYc1nZDKOeZibdb9%2FpCvVaSCRAlNs79No5M6jaQFPLfHSJTcK%2Fwcqkm4fEp7Af%2FnFaf2X6%2F7MbEfBKltJUlfD8Mz2kx9WkozKXTSkfZoa2SupGMcmMNnpw9MGOqUBxS71K%2BGYY%2BrVBNKs8rJ3JHtSsSypO1Ya1uk1dwsfqGvi383%2FE0k9vlbHDMMz1G4bJlBY8qizEp5tCPfZpehYJoakAzIsxIm8VaYK8dSOZEcqMf6ncY3kaOIHZkz3GIT5h8pcn3WbdodnHo%2B8Q4EsV1PmuDN61N0gTI82NnsA%2BzqB0hy2V6fnoqGUMyH2vAmEaanBlkHoNZr8FcekAH5KLe0aG7ak&X-Amz-Signature=ea2ebc86f33893dda593806e89281a8fa36f3cb35c5b77c52caf554d559221f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
