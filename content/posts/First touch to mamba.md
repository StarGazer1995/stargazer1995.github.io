---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XQBO52D%2F20260719%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260719T045946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDVZUBsxoF0cPbcxBlAk8V9sIwsJHunmK%2FkANP9uqB%2FeQIgFqlFVgnnZOPS2UuZszvhOGDxYAwmPSAP1p7oUDv4qecqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDB384GY%2BrKbI%2BE%2B6hyrcA0kJ7YvJDhHhPZh%2BE9bjUy0l8c0%2F51U9Zt4afrrCO24djAme3%2FbMeLidYxfSUV2vTUTsYRpLuDsbqd2vFW4yUeqSabEPdSL0nRQjMoOIMQSoTfT7t5eO5mYda6BYgWfDRpDWT8t7pECb45wdXC935CuvKO%2B9FsqpCWYkdzsTXGRlqUwLoApxLr%2BAwj8nB0EPaM0Ja0jPgw%2FeQ7SXurhgsz5pOF5U5Dt4en9Z4qtTxPhXQaWshuAdH8foERSg0cKhO69mLLZjTkx1p3V1SflsTgHKT9UdQRKHkIMH1Vl6L3bfsApU1MMcFLwtUCzVfBIPfepK4ELxgzZt9S4ATeYXjS7rjGXjz70ty7C1OO3Pf%2Bqf17erT%2FGANlaqTNoMFwuLwcWPLB19KkRbRLQNyHQkM0OrVr4qhDY5Wpsd1x1NRWmQlC0CwfZaaa0veR8sa55mn3DuZVzF%2BFLUXr3HYMVc%2FOG0eOTYkTphDTvfn2fTd15W0Z77zOXklzQr3HCmWeRxds2OwndVYt6u%2BhhJIR%2BabmmkDsK34kk0jRNSBOWmBNbSPsNfab8NwMsSdxa8mh0DDVCqH4WGeiyLQhd1c9n0N%2B1hMQbRgmkM1pcrMq%2FCvD9WMhlRSWJJ5%2F3Bga5sML2G8dIGOqUB7%2FHl8VoUUOXV3qKNqbCgNeKwYV5aXSlTZ0nDupOZGwVie%2BK0j3A0Ib0BLIDXHsiDoG%2B2dNJzNobxr1vIGWwULYSizhsZCkwjx1V8wHBlkkI4pbG8pnCkhDNfvsvDfdja2L8Grs2ePQC849tip3wTnLlBNfSBpajNfnLLa7k5%2FWRFq2b9%2FhlRNJUrtujH94MEvGxeTiN%2F8Rg4FEM5Veyu3BDWlofk&X-Amz-Signature=c990b8eb4f965cb7dde0be12604e1f4a43da1d7be7d6b65e76d25d6b0eb1193e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
