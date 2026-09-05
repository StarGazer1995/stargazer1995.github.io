---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QS5KEPGB%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T062617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQC0TTRi4s9FNIdRmlZyM4AOu1cUCVNVrTERHlqGbwH2qgIgdmHwAWQHlUElxn65z3K3QDd4mDOE8rdziQLhAa4wWgQq%2FwMIBhAAGgw2Mzc0MjMxODM4MDUiDPliUNM1KiVmcCz4LircA9EGR8f7E1ePPUo6eh2ah5KBotsooR8OQBeriJqf9LgDcXG8NDDck5g7Ex9i7efuUQigQE5Q9ctL5WFvk5wG%2FpdrqRt2brpRQ0%2BH1VyLhMdWOeM7j4fABCdM8WNPIjk4HJO6zwYeWgSWpdFlfqChd7fm79FgBcoVgeTUM4llJHljMd9Q1mnJ8iIPjPuLXbSsstbUn%2FZSfDgCG3SeLVNic0RZQVB3LNNpWnHg%2FIMpO4Ps2ssh8LM1c%2F6Os0cCZm8uOfwIHnfQnf764kcF5nQyyxjfasDTXxBG5%2BxW2V84CGxm5f8%2BrZF1P%2BnRPUio2fdQZDxaUUyGGjPpwE5x%2FIjWWwZ0Nb1UkNs1mz2A9S8pSlhskW8%2FJWqtqfSe%2FQBmLjtuxHpQ3ZUSR0BEyj9owb2UQTaQAuLQfE7xcn1BZFCDtLtYkHd8%2FMN%2FoOfCe3K4kbvEav6jgc1NfK49o26g%2FoLWSOb%2FHDE8AJTyksphsJBGRPNKXpv8pWzTBA3yBONARMgIp%2BUVnMelFpGc9csqlAzvZWW7qt9A3WwumrjKsEDlKPs43Trh7jUKQ4K8GMb6US40ADebjjpjrYhLfuT0T%2FR%2FmH87MlntI%2FTO39sEk4smAlZMGEdgDslm0vGlUY4rMKe57tQGOqUB9QnYYJG6hhXvy70JcFXyZ5WdtQmKWUpmOfvkiTbV6krCTzzhfEADjV0fwpIYZWaMZVB4kLdJoMyXNJco3agWnJUNyKioaYLoJ09%2BOJHLG7d63MB6efyF30kbisfA%2B74tgrAkHBm6n1kYUMNu8eJ%2Bi4LY%2BNOM9QGZFmmBZPNwUU851yUZJcz2JVDQHS%2BD8PBQ3RVDnylO2DPhSw3%2B3E%2B57lH%2BJeWl&X-Amz-Signature=3e6317c645f012000c09b7a20fec7ebe289240ec0dbd52f18f974addeb155673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
