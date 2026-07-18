---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466366UV2W5%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T223733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD3bfU99%2B3Uo9soJTqhxFQEc6wWcha3mhD8njAHYXwsugIgZ%2B5aMVdUypTuDlvK99434V3Ltg8KMy72sKVMumgny%2Fcq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDMikjritK7H7VR2mgyrcA4kjjZsVlbxwTZcAvKNgus4rIgWTpTCZN6kfQoppvIE6THbEVOAmMxvdfb%2FAYcDKpcNiMMiD2tMy6jcPrqXoHQchFGd%2BdATI%2F4ny0RQpCv157pF8uIB9SqRkizRooz%2FFyitqOpEdYw9oTCb2Wk5fkgWIuGAp1TTKgMynBWwH3OTBLYug0pk9yXq8JHsMm9LPuGLfMyrA4DFkjpzRo31zXdEqohchQ0hD3ARRA0%2FOaHV8mVh%2FZ%2BsoFwvXV7HDAHubiqmwLRLgdv2lsRRo7AtAfTIOMf170uhDlDGS85%2FJ8%2BLqVqgj%2FYhFkmFGx8taJvoXvX575oFC9EcXZTJi58OWjWyQrvAWhWrcSxK6LriUldnyio7sYnCfgHUCfcujV9RlutJ7etT3VptLmp7iCD93qkA7snr93qmvl8KlfZy3cfCPjuvmPARDBNgeUi9hZ2CwGOPfAyuS2GhOGZlE%2FabwYmFMFEc8bQugaMAFE8ztxAjKLLuBPoEjg0AVpOPTn1RwWBVkweuUbcYpw4NikZ0wadPAJ4x76js7j9RZ1NlfmmA1okjwUvf4iW4g5S1vxXGCrBnt7snJP4PMWHHinlQ8leqTTM7ODGWaSphbEfnhjFDikUpmiwV5Aud0RMjzMIj579IGOqUBfX2FPVyylQSO%2B025A4qvIFMmCoiL%2Fs%2BLReUxShiWGncaZf2RoVcQgRfxwkRtJkybXJzbXGN%2FzRWUStNP%2Bdke%2Bw01xe%2FnQHBztI97na6Eo%2FMcl1iM0n7owvMGaPrMonLl5Y11k1l6QhGcXQZUanxchoMb7SEWU6MbqTkJaDQ%2BAVuC0glwPjtYtNn377nnSDmEUoGFXg42kDqNd1yeZVqwvTDWLMC3&X-Amz-Signature=1f546ff644ef25d52f95059de752f9a18b74c13834c781ee0f30d3f0e348fcfc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
