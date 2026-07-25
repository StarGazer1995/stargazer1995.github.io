---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664V7L6AZS%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T045446Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQDEkT%2FA0SVBEXLp1e0UGvkk9LrfxWsX3XRhhUmtEfyeKAIhAIn3PEUDRf1BgrUHn6YMF6d5CrAapcGsUlU0vNUOo9wOKv8DCBUQABoMNjM3NDIzMTgzODA1Igz847ctd9fdTBMn9doq3APgeK0OBuWvm8FeVPKfUYs0gyJY44HbJf7y4vOrhkODRRLocQx17YSe0tEYMR4rHLWXzFhuYj7242QTspMxT0GI3weIJKYW8hYumX4N1qehLj5qQ1Y9Fch9luCsretcQA7Z7dY2yYo9fb6Ewtf3G3d%2FsCclykJx7m1Dvf9fUcWhZpkDI9fc769xouYjwERMFwpBZwvDTuJOvPkNK3cQW6wKTeQySeGIAeOwxCq5OqA2xwRnPlHqotVf0%2B7q3fSsip%2FITPNvYE4jMq3oX99pX8uuUhCN5uMCJV2UbeoXhHQJLaLMKwUW0vdC12HFYywzk0pRDRQPgYmn%2FzAGLRipBg2CenDn8wKHKE4prMEIDcSnI5i0QXxS8cn6hrJyuqv%2BvMyjyZMmo1DmvIfY0LsmqIvgmaC3BXm5oQR95chR4U9q37HxJSiIL9Vg00voZoMfzac0xvXT%2FwYn1xNDjfhGPFIQJVaiu%2F4wEfsMG2d2rsdbBSUP26leWScuZIwv7SBnK5H11t%2BMDRs806P%2Berl6W6ee%2FcISJQAh%2FAEmLiFPXhWLng3UFvtEFzFkPF47a3P4TGMytx%2BiPkxEQI%2BmVGtlp8tLZjpUk%2FbrGD%2Bbx%2BEM13gZ59p9ZsqCHGVA7rILWDDk9JDTBjqkASEbuFCjh8zdd44fRzrKj8%2F4zo3AxemcLP4E2%2FyCJT%2FGMuzXhxtUki58Aa4FNej6uvCOEYlX2AIEkvmClBF94xEk0N8fKxZdITHRWm1gNQe%2F1Fj6FVPRFOhewKSWsucHrDOMAqZkoqLBaFP6tzRBUrt%2F4OzJjqeKZf%2BXqkOWrLEgDKhXLfWIch6hR85%2BoEfs5AndtE0oeG9wFym94rEYciRgUPo%2F&X-Amz-Signature=9ed509d8e8c02b44efbb3eef9f189c600c703d286d568450d2826e911c6c3594&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
