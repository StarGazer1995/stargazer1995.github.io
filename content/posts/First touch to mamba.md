---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JJSVY4R%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T191113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJGMEQCIDMJt0uBcIVYGv8AUiWfhxkM5%2BrNt8yUNQZXRrjTbo6TAiB%2BxOO2P7hzL%2BfJaqqJ3HFgyfh8YHm7YR2VX6T7LyoBxCr%2FAwgsEAAaDDYzNzQyMzE4MzgwNSIMv06oP6F%2FlShvhh%2FBKtwD%2F1Y6GiE2lWxDiSBaXbxl93jlfmJcyEcorR1u8bkOtfTAfhQYVkFUC3knEaSrncZ%2Fp1FdFABUJAlWbtKqiIu7dD5xr8zS4tSRyvKsXOR8FXpJ0WZbowvAmLUbsIUBYj%2B4xtEBbaoI1nn5lILV6mBh%2FuhHODk69ERE9kD0qzYJ50e1Gxs45bWb9hNplZ93rfSLx0wb06Amik7soCUScNmJB6DCGeBVjCChHjPfbUq6OCRIYfQ8kSzjw4hjUbDYrw04JPQFChbg4H0o1jSv%2FiRfNC4TOZsFmnq0ki1PDCOUvYDKcuQtTyiy6Pwnoz3hTK0QrKagKnZoNn7xJ%2FfuYeBBi5vL540zIEXfQANZg91i0GfX6ZTwZvWJLXw8MsejP2NH6SsPuotxKfhMsqMZgL%2FMYWCJSm%2Be%2BZ3B9GIPkD56sqGZGwLsPdiOP9%2FSR%2FD2Vc8IUR7G%2BBD0%2FE1jD458Y5iKZ%2FRKLp0rIitWts1UKGBjxCYp%2B0clij0%2BwmzGR5C3%2F%2FX0K9EVc8%2Ff%2BfJ5vZkJ%2FJcsLv0fIxVoE%2BO1KsIOlxWwo3FE2%2BholszaQJGwWp0pI8n1sQUig3V9YnW1a2WrIpnkaMannv%2Bb3WrEqPy7JcwOXPyGjDW9O7hSCYHAI44w1YPO0wY6pgE9UZEAQQffvzVe6JMjPqq4oaRbjrSmQGrMhOc2%2BDT68%2FV9sUDV92RJ5DgwAqpRrWDYBOxHjZ9wPWMuJJ3Z4soAs%2BdmJYLgshQHOTyRc%2FnlZqRejHmd85odjoA%2B%2FEIJlVW2eouReRIGcBCuMHEd7EILA3s%2BdJLK3bgSrY3x63fx6hB9xMsh%2BBh2wIr4GapTgEMnEXkeVMwCvzOsnitpJNxEvKRodcTw&X-Amz-Signature=6c0ab0266b01391a8b0f84030574d9198f7f23d70d58ac72948666e79b67f457&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
