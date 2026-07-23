---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RH526Y3U%2F20260723%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260723T080832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJIMEYCIQDo%2BtIW%2FTalMR2B02VV%2FGj%2BM9olz%2BdAvZwOI0IHnJPCTgIhANG%2B3TxKdDlEyQKPNbwy8IAO6VKp2u6mUs3w6m9Gnn39KogECOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaQaoGfr0ioW9bN64q3APyCfln%2F82OmDwGmaPlofghh14ZJ6HBI1BNPysQNlFwHDxLUttLbaI04KWysTFV%2FBPnXMFn%2F0EHmx9bVbtFoSCvWAUrfCXp8Z2H%2FozUBD43rHIHrbhQvR3yUse3KjIHcrfw2szOuu0VToEhG%2BfQ7bORrJTHBIJE4bLNi5K13%2BSMp57muSW5YY%2FYdxSkQnHipoa%2F8nKPxENHeOyO8JVML2WKZvn26wE%2BLDsWpwe%2BlLGKVE9s6dzDWchsYseCXNiTlqU4NvrJO3yaieD0hStHeJwi8vZuvxYYCBl%2FwrHoqlZh99nP3PVLbqc6DZD2tYvU%2FF8N3SGqeZU9iYzrYW%2FIF5urz%2FV2WOJ4ogrlYFJw4kNCmurqjp%2B2apVlbioQbmjslsj%2FdjNiXFf5GpsW6U10mjSGt3Ya2As5AN0j6g8qrf2EflXWX9MxuFDhiD7RzXxbk5Z27RwhsuTg76GfhUNfXs6XksdyumbA%2FqY9hlyzTaOQcCxyj1wlu%2FNl9k5cUNjzJjdCYq8oTA%2BET%2BNq5GSr%2Bhe8ocj2g5KghiBI19pEqvvUOJ4eLM8GMBaa5%2BXhN6Cl4cu3HaQSpYRpuTShnFqOsGSnQOk4iyzQpyIQ23OCIYw9a4RBy14O287lVrt5KjCI6YbTBjqkAWWAx%2BbjoR7P7LORzWaXbdD7fhuxENMyiczWOSF0uSimMI1%2BDjWpCIWh2OzCUEhO%2F4EvDxsCUimdgZZp0BczHHxpj3kLvvyixUTWfADsnmFB%2Fvvirbm0ks737H%2FPwtmo1cfn5nGC0Mz8miW4eZwUSNtGFDLTnfjls61BhrUFyUEF2Gqa288JozyvHEyiKpl65DUqND3JqG4R%2Bk5%2FpwYiX%2B5hHhWw&X-Amz-Signature=2af536cacad90b04be91d4d2e96c6b74d23f07e8f500c746cf55fa00f931ec12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
