---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZY46L3SV%2F20260627%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260627T015911Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC3Ebgbe3ThIuiNq%2FSB%2FLtPCF8THgRY85bbx%2FJlsri62AiEA%2FVaDGda9eUR7%2BLyOLr2Ucd3i4vZ%2BElI5%2BzqG9mVM1%2FQq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDCh%2BBAlVLbw83qPN1CrcA52fb08501K0s64lYBqyFV%2B33P%2FangfX0Vx9FpLjh%2F%2FARiNfIrySb3lh3dysdS9MSoQ3upPrXsseRhAsfLvf%2FHPJmpFiZ6jUhksk7zTvbYyifkAyPePm6j7DsVtc0SqjUYcK7cAN2H1yYpdffOd7iVUkNwkBkbAM6jXFNL5mvceGf%2BQghgM%2Fc3vNx3FHhPNFUj5fcvakLIYNGiEwpRR0Zkk9TS%2BHFamKK00W65%2FemYYZFMALeWDH2GILMtCaDNFQ4yCD%2FEBwVn0%2F9ZVon5UlOZpYPiRqSZVrS1lL3KfV2TFYFougltLF1p1v%2F7g7175VLscGhn3qoCw50UtnIxUs6h%2F%2FsFnAx7D19rWIgXXV2UIW0K3Slf9KsdQaVVhDkwZZK65qNb8I8U2fHz74wPBPbhb8MOF7GX%2BCDy2JSE43fNe1nYYi7w2%2F%2FfvJp5wLHGcoqEtyFbVpg9j7%2Fjwihjc0grvmPrVNWDsnGdYlILw5m43S%2FRK0mbTTdK%2FPYuMxOXQT1NHjr9iYcEgDmxNpKoDLQ65AySwzO7%2BKCVuG%2BnkBB9SjgbhgLKg03W5GumixU60YxXfRENza2GF9Ccck2k6LlZGBTUOzgJff7GjvE8n9tD2BEg20KkdUMZz4AaP7MJus%2FNEGOqUBfFwobjJoIgftR8s%2BO856W74PovdoH13gjVfvkhPTpD7kQMSvRExqTAF98JIjCCaHdAzTPMgX%2FtnqAQzVOJ6N9hdksqSK9JLeM1z5QFVzSgYEyRauiGmedDpeaY%2B3QNjOql6Qe39K0E0LNYcNaGBAy9ndbA0S0iRAiiZ95BA3%2F6yIC3%2B05gpqRTti1I940X2vC75IV9SogpKlRyRhyEA3WKoC6xlq&X-Amz-Signature=eea37f062da6d6741ad5fb5eceb7bfad39bfd64642de35d69495101cd87931c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
