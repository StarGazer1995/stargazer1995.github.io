---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX7DLFDY%2F20260731%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260731T115213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCNeYBDSafUQ2niybl1DmroXqX9cMc%2BpeU%2B7xWfoDWB0QIhALE16i9xtjZ%2FsEMilY4ksa6VgF7CGaRNv1L1%2FiW%2F0m5GKogECKz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igynor0EPhiqOgany34q3AMBCHSBCGNEWZVumBF%2FmUqvLDQJoevdCmYwmm%2FOaxzJZkyCRY6yAG9AaNieaBrEBni0S6Tm9MN04ksoOZv9eT2GMkgRIlKMbaYzOAirz2dcWlQy2G71S7Sh%2FkzE6XId0HTZ3SIcPHzm1thGIi%2FEbbd3S%2FhgJoBfF0DIZ%2F6lPV3d%2FqmIwTc6qKAeBC6C0bxQS6cwuNkGJWHXmqeV%2FQGPkojLjHZ6oVVL5vHz5TRCFKerv7Mw2PK%2FlRcyb%2B%2B3udASUvmoBRv0tB5V8%2BwJe5M6YFPnq0YykOMOXEdt2%2FowGZ9DJOhAE1hWUOG%2Fz67HqbRVG2q1yoX9UkITRNjE%2B4nustyycFdYdxIOzn1cKaSpGmwSGnn1E%2FXuZR4jfZDmnZPkHPulmAwQCLwz8efii71D%2FWqc18v15NIQujVpM0MqNZz2V2WlvaX0D23ejyVJjNisNA8dbLL5CY%2F55wlvZoqFb7K%2BRh03eLBi%2FQhOO5Ull5Jl9%2BmJLTHix2AC2hmDJ1jx1ixofqYA6E5QT%2FwqBZ5tuQEMV6n%2F0D4X48AeaqXa0JLxzfX%2FEzvV3eoVrwenPiuK%2BYDaw9l5zayOPbYmDtepuSBfAPRTuuyqcKOB19VilUSEdLKjr95TNxcNeu2UDTCog7LTBjqkAfUTSBsMyzQVCWblQ7w7oX%2FQRWEqRLsyOW5ubvBJUeNv3rJ6zb3b5pl3ohhMwlhulKYo1UJ7mQ5W5ZFlPP%2FOo7TSCnbL4%2BDMHL5Me%2FdcPh95JbdnHqKyiSxLW9GStkIH6N47taHOnBhuI%2Fv8wn3%2FhpmRd9CeFgexbmEt9weMymW1chFLO%2B9vHcEX0XNl9DgCVfxF5oGQ0eFXPYtQsW%2BbIF4oA6Uk&X-Amz-Signature=fe4594868a81a7e94cec79d02bd8687d1286428448b8eb603a6290e510848c42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
