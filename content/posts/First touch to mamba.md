---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJ4RAYN4%2F20260531%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260531T100711Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJGMEQCIEMyFRiajLgq3VWWFE2xj7zQC5bWHkEr%2F1KlCazCrO38AiAaRgCRhsDqxIRLQqzSun4O8FPmeETv1fp6AXrgopNxciqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5cbXf9E9BCGcfKB6KtwDujtkvAvS0OJJgK3CsL27nM4rLAxhTIjK7mCXIMA93O3ddyTMHL0DXcto%2BDpEpEUwHdT1pZ%2FhtqeJt3kS2n6Qp2sKoOM%2FY1KF5HKBd4iIpm8S%2BNsq1Z0pU7wDM6xWz5ZX5%2F05E%2BdZK1%2FbCJ0JXOUyHwhJPSC4IWgrH585z4S2rtD8rlRHb90EO46%2F1ErJiqSOLKCf%2FaCbAliP7wMRRXdb54aBGe%2FEpCiLdo9jVSezXsNdr6VWH4Ye%2F78cpGcO2fDxS54OxWGmPF2dNF4QBs%2B6wwUmvZDPA8qdaJN01eCEtSVbwe0ri%2BbU2Q7tBNwzQvFxITXf4fs8hCOCyRqcEDtaYmn8GAGAnAspDtysSAbKNGxYJypesXK7bO8ESFuYJjRCarK22px5z1aQVtC2kvrlVHDnhRtEmuGMSFzTGrEuDXRcRf%2F8CEvyfTA3H2xubEGnaOlzeeAI2Y39F%2BICqcXSYEwPqilGCD9hykh2gvILF7voUXvGSHRnq%2BofuYzwCCbxjMqv4u4xFvXukCy7CYYw2L%2By6Db9PUmGEWRYQR9yiQoh2peqw1KpnWrZ0ddIUIriF9ab83LVuhldXhemIxjXEvR5yLrK%2Bz%2FgHtKqkRqSjtn724c1SEx9Ze5NHnMwr47w0AY6pgGAsed6lm8LhGwkZdSd8fW%2FNgtk9ChTovli6L09R5nxl483ujJO5LLB3w9X49SKvsIrZ0hpN5CpX2oXcajIx3Oc5P5WJnI6b97Lc39jN8GXsdptzr2emxwpFfO%2BDTTJDtYAiCPoi7l7E0PPQIDSbSWvFRQuf42Xm%2FVoPL%2BEhqHJfIgcxZzyQtlBZ457L4lw8Z9%2FXem7U8aNNaU7vEyIuZCyz0lRPkt8&X-Amz-Signature=98c7039012fedcf74c6be4a6a4912a546df77d54b4c028254b12c6b22f649b56&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
