---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHF6RXG4%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T205416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQD%2BLyngc%2BxbPTJ3J3Imqhb7nF75tQ7IZIR3gzDhrZEVMQIhAPRmPh62%2FoVPyN1nLFnBuyaQihf%2BkJ%2FsMWkKKMqBkeGtKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx7cQ8IuliVUe7T2Woq3AMFZIcUvRgXy4%2FpPOD%2FH5krm03JuiirFMBSDn4uwegKVJga7xyJIOBxObmKiuXKUKVObaOWUfeIleWur5sI9EJJZrJvXcXLnAHq04e6%2FIIzwXJjdi9whcCbxUuTPJBYsvyil6jO91AlMbIy1eDUPIQcBSPMW1dWO1P6cz0maTs80leeP3om7CtcCeuGEGlqEIQGcVFfvLK60Oll45lpyG5OfoLb%2BgIFZefubdyE7%2FjVsbnw55%2BPoK1cFMad04vOMTYUiW9jRZUSkwLd3vQPSfYSKwDj81aLzP%2FJ8U6mFXOyjqT2Lvg%2Fob9RhJ11OhdST6f7yvfeKKUpZEsZmLTtRvxIO4Di1d6mGivMGt9BLI3mRi92vXJFrO2Va6bQRRW1BjxQKCBK0U%2FZ9Ul1eWsaQ7iyZ8WXpAGsjuS7P%2BrQn%2BdZn2bQNzwrfCgncSgP8nfjHmrpxvbCl3UHt7aNScRILKFSEQGAnJ4njnvNlMD2OvyVR6FvogxGHJkWME%2Fneo6uhQhzBt%2Bne541EQosFnN05bm19hD%2FoUI9SG9RajArhbi7TkqHDJWf%2FzILtUo%2BAibHHlEjaZME2hVz5UYwHynsecQoGvjhdctuiT%2B01P8jo%2BVC4IKOOeeKsmeSRwhS3jC6voTTBjqkAWJUIBxoCm%2BONNI3YS%2F3ir0L3CYxeyA7K8e0fhD1Lx7Hme2LkcTcrAH8r6%2Fs94OkaWWmE59ibPLydY4k%2B6FFgFerSO7e0TIVgLh%2Bs1tLsk93dcK41JdYhKZUjK%2B05naDfCWGpkVIPAIhJutMTf9q6ORq5vJj8qGJXXvMYr0LuE%2FiJBzHzhdYciMa6RqItRA6SViiLpzoQcnHZOll1KXm8Ai7mozw&X-Amz-Signature=a9869a05256ff50d73f57b1d66a57b36605fbea9d2e5a4cd326e3102189bfee5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
