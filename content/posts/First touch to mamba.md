---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUOKCB57%2F20260913%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260913T170806Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJHMEUCIQDBMrYH7l6ecdL6JkrK34h8f%2Fmg8%2FJbJm00ZLADncQQTwIgJpmJnrEOHX6Ehq2oZoiX2v3KlMMFL8dPNZgmxhh%2Fc7QqiAQI0P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI6tEPeNx7XwARH%2BPSrcAzhg9Cs74u%2BNscJtxgZHTz3pWmxmt2cbTidkjcyhQ4X9AvIMduAQD4mu6gbv%2Bw6gTqDXJX%2BQVL23%2FQ0QMfjl2DHD7ERHKDmoNqMke%2FgGPe%2F%2BAzFsjJUo3p6XgHOYlSiX3c24EYIMdsJwTP7V37GjVUpsWNNn7e%2Fc3NhpjP%2FTlSrV1qOG9wzNTmWn4GcnOQB0GxfhuZ2JWMhaQ%2BlvKLAL%2BEPEcybMm0ez5MoIsJHIryZtBaknOnHFM0EJmTaEHmGCcWqNtIZ9pL0z0mNKfxX7BcQAlq1kCHZenXnLdCFF6Kh2uzM6vrFSKy3tq3lXk09vTEjdC4YfYGeFAmiJlc0vThInNaCRNy4%2FwyfUAf3opSxQqMR%2Fi94AQuzjNVXZ32SMF33NTmReTODsmrPXZbzqoZxYLBfApLOUFDFtWTgH9%2Bk6Oflx2rKEAUIEXd6%2BCh6COUEeQeOLy3y4eHHzlbZ9k6k6hcSkRxZp30aNNiu0ANXWbMSct4QyecUZuOF73B2SaocLfRoQ3xZN%2FSzEdqu9Mnf025NgKTTmpoxCrXBL6tU364ilsp6A0A%2BEng834KCrUYB4yMsI%2FF4d8sKKq%2FYQKVqRAI5bTMHoYmZIuc%2BxO9dvtRAc0hr2kpp4WZKZMPPmmtUGOqUBbtH9KbjaxuupuEPyzPpSM2fKz8yyNQ5OReTWdFy8JGeVK3d%2B7Y4QI2CKZHFEd78wcprGu1zD%2BkIqd7i7CKPjHfDYFKrIlSTKsL1ZccNAPRc61a5OTMlJVBrWkubaIoMr7UIunDVvlof9DOVYVNjzYtvfmaMjSNyRvRTWoXDCAzRmdl9LqQezCrpi%2BB4DdnKA2Btzf2HjZcVfz7Ult4MQc%2BNnTJMr&X-Amz-Signature=b9265abfd7d0b1dc2fa50a9a602cb8e08392a74964bb19e7942083a2f60df65e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
