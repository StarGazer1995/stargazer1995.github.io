---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTTVFHT%2F20260826%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260826T122529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFQaCXVzLXdlc3QtMiJHMEUCICe%2FHPqUQSOF8PZq3BiTX7FbaPDRdvbgVZ%2FJKnAPYXjPAiEA53WaveCvYcwo3QaB6mdFQ9CsRhQqTG50emwmnhTatucq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDHRv%2FDNlzE4z8UmSTyrcA8XL%2FfoHQNNVfRLgwgpX0zgEaTfQDYOZDluTImyJjxZpmJCgVTHDMCqHVh91DjFFjHOCWsL7UKqxwscgHXz8z4NYyLEMWObZgtZV43JttqN%2FQQS5zK128aN4Ot8cot3wHAkNsYn3Vt12o6qZjd0PKTA9jTt32EILQZ2O%2FGT4eWHPkG6ym8NUoZvDeOgdD%2BtIbkkWHVEyq%2FYGD1eOTg%2B7Qq1GXrH96nSLDslBZ0Fw5uQDLyR%2B4Hx0ACuH3DBrRCxYG%2F0EhkIWPt2SOxIT1uXBmQl3Oj%2FUJ8nktJghnr6bNxDwfXRIkvuz9CmmbdZ%2FhR4fvtBZuL8XtJkCvDjuMjJ8yZWISPg8LLrwLC1%2B1vID9QEXEuV%2B8zwmWQGVu44hqOr48447NX6OBrF8qzpOimEljDDcALz819b2Fv5HD4JSqRenfNmaBS6K9H4BPg5JxnphK%2Ffpba%2BD9b8zN29rwn2J9E8GLB8hjx4tvNNduUrPJ0abhYXTwb9AYADFQNxVuHzk9qaCUrFVnWXjMV3VQv5YWPih0aZL0I0iSeyZa5q71cAvl7Omr5cvFfZaoCup%2Fsd7NqlpnvQ%2BiFHvVl6xl1MclBm5NmsFRjhoeqjj2PD0EUzZP%2Fj62%2ByoGYj%2Fs2%2B5MMupu9QGOqUBrIh0auPCqmMasKqWcppTAiVHMvRope32Z24qmoavh4TFip9L6RqxeYL89OS3FOFdc60b7kSTyuVvr1wI6tp%2F6V84BBSYHmkHoqndR6GQqrXYj6Vb4iNe%2BKTpkNOVC0YCHDFHaN%2FWLFvVHIs1yC4BNpLpDz9WF9ud3VKoAuqhyR5P5eZLfd6hIeXdVvLETTYZbtFvU2yIKrUJ4XkuhLKBm7%2BAJ0T0&X-Amz-Signature=0314d6055d45eaab900558f322c484f751631caedc06870034a8c9eeb47fdeef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
