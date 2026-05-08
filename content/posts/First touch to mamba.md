---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NJBPHEO%2F20260508%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260508T071507Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEUZcDME8c69TTL8hwVBc7IMp%2FLF8uBclUfAbJUMIPYiAiBYJq8opkQy0ecrN8LcDG3yg7hGdKHkWT7hKdGEVGA4ZyqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPclJ%2B4jX1zkQ%2FmiWKtwD%2F%2F5AHIohqcMf8tNEuJPPfhbPBm8uLXscf6pqGiAp%2BhPLrYz7LgZYq4QofTgNDgBlGEVNPbfhIop2%2FB93ko9SazSgWWAlUxqePiWGyguDEgnHiJEM4DFHMZg7gh6DGOrhCBXk1zQm2YYOWVqNvDASX0m2zr3sf0cHsHQVqj%2BTtCL%2BzaukvufQXhrGgrfj0KHoixVo4BfPewIopTsPUrFAu5cuZem68iUkfTmZ017QXFH1oZCt6uSgxC9a3WHMrAEGVgFY%2FD4y%2BzAzKYR%2FConXI%2BOBhMoB5Qt7%2FAPnljnl0A5c0fpocZStm0pa1sm2u0ex3%2FYAIeFszjox0XpJIvEurtLK22MIPAx5BmuFuf7omxQ0FupIyJ51ym67jM8LVVZ5ckni%2ByQVvxGeMq%2BC0j1TmiDkboqkaiG3y4dThL%2Bo46Qm3HXr8vNY2nxhhmqud3CftVAe0HEM8oHLHA%2FbCxmtlMw0qCIONCnLEqBicaDVblJ63ZQu3MRAgSDpgsyXuOO9xGmOrOD1Nr9CV%2BLJDux4hG0j%2BsUfVS5tZJaFcHphE5vySM5e0j9K7eEJF0ZTg1ShGNRl%2BJfcXFVOM%2FIvEkZnPu7wY0%2FBwSYc3X8oswdnHlNNPgYkK3kH0spjC0Uwr4D2zwY6pgFifnI5xjWWHC8VL4Pjj4I%2BYEDIE0YcoXRZ5WdB0C4cJ07nn%2BrenQmvLXN2P3VjrW3%2FGDf461jL%2FbDoDhrSrX155v52%2BkbqhOMqnT0JyLEglSQt86G8CvUPWs0qe39z%2BxMxkhqiwnC%2FnY2j%2FTGRg010aSCnU%2F0VvkZxi9fttam3RTil7KP20piU6ZwSfBd7OKhbcH9f5cUsH%2FQpPQIZygJilEAT1SRN&X-Amz-Signature=d77c6b5678bd2141d9086baa7a264b71887a9ff4f6b41fdacae96d373887e52d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
