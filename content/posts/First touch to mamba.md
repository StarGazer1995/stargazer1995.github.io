---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMASE53B%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T162536Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIFf4AFMHcNx0CxPeDKChKPM4Q8fAS0kitafU0JTMZ9FhAiEA9X8DafBbMcbF9hDgD%2F0NPnwbfZWGZbPcuYEFBlyNky8qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDVCDouy0tMsyvd10SrcA5MY21SjV6GqHrjjVQn1EbqVwWA3%2BYKA6NfbUnmjxqWLMl45b7lkAF3o6seqLUXe6Jx4uwRxXtKaMrF%2BppFD1iIPNFhcndVvsrmxKywiKXjTd3HAJo0Y3DQhCfncmEXnohrFXWldS6UuMd57Smov%2FYbEuPQmYGm8asf94pSsRWyFHGysoiBQSUnwC7PGeJ9WubR6BzcmJ6lD%2B7XnQg2jnmndq%2BpfWnw%2BJrf8hRe82H%2FxDOqviCvgsqhYBaGEQNg13NWf2Avb9egg2r48ldKldJUzCv25X2tBaP64qHoyC0uNqqnwHVLtq8jP4%2Fx30AH7mpPxL63ohg2%2FuVdT5zt9aQZLQB5xvf6Dymil1fC%2BhxKBspt4Hcd2O0jeuYQaHF9PLI0sSnLeyQWVLVM36KMMaZHNgy8LYcXEtEbFQqJNwLrNis5O2SiZrRdyq%2FUveXg9FUJ5I5u89FFt%2Fk0kKXHx%2BoS9Ka7O4kbO%2BwdKSOS3d847151ySF5PT1h%2FPfGPKvSVEh9XXMU2Xlpc1KuTcTNJTBheC9k%2FY0AXPMnbCNa1OJs%2FvLPdSNqdMi57J7lZR55gjaleFDHoDmi8%2BetnhJrIQilLDkGAS%2FRX6HjaTiRxjDCphTIU%2BAI%2BEPQbcdkjMKDloNEGOqUBPHsGn5OqNB7sZXwdyNSF929yjDZpuOEGSwsDvd5UFY0JglVq4U38l6C15qCiF%2FlWgcK5kZiCgKzJX26CUDKViyjnT8DDjnE4ydXaDq0vHmHaHs8borLxz2afBPW5yjCva3rw24B58gNEjRDXat%2FpZOPOPPOlqYuZobdLnI0v42AxbL9QphtvzFB2dgJ0gvAqPBoVwe4cv2IiJLp7jkNiHPlkm1NK&X-Amz-Signature=973d2f6caca61d925d021194abcf8ff04eeab7622e8551f1fb95c6e6c2b42935&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
