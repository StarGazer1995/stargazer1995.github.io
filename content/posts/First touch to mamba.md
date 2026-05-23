---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZX34FVRD%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T164718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQD1R5Rfw4OaAyYzDSLtkdQAgL3sVq2yKrkpM7Lo46xjDwIgGel8%2BstmT6qDr18bg49vO8HiZZ9i91ENrbiDezOCbaUq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDMa0JFnWLR5N1RSSpircA0VoehM1CooMZZ9RWqar9o%2BTxppH1LTe0P9ACNBhEPbHXcVTwyc%2BHr3B5gXH%2BbwSAehf1bFseKWdeA8pCG35DfsyLfq%2BQzFNzC8xzlWfh2IAx%2BAsxmnOpU0OPrmGP5%2FYPLSXZJDPlOTm3qz%2BM9TO7gwdBtHGaRI8fUJHhYMiR5PpDhS6sUXETZccGmPcGi47i8AnjezpqhDVbEW9b4Pk2R0sI29UZ3x1kFbPHQGDLa%2FDdJ6eMB6DZ8UdRWuE%2FzIogjdBO9e7cT1HiRanlcYiO5fztgfcLcTfy3oOfA%2Bt7ZDpxnmLJX26EJeg038FbofleCgNHwfLIU4W8tBGRxwJI6lGmDDPwX5nqYIGhcOX8uQlO6z4vJwJ8aFUAMsaJhkIN9cF%2BYzain8yCwYB8%2FVERd10OncV0fT2L4HmaewNSnpg16sK3QM3CGbYvOQ6q5GVaM3eXurNXdXEcSUFxSm9ZAxGnntL%2FeVg2nXh7ldzrA0m8R0AoxPlWOrRKb1TLG5JarUbdb7ISDxWtdl5OD8RxqbYeoRi8niCY18sAkVzkIihvyBigSsAdy9tVGFMtQ76TjjMxXlawT27O2r%2BwTn5Xq9qkTFHH46eeeDK0aWXFwtu9x4PG256COTwAWnvMLCRxtAGOqUB9uMExHMA88I%2FqvFXG5cxF1SBuHfwKUlaO7Zaa7ArjhJrLUdIbPX7bgOg9Cy9SuJk7RUcwp%2BhEMvfWhH95afpO%2FWcq9pKMKme9GrkTR0GIiCzDWtTJVeFQlu17Yku5kNH75YURTFTVzpKT5rK5GzPIb7oQN7abiIPIbNtMVExNgCMOoPqZ8xs4fOoQkXWi2EJ979UFSuag4H1nOs%2BxRmTDkBrSSDS&X-Amz-Signature=eba143f6bc88f37166b5e24018a16d39524443e5e04751de6711d5bdf732c821&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
