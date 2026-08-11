---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOIPTQNU%2F20260811%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260811T123754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPy4HIk20bf5Jirtz6UJ83D9EVasrMdNcQPOe8Q7qoQIgYhbQDRX1HYlcGo7CazvqjWgvtbtNeuP0dXIYpaqemecqiAQItf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH1sVs%2BDd51hFTBlOCrcAyYSlJ1vgWeNEFjaRInERvtzzNabxQ01VwoRLLcf7bfRnNzx3u5gjI1hOE347JnYZFVB6eEtR8Z5USDC49uiCW4VNo24JS53WBv7JwQ0DEQb2jE1pSndLththDyK6xgFQcmT4BIwHxEd1HGq2eVvd4Kpoqp6QrWxgRD0FFg1iMX0cUvu3%2BfAllzUGsmvi9HvFAI0raa94ft9PZx3HNSBWbWm1x48h28ndPxkvf%2FA76aQ4B%2B3Tq63eSFES4nJlv%2Fmnvrc6lYoBOksreU0QdhQ3KmLsz%2B0xdEN42fmxlGmUrinAqfqVSt%2BuowEE3orcw8PcKmCFJEsI3%2F24TdJF04aiviWnkbOGlJOE%2F88HUpCygD08Rmkubsj31C4jqT2pMvIV7FQQLwiLXkuVIJ5d5ooMVpVHjMxqZWnOBdlVVeMZu7lv0OaOSTynXwl4uQd%2B2taPQBfaROyk60KtL%2FFQfZUwSIgmEBwyLQLNC79oAe%2B1FgADAxMb9%2BKV%2FlGiOlmCsaeYZnjNNERTz064TITLeJOmjnbRp%2FbflpcZOFKVou9zIQIr9zLvjK%2BwdDg5rSHjxWVnMTdP0wxsJ9YiCbkZUSjXAaCkytDBaNAExMwWwEt1qx%2F5%2Bs59%2F9P9D7H%2B%2Bq8MM%2BW7NMGOqUB%2B3eNn5ywkHsGiLDNkIk7uJc6vnhRwNOB%2Bk4Rpj98FWU8RpMPA7TXg%2FBcw6DfBq0g3n6n3MPAsZvmEQMH2MOYsXY78taatks6msufB%2F1oJtukPu%2Fs%2BM73Ykd74eXDr9AHFTmz2uiCiUb%2BZWEBpFWb9JoEEoh8djgmXW03w1UG09QVdLxIjnDcM7D5FyGoGlWZL%2FI0meZXTNd%2Bw3KyjdJKjesJwcxr&X-Amz-Signature=e5e17384b9f51ccef164e1d2d2b815138ed06dfb38da53f76eec6a50e0b0c5c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
