---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDJODHXP%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T074843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIAlux7qhrUNh1EAlTYD%2FpvgdOXpcmh94TBwBC8sxTZxSAiEArkxkEha9pguJlH6daN3woq4xvBJNxEpiQzMQxOCNxvcq%2FwMIGBAAGgw2Mzc0MjMxODM4MDUiDGsM3yza1TKkmR8sdCrcA1N9YdbXCKNElda4jrZeOMNLSW3vGolXfAHxTupPaV6XOxM%2FSVBUwQ9L2InhgqkKaSMZnRwKAT1%2F4hBkikJO0HvkF5EB0YB55JPRfm29lbFyUpS9UenFUlM00AOGZv6pS3okM5rXRIrt94NVv8eAINz6M1IyYWzwj1skiTx5PYE32QlkP6lU1vMmdbNWdPqN4CdGm4YTthqkZ80xNY%2ButlJv%2BpBuRKiE5DF68kjUVMOWQIp4b58xdqOUepbK7qIbuvr%2FI1Z8QNmbueK7oR7iwVgRDQ7lANmyhFEzfsRQ2Xo10t9ySCdt5JOmGsTxmFefnykvwMekTV2FEIWgGmFPTb5jzjEk8rWscmD%2BF1ayhNog1Q9FvndiqH2q2vExyPA9%2B%2Baui%2FXu9ewRdRraX0M7ysqJRa%2BtegoAgTQktAY5YG8IyfTjSqIOsoblwhgsdlITQIc67HIuwKSTduRD9FjPFghaTj9kfkMryEKlYnY%2FE%2Bzm53upR55WE5FEVrHRZzO7Mtby%2ByjpPyJEqE%2BDv5r27yi2ezBJQ%2BxbpsCXFBTKrkyTgYsp0AbIKKB8q96%2BnKjFRiolQDuG3CkewM7wD1HxFvNELBKc3WMx9N6lMACVmmAvf7fw5B0EsDJ2yrHhMILFkdMGOqUBEqSJU0mKhKPg7HziU353d5lInnOwkQIt%2Ffz%2BRWYD6LdahMnd8OqIBtskin9RilgjwqqTCF4QBMNvkZLDvVq16DzSjt3m%2BpyldUyyfxRQGezXsvaeTuqFWw5Z4lhfyeDRiy4CLKT280bd55suJHWtvQIZu%2FivPBuHhstvbOgeZ%2BuEpbOxV17CtK1Sg3nMQJBduaEh3ByeBcbgOxa6dgFnSA%2FeVHcK&X-Amz-Signature=18f0c8b0b29d254ec9063f21c8e43ec429af02a0a2bf92667cdee56f9607ea23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
