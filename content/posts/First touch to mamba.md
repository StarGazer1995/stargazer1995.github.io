---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LLBFEWK%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T211114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJIMEYCIQDmiQrfzisAw4wEOzUX0QHL5ScmS%2Bk5txkqGPLjaBL3egIhAK8W%2Fw%2BFpd3i86aiAduzRSJPxevkY0krwLA79KxfqxKzKogECN3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDlZUnYgNyBWFZy2Mq3AO91lWrHLlMG%2BnfnVllrtjwx9cvzW9GtzWHv6nE9dq1rTpmDKZVoHZE%2BnreqXN6zC8t0xJjfqLrw6RjD%2Fy1DiTrc1f6DH455VuRDiNOkEt%2F5mHQvvNW%2FwNBaECnrwrsVFZMGXThnH9AgTqNfnPVrBnVhZseBqDVKbz3eaG3%2BQ0Kzf05QsnrA498od4Yb7k%2BGSOzi9Gs2s709JBxvX4oEmPBKecSoNSGyZqLchzordkStbNK%2F5ia2EbnGxGzDk74XqHfN0WBA6fd5v%2FIIlWM1PQ6Xy7nLjATl7%2FA7x0fgxSQp30gQ95oYxVeVVB0dHe8qv5mq1esp%2BCtWBULTU9ctI5XjWp%2FxSMzhVkIra1DHOt7UIK4hQa153HLXfdajGXJ%2FJKQJptZqr%2FHI0ZsrGQcmVWFbzWY6enbIf1xdVV%2FnJ4FLtv2CFxp2FmUTxjDGFc7%2FFr4gHkoHaNozAGQRwoDOAXCXuAzUjauOAfo8yjjLL8K%2FMecyt%2FCCoMpLOyvTIRR1cPqjTdlUFbxP8mnXqw7pIudaSijUBGuL2J%2B4SMPMpGk4BS6BzoCA8RM4vq820MAwsTY1goBU99FctOysGKU7fM2%2BMuoEHaJCfnU0orL6XO%2B%2Bx9%2FE055h5iQujBHczC5gbPQBjqkASwruDeqJ%2F4Oaw0bmPopXg8hIAmQkQGvV%2FpJCHuTwf0dJBWJi8zQ3H%2BEH24wDdhIu%2FL9t%2BUGMqI18XqNSMHkT%2B9grv6mj56EVKvyoIbzkajWlTJYJ9DSP2TLy1tp5SociZ5D63bJXOypuWFPuw7z51qg77MYN9QRFS3asv88wlHwACcYozlH%2BqMgJhomnCHl1SFa9DrwnjOtZdDEe1mA1275JKgO&X-Amz-Signature=71deb7434a9bfc3356e182ff7b5cbccda4644ae9bcc9ffc930a09da61815f153&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
