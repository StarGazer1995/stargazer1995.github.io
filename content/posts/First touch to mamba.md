---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643IRA7XM%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T114742Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEEs6AFlZ2Bc5j6tNcjuY80qoLGceBEN%2B0OKQeC2JK6ZAiEA8j2r6Ujwithnu7XTGlztsVMgwLRQ66gD2hC4%2FcGlj%2FQq%2FwMIdBAAGgw2Mzc0MjMxODM4MDUiDGf1bWML6I38yFRHMCrcA%2Fwuvf%2BXwvY4jh5atOYvfquAhr5eB4G6NdP11Ajw5bst1mgsWHpFmY%2BOMDE6W3ZnyPMu2C%2Fn4eoJKdxldS3JxS20KSC%2BziN5kSLATq9lM5KGoV%2FjR5x%2BVpLu0xTnUypGIttN%2FkLhuTfUF%2BkTI1OwbTxjRuSEdatA1v%2BT17vfr1q%2Fwq17cm2s76PGY3w%2BaPHiKUBAHIiAjdRlqbLZDp46q0WceizQi56eJDuJxTUf8OgBTXxe4vGdXJnNbDO9E0Qfh%2BAEUwqYDlzhMhDvPZNBTYuxt6mMNW66AXos7MbRcGNPvklv9%2FCDnSPa9hGfcEPsditAGrPnwZdByImoD2JAbz2tBOgdTVTZFw%2FfFjbkwGPqIGBUo5k0ZqaQKbc5QdiA7OuaQSNGlMLBvIQ3t8WSXjRXG41rh8AMP0qfSoppovYCTb%2FOo5J6%2BkX0EIHZz4XerPTC6v9vxSThn3zOHi7jV3HkuT3qGljRP%2BT8sdjhZEQBstBMASWbgi0SxtDyXCS9Qni4PO%2BNqQyBS83PjpD31MsJXRHy0usIAqS1IDB7GuGqwrEkoHeCk7VAtJLMKBgMWDbQALg%2FW2zCvUTJWklVAXIEUs%2FqLlldtyK5WzsdPIV7NtSzJlINCor4Oj92MP2CnNAGOqUB%2BCgdItJwdyCfPIL64G7OZV%2B0QmiRsEjYIqAlRTAU0GSlS1ObmKvyKUwvq6HarOHJKBC2%2F3QrpjbLnH1g8ZZEq1KuA9pZC4jN9driVKeNq%2B9GK0F9xGjr95%2BwAvK8jARJFmXMNmOtNoVnEJ7B6X9HLbtXEg87dgEqaXFBJ8cNsES1jEHAelNHzbg60HhOoQJ%2B%2FlAwpQBRp%2BCjTpPhH8qnDl5cxuQF&X-Amz-Signature=1b6513266c1c71e057564172273ef2d885286de2ae567b681baf0dc4331f9df3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
