---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TDKROOYJ%2F20260812%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260812T124037Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIF0GfPFp90ebii79Ntq6bGyBHB1rfPOj2lIJFHeqboMVAiEAiTr2aHCviQZvy%2Fri3ctCR9OE6Ua06256iXlcL%2B%2FFCjwqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOyNRVj4vC9lzXrRlircAyCBG8eGRxRys4V3h8HwP5GhwMPDktwDcze5sW2mS3xPtjLg5pXQG9a%2BpiND%2Bl0DivWXQLfnJvgrDNjZ176dPbLE9hM26ZFM9a0dZ5s3rJP0TkpwKsLdhANkSGwl93iPpkx2Y2mrYrMTZ9bRhYKCcmXeiiOUFWGedwueEvw%2BbPYyWAZNO66bXUe4zlV2EbJCyOLt8PMPsRuLQ0Sy8tzQ9qabU%2B0sNRcZRd34vV6d2To9QmRCv7HyVQuTjMgq%2BObLSVAMRR6fndCa6pz%2B0%2FR%2F6Gf7OG2eOQdCOE1W8jwDE3ao1NvCzQxP5%2FC4Bz7rQdkAjEShPQfkgH%2BGIpEHZ8XI%2FfWAsCk0GAV4BvFoCIgcPvihnm961%2BMGghrzWGRjUjOqRsSkqJPM%2BAvg%2F%2F0UtjdY1sbPrY0cgmxuz6rRZ0E7Uaqc3jUvYCJkrxL67TGFsfoEbjiEjkutrqpSUNg6cmR5RUx7FnaZ2gPz6%2F7ZngjVE%2Bx1ZQaCEuFAgnhipD8UGY25jw7Vs8Gsp17iQwPTNmzgAfluTZW3dZentK8m3Inq%2BQg0FSPyDoTurIf5uCB6I27NLPaxLxjUkcmoy28eoLVrUu9%2B31Xi3jhRgHvmIHiAxzj0g%2FjgEdQp%2FyPBuLdNMKyc8dMGOqUB%2FlP%2Bz6KbO39VU%2FEPEPY5vxjKAWSd0vk6CCX%2FBFpZv7IkZaBllVR18o3I%2FkgT2j9NlWyBbKAhC5jPCC410k4cgF2nDtxjl%2BO%2FdP0HOre%2FGiEYyWSZeWvRV8wg68zmB1A8kkvCVRkBdkQoDtkaIU%2FocLLI9ldZWCtFTSnVz%2FNNt9ZZxpWPD2%2FStEBgXzIpaBPHaBJfES0AgTlyLi9qT0uOKkSDQpnv&X-Amz-Signature=a95563de700481422fbbd02c3227d6ff283f9891f5f15ae0472d64f044aad5f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
