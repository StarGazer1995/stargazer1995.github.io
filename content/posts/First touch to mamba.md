---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667MKBP55M%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T080421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGgaCXVzLXdlc3QtMiJGMEQCIDVAYjgkQZ1SdZo6ci43OWO8fWKYZFQtxETFg1tYvSaIAiAJZIk3Vdiirg8un3yQyDQyyGigmxJg9%2FGc7QD0jfCzcSr%2FAwgxEAAaDDYzNzQyMzE4MzgwNSIM2hu9l%2BKfZlUTnIMnKtwDj6uZwjPjXj%2F8sHkWBnaJMgF4cvj0v8utUjey0fyVRPIHsfB8iOOdQ%2BQL40vbS5EShvi%2FKhcRPFkOKA%2B%2BajOgWvOiPXq7R9bK8J5lm7e54b2DirtHhX%2BHkzPVlfaAFQ0iB9FxvfYLMzTlZba6YroQoChElOLiyQrfqKR3A2dvsbzdtxvjkdskBvxYGKiXCHmXWzEtKwPUgFKqo%2BALhpkACGX0sUkmFQKYQSf7i03yVXDtqS2hsngSxr7Fq1SOOcRf08JQJOsNAXvMeV7bR%2BocLRVYCbEKh2L3Y8fpfANvrh%2BIW9zFj23hVpu8lOlpBlBPmOIo1uvCqwLpp8XyfJtEZV2pMVqtxXdPUWOJEJL%2BBb%2BXtjU%2FE7H30N5ZpnD4vHCq%2FmgT5wklY9DVLZihw3%2FLYYgHXXnzKTRCwc0dt%2FQ2HFPZvuiGKLIpLSusg9txKQvr%2BgcqCED%2BmoY%2FJVlqGp0FE3bZ7GU8rsnMok0apgek0hzHgshFViUpgmad2kdhTghn5xuBeLzeKNkCL0gahu4x2%2FdjWkEpFleETokIRKNHXeOsX4ykZAD3dmqcl6hgbCMQinHZd0Sj7IGs0PU%2FtYijABwgR6YSaO0OciFXkQhB3wt8vrAIb5KTtu2hfC0wwPeW0wY6pgHFIyPEionOroA90OmZ25ABS5GewWyUBwzB5mUNXX2RFADBa0jfiTWX5SC74BqVWWO0qVOQHMzWAy4%2F5tW1JsSUqdKyAHEd7RnCIMbZ7nmfoj%2Bwoq02x3FzQpPszBPLDuJas79uacG%2F9s5rpSW3g2c5IOUiCkyZ0xtPjiVLAD4HcFmJZdaEOsfxueKP%2FWovuvWQu09%2BoWmG7oY0uNYZQOq3xB3%2BX%2BTO&X-Amz-Signature=3497b8dd4b884ed422af2060a73e11a66f89aacbabe2db727bbb08831ba6f080&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
