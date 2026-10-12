---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VNTPKZZC%2F20261012%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261012T004834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSsRKfYxPu5eskFV9lP1AaeRM%2BdJFgafaGd15MG7g3%2BgIhAJzktMf82ySy1ZwyI8xb0plx1jAXRTY%2BE4Y9DxXcp052Kv8DCHoQABoMNjM3NDIzMTgzODA1Igw2kLrqDk%2F7cv5%2FQpMq3AMrok2U5Pswnm7nTA6Rhn%2F6aivZCNHDFFlbK30vEKWZuMKaAj%2Bcjta68tuB4iXPM1v9bJK%2BBvwOefNfRebkG6ub9cKz37vsss9hRtgZZ6hS91OwnAPcC4J4kTTI8aYaY5M6pm%2FkpGMNmS5aCq4BbqJyyoMkPLo7PCFMzo36YoG1AOypTwiEi8GqDfi6yHZXSCeIFUm6N8G11u9OLIplHyq6dz9LVLQzMuF85QbFQW7hdlpOu5iRelFAN4vcAfG0zYYcrERo%2F%2FStze%2BEZNOKhJ02AaTzmzfmrbl7V%2B%2FTvgZQbB%2Fc7JmWCZLJt8kyOJ2%2Fl%2BrETiyTnor8DAv371Y9zA3g7zE7vocEQiutmyQQ8nV%2BaWVMnBy91KPDT1iSgom9oVO%2BXa25imt3Asdz3%2FGmHjgYsyKptVqbHqoSGPSM2U4wDM5zveV8K4EoPNImqMCfKO0dD1AsM5ZaRG3xLbRFREFnvp%2FPNb%2BpL%2FjMLmy2HLZlH3U3ode%2FX8yifbQkk8%2BKelpNlne9Y%2FFkTkp6qdBuOpnxrvGsOKKB0UR5smWioPE1DFNccyKrd6xWkC58TJotXplDcxu7dl5QRkiIcmnUCnN%2BIZBEdnjqmYPBK4B2BadZcDQXXKrvyu2U7kOfvDC%2B1rDWBjqkAWXzkbPOIyASfESB%2BNdfCyFqhFM37pPKM3NQG7sDfTocYFHMXZFDkQNdBNwifw1kj2fhD4H8yVjAbrC%2BueqsoQcz8OcUvDt1yt%2Fgmpdv9budl8lBt1zJju%2Br8LNqvV0i6%2FzEOZJfXH%2BwC5idfXQYExlgDC7wTP9nnfSLGbsh9EHrgQEyVKprqv%2B3UJwcnokQL%2BSG%2BhUb29iY3Ln3oEIcDR%2B3gmPy&X-Amz-Signature=bb864ff9abd8938b7a5d65fc785b77c8f7e6effadaed9053d6df5d006932121d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
