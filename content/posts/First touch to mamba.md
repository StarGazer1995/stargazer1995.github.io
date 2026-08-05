---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UUAHBJ5%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T224749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQChcF3wDdHJWdA1ZFdJAgesTUCM%2BTOIsZ%2FAbe6Fh7vdWQIhAIdMKVIbwZC%2BRklN4WBfIrSnDLQ0S3TdTcoYOG77siyXKv8DCC4QABoMNjM3NDIzMTgzODA1IgxbtlPDxQn0cgLUzuYq3AOCecVwSWtC%2B9%2Bb5nRSiMje2dO6la8eTrFjMIIVL7zOaxNt%2B1eQtgK7WBGPXm6l1KFVwzUxq6S7%2FqyzWOhczE9q53wbj9gvuquKCuUk1WLvv34hVTx%2B18oPVI5ftBEfn5gD97TxcILSYwSheGF62minoMG1AcAbO2pIhlBwKdDG%2FLz5LLpppTXEq%2FZrfs8f5H9r8mtYD7Nqrxb9YOPuOAs1TE8AJRP56I757VBwQfl4CXu%2BvBrvMrhQfQ%2Fc2rl9pd%2Bovf62XRfsxpOeOZ%2F1wC%2BFm77T%2FBK4qjp5gfJArUT%2BoZf52ec6fkfg8RtfA2dlZfdDT13RJVaPfAhA5QNzLjAIBA6PW%2FahTkBqd%2BuWUoqmpi4kxjGM45ZGny0EuTc3oxSBVWjgMoU53eW0fzmA7JKAP6YZ3lGZ8vO%2Bz8dJEYk7p4tfmwvhjh4V3%2FPaQ6cgaMDfqwDmFddDUQnVlfC38l7MiyW6HhCgYHSX00SFEn9FFkzeDuOpeIItHqb8XQAiZfTCXMPtJeTYQbCCozgkU3862RYvDZDvzVgIn1d7Q3mxVbDepRCKU%2BlU%2F6AJrAGco3tzwMG%2FIFIDQctIlGMoCLE7%2B21i4F6CzePTdKkNc%2BfvBO8R%2FIUha4V%2BDq1yyTCF1M7TBjqkAT5XpdcDouTdepQyUxlFFMD9ijIqcOOZ0sYmhEyE3%2FIBZgpMcoZudMflxR%2Fdn9%2BkB7ngZuwvRwHsHSUG7Ie9AkMvnQe0uEcVX78OvsITcXDdjtgaIT23tAnpMkZQ%2FqSDgNSF4VjQIKOudm4V5Pz3XwWVciCeyyJofmfuj89wUi%2F6g1NRmDAD1kan4C4u7%2FZBEK7pV2Et%2FAd3%2FbEjE%2F35%2BRlOa9n6&X-Amz-Signature=66d731c86a46dc994cb09750353c669f2c489746a0f610b9c1ccfad0621ece1b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
