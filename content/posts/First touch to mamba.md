---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQBSJCF%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T201614Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAgxGm3Y8zQ8o%2FrX5ARe7%2BL7kS%2Bpd7qf%2Bvumm6aPaJLFAiBHtxap%2FKAkr%2Fk2cJNRUnzkOtSt1d6HMhwAibCozUmoBSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkIH2WKFcyVIggybIKtwD%2F5bZCuYzwCCHI6tXDYFqQbLBa72m%2Fk2L8OPgY4Mf1sN5VbH0GqZRBn9hCpzea7%2FS8%2Bw1c8ke4tsC%2BpFmLG52fyl4sw2ljVqGTPo7Z8EFfxACGlg5W0bZKvjYq8vV0qbKf0pzdJSgRzsdxtNEP31fM9TAEjcc8LgwU%2BKxiuYRHepliiBcD5ivD9n8IGDtsjR%2FP78iH7AtUPN5rItzPz3LAQkJe0N1bCRXhan3zIJonxWknQc9OhZhu85mQejsiVTL2M95%2B7XU5TCANjE1DXZokuBhi%2B92V7cmIOUx5GBZlcdh9V3zFcN9P4oFTB6xIGpMWwB9q%2FgSIAkDPJyEdTDwGk9OcxIg%2FbpxPhKCIEeji1zv%2F8KV8IivX8bDXwAcVb7vnqQFsZcpq0as%2FHxBBG%2FZGLdFDbbmPUrACU5KJFSI2TRgTabQx3YhskjII1FBUAMM6ii7DneNAh0XSaLUDUEI%2Boi53A5j5wwOCi6VMr6qftx6TWxi0VgwXUh8e6GwrXlzcYibQUQD7B%2BdHhYIzmbV4vGshH0TlyOL4Gmpf4fXqtNqKq4xA3w4szdQOnykir1wUqDKoM%2FhgzKWZ7yUgRWIagQXd9cFL3cB5SX7%2F9rIE1%2BcDEVebSVr3J2mFIww56Od1AY6pgEobSs65aM29CcS%2FPbzHlgFRYuD%2FNgnnU4HCqcLjbn%2BsAVxwkzAjWQSywe81spDNL5BAGBspdPsbDwP%2BAwIrc9uhhKPsrSWLWTA07z5BqWGynL61Cvqyh63Mb3ZC6%2F4kSz6y%2BP2OkVoh9viTL3BKCTYwS9SDxNyAwpNg4MHm5xMBr3lMCGQtNdNQOw%2FCrxqDdWjXnPn3KofGeG8bugI4P0G4SrZ6RZO&X-Amz-Signature=c32167b10ceb77c56e2ea0384f954b8bcfba3796ad7fb855fafa6ce3e5fbb7a6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
