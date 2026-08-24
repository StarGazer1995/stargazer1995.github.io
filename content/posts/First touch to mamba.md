---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TXH4CR5D%2F20260824%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260824T122752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECQaCXVzLXdlc3QtMiJHMEUCIQC5chdzhFIdvYNmzGox02HDtRFGTNfgy1w7ucwq0wT5UwIgJPAGdD8%2BRyaO%2FwYoSbMlwVxC61gMeLnUlOV%2BJb8iB8wqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGJBEdn7xvSs6%2BRs8SrcAzJ%2FLy6aHz1eTqqleCiUYHz1VtS4fCfGeB88nEUmgEvGDYg4YvDKhlQyAegzIj6XFTIdsj5beXv8dEaFa%2FvI19SV0mJiA9nlu5vf%2BkZZc6IIoD7Xz9yr9ip7AIe62y5yB7kHVcycuR3Rt0vtVFNCWLM0hJkLVvSavg99y3%2B05QhEKJHCNWagi%2Be9Cd9ft3S9a4pVlw6j5CO2TWz7y11xxeEWzhYt1jwjkSLBlvpG%2BBS4Tg0jw0LetEADIOyrVQejJyYqjk0BhEJF5qHv%2FnFi%2BHMLZlG1dAcNf0VCaT2mjoJVabWHrt2z29jet2bNU4KISfaPyLqNsjCA0M1dFH%2FZ90FQjpQkPrVR7YZ8vvemErk5ekzqsgjEDcUg6FZaRGAPH5dL8KAzpl3IZxu6v1vavD4IPA%2Fe%2FGifflCdy2z%2FV4OKX2qYe%2BpsWm4Qmyt4CtWFcb0SDWAiT%2FzYnARBVNY41FfXzJMCzdTPwBLTEJIPCFoYy62xZVYdvRoOkrHx9VQ3UxwTMYBlTnekKW7PyTRWL8DrOOsNh%2BCymFzRDa4sc0KNmKfhCcmtNi%2FEkt98kjTOdJsxTQjcgHHq6eZMi5xodhx9UJo4nC00KZNNx1ncaCUCn6PRwN6z2hbn54FGMPDosNQGOqUBP6Av5ZgQq%2BSk00AxmS4PyrMyUdYcNydR8JfSOmdQiK2w0Ax%2BhLQUzd7XIWfAv5MGaSBGNbQnbudtV%2BOb%2B%2FKm4aTKivAFGiyevSD1XfWPrMsuDWr0eBa%2F344wIhGmpeHia8f77txLYscwuErwhFBjNJMJeTuEH0XvkRHmWoJSlgURhydDAk2G0JpZvbv3zNF3Umeecu%2FC3%2F%2BKy2xON4FPE1jx%2Fbuy&X-Amz-Signature=efc1a869142ac2b4aaadb10ac60bf15cf30d7afbd9ca4440a49ef32c43af1435&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
