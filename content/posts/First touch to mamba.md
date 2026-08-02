---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667W2XSUDB%2F20260802%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260802T080141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBAaCXVzLXdlc3QtMiJHMEUCIF1FVT%2FawVxSBXzcwYS5LbHXFn2oqIOp0BQwBLuUz%2BvtAiEAjrdzVjqRRqfuV9R1GvITUmI1YxDK2RhEqpU8%2BqCOp8UqiAQI2f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFn%2FqUds9EPsYCMkCyrcA8RvcHz%2FFm0KhCLU0%2F68h13LzXuAIEfcCTGV4WAmLKEzgcZNXs5v1xhn0Bfn3ethky0h2lfz744P6W4VcqPjeUO3VmBLqjO%2BUIX7bbfo6oJ4DQZ7aOUKqibBOJhn4AgfD8QJZRmF1yheK%2B0BtL71nOnDTk6XI2vcwlJgOGNO5meJWajKovumuycqniyb4oux2LxhktEGyhKHp0asz9LbAYpo1SpVFbPpG6wUR7Vfg36OrxtsRiAjis2vdYbB%2FB%2Bcg5cKjbcmRokFZamz27awEQard6Wn5l5BuCF0VZwx%2BpjVx0hVGomCrWIpL9ihSPpvq5RqnVjbh4b0c4bj0Sjv65EPrnDrmNPvfD2Cju7zovaL8osgQlJYo%2FDu3qo9vqhoG8VwAntXRM7zhFKBHgwc%2BaSsvPDLnTOC6QwN2s4iQ3JnD%2B0ZvFaRXRaTdpGCbHVMnNABuHye9oU%2BGPe7yiq2elNfYZ4KdX1SqIkCF2XGNgkN7qg%2FSLHIQdciCVNYqRzPYoDB3a2sZcMQhxqZvhWtIBbtL4NGD6cXbg5%2BdID%2F9BzYf4fLYXJwfr9rbdBGIbllVjzkf5bEQ1hPd3wCAPMxO6P4Wv7bOFfR5ZSw8JHbYyp6tttAXHri0krFRsIrML7wu9MGOqUBUZRtlBw5gE9cyIDNFPUA2ftNWhfyruzETcJCHN1BsZhlYZ4BgrBmV9Wpx48c%2BbYrIDUGcZUlCumCdFHWeP4s%2BZc2tsU1pas2lQE%2B8RQes5cnZebRBKo5tYpqxarRYf8KgxuGKq6WLOcIsaAD%2BgjqLY8vWhQmF%2FA4pJe9gfCaovXFIlOFQUYHwP6zZ3UHwBHym0kF81c7pF%2BsWAbgQXAl9k0ETAqs&X-Amz-Signature=e430eb05b8d85f106efedb622325e88c90f103ad6990f83f4bc59d4c42b5c932&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
