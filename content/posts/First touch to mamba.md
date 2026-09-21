---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46645XOGU2M%2F20260921%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260921T160454Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYZ7fMe8cBPI%2Bxs6byXr0t0LFmFG%2BwcS1SvHoJ%2B54DKwIgQC0QEKfcvS0ATVpC6Ll3XkmBnHmVd5Dyqq3l4UaSYvQqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEIXG0DwGCGcsMPtqCrcAxeR4dV02W1%2BokwV7mdPwIxAws728rfkTziY2i%2Fw21qZUJbe%2FwHfu3jPnGQNLPPZbmd9RVYyzYNCYIme4B3n6phfnDLIz8QuiGxWLzr%2BSSbAmvxH6FR1t7rG%2FdDm1t%2F1c0I8xplfZx%2BvhTHaA012LpDknou5uZT3ZXfvyp5IO60X%2BcksrGqqDBiFImQvWuwrVwPKY35s6beNrn8WSoW3Ow45VwNR9ei%2BBhGwCuvpFZ9WnpbQHyeXCVk3kVzrCvlMaOsaq4767YksAfGz5NTHe9t6rdkk5cDLJ5NzBuE01jwaPdMdFKlXt3uqpfNCR8jNN6cchhek4SiR%2FCWpRgI%2F7nGpJs9r10y%2BwyUB1oCmMveoOe1FKEDzaYeHgT%2B1%2FW943PrjnPsv9yn7r7hNkLnd3OQtoQKJIk3nx6OdSOM0SCzlFCQVRJasJOnnmIx%2BAXCRNW0tUMlW5FERmkrasPESnadS%2FCZcoXQSjopqXsJ9GWZVs56wSrMvN16dJRRdqt6P5NFeYJZ1yS7BrVVObQh2N1K%2Fu7YWglDtb%2FeFe7GOw94rA1u%2B5hpiXdJQ2U4b%2BvSSIkyWZQsvuYD5JufBPpNB0PgG40rHpBSGV1VIQwLlC4cofMCl%2BcewbLAK%2Bd4VMIyXxdUGOqUBvH%2Bg8ICARiv4vEbfDzNURoEGR1GGPnSKuYvXLerFK3SyTmrM2k%2F1sHJJnlXYfq4fFIeJl91ZULrl8CvCidVYT33GfPh8%2BhRlLWquuigldE8e4cHuX4ZPnVG6FaE1caMpXL%2FC0o4RQ0cqXilEpznQI%2FC4YH40MROQG5gcIXKQ2sbF8pk%2BB6514ecElCT2DMEXdZUacoFjKs%2BMu7xNgvJdkEniyZw7&X-Amz-Signature=31e7b92bb2a81347808b181a4ccaefa214142d2d7ee2051567a5b94cdde0deb4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
