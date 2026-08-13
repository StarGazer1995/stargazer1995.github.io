---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WO6FNVEO%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T184600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIHqLO%2Bc4h7KbGiQjaGMBUivmjtwVCHimYESlX1lvQsy3AiEAmzMRq3IyLJyhWHuTUXlhKuXVfTumVp8gs5DFx9hHnKgqiAQI6f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJbEHU37ICQuL3MOnSrcAwswtZfhyXiY6c0B4PaGQTewcDtKAkn1PwEqHjbYI6KDWvVArBTSYP3%2BsvEn44fZeWfykn5OpkAFq8oGeR0lQN7PrdDDJDm1n0Ogp4OfCx%2BHqGJJ7gL8LNSw8SabwFv6esZYh12%2B8gPy1AEMdWTXHUXI32VhuBagOkh3ymiDk5MzdE8qARFuRGKYtuWoD4oJDfHd4S9ZazqDLk3nJo7tCMmM1qjdiEfkcjTcP54OWvIvCWyhxlv0QgEA2KpvyftI%2F3XXz6OnrO9QpHC9t4b%2FXNFNuMXDFMR6dK6BOofA7LsYNcUrb9I5m5NlnelKZHPFKM%2FQRDn5hXTvuBlApx1r0cOkfrmPiGh0U8LK9JHAufelqES3bwgahKFTxkDaT4d5foTN0QAiEeumYQpVwblv6NwT%2BrBlkpbpMfzEdtQrOUEG0FaeOh7f9Nuz%2BffjfAxIr8n9L%2BSrhhSv%2BZ05eNfctqlH4QdGCuQZnThDvID5RwGo77fvrD45nqQud101RKeHJK38%2B5gALTKk8rOHcAGtonu9QhP%2FvDFHZcgxK4Pojda8qlevVtI1lwkk7hM5h%2FB7peS8kEHZo3J5Wz32OkrnqkL%2FNXR38FBVBqMNJZea5BvJSlM9a0sNATeZADA%2BMMTb99MGOqUBXDs%2F0FcK0ahyvo3QzFcykN3BnNFj5bO5pCXQ74R%2FmIkdHuLvaEHOq21QdJxwR5nw6EWyiKBalphU1fHEtvBD4i0AY55wNuHtXLvuu%2By64awzH67hAtNadIAuaY15hqlhoCFVDXmBH0toRG%2B7MJu7jpZqHc%2B%2BHxWQznrjzJKnqJRLxiDmH1HwTceHNSzzz2B6n1owCmRYnVOGH%2BMv835SZKtpIyo3&X-Amz-Signature=7ef7b1a53597fcec9ad5cfaee2cb6f8d613d8799e26d38bf43624693d91b3695&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
