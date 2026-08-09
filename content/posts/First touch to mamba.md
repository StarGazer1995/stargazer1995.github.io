---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OSIQT4O%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T082857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCvXrckgx33iL16w%2BjiYMEpogxNzNZtndYm02cTV269OQIhALu3Gq8LK4b%2B%2BcLETpOZVx1y4CuDjJ1KHVIkuifFyTvLKogECIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxMxnnSKo5cG%2BObo5Aq3AMPCsuslBmjpjdGsTIffr258huqDgf8%2FfI%2Fn8%2F%2Bz1Cy05Gjcz5B%2BPuO6ZhLmDORqINJkkr0zu0OHyFubw%2BPVzi%2FKzt16L77tyrMnddktj5ABPYYkvAwf3JKGCbiRpO3mggi%2FMyBnpfbCEyyoQuPIsGmFZKlLYCF8UqXy%2Bk%2Bfv6RcTdQ8dIoe%2FSMyhZSoJUcOs0hv4%2Fpe2gCKsu3X%2F%2FHLsZaTPOMvrX6vyiDdrVyT9h04lnmfXjFk0S57iR6avniF0x60cea%2Frr%2F4fFl1huXc%2BEMXzdR7Z8%2F1DO85OIrP7PRMy4TyQl8ZAWp0X2DLFxEUmJ7opvFNL4o%2BRO7sKZvnP8iVEI1yfuF2gmV8186suq9cA0ugMru6iaaDxMXXLJGKA3MY49gv%2Bsa44Wd0E%2BatzIopI7oGwJijnqaeEFHBc4CaJOlInuxssBVL82UCLzxSwfUWdow9v1sUxJnBiretJ%2FRD0%2FS1mTCh2TAktolTjwnDCCqVk4J3XAzGD%2FHZROgJOBNc32laQ0X9QFTcEV9O%2Be1Yc%2FerjL6B9C7aQx%2B9CdCqCzHRhdl%2Fe67aOYA36X6Y17SiNVrrzVYSV2RvYA7dbH%2FjOtMZ52J5kmDDOs%2BrClz%2BbzKdz21cRypijNV0jCT8uDTBjqkATH%2BlPBLK4yyJF12%2Bepe5Z6flMa6ZKORwR8n7kAuY5fvU53HHQ2MO2ewhn0QTg4U%2F6XKSesrSQkcJhqdfP%2FNrOJuH70fYAjo%2FIHOYMMos06OlyCZebiwsGpNzMjS%2FK3k8pwMYC0wW9zY0azSZndI%2F%2BLlgxpLwL2XXEwkPTNW2DZKQimzMlcFxLa4J7JR6aQfsBklXjt%2Fp8bScLkXYcnloTjoXNr0&X-Amz-Signature=f787425331788382d7e6d94dc7b50bdde699b76ffe078e1f08271fa0de270c68&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
