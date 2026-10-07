---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BA6MOKU%2F20261007%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261007T145115Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQD8sOm4f6EEdt1d75Z7ygC4yCs783HP5HZdBr1a%2FL00YgIhAN1YsdMioDbQbAfGrf6ST7FUrvmJlTJHDNfrvu4qqVhEKv8DCA4QABoMNjM3NDIzMTgzODA1IgzxDMb3uE8C%2BbG9Y8Iq3ANBkjMZ1L5pEkzM4VvUupWVwpowvoJmJ%2FpPsgDigXBu6Lazld%2FWIFLwsFGrUyCpd7bRbJLTKV4EBRJnIoXigOMbwrvyq5QtSI%2BHDLoxFFW%2FhJ5tSMqNUqKQIsetFSf9Wr8PuzaHjA1wtcygUb7gPAw8bQA5IXgRyEUqnt6%2F1AtCF918o9%2F6DPbZb1Yab%2BmcMu2AdHIXgww2QyQ3YlVpvmKcOp7ksAkLY6T4VebnstFjm1IofgWv24zIA1vWKvrAvt2CAU59vvj5aA4W93c6JB82VdP6kW0NoU6qQM%2F4nY33wG0arZXufwLmjO88pQsr6NA%2BpQyNqZoJx56QiB3tnrAVEcajDSEVCIKLAcdY%2BE%2Fqr7uP7R4gRMc2fgRMKn9b8HhvrXFNEfE5jywZ2aFC6zJtozyXSmKEgORUB7ymCcFzdYxOlEAAnQ7ZN5K5cmHjBcLv4bORp%2BOyJbT1U64gWdbw7D0j%2FTBlJVtZDT%2Fs2X8L1mnnFfLXEh8HboBiNMyx3AdSJnsvld1TI%2FHniBmMP1W0hIVuaavQsELmY4Vsa1YSnopsWHtNy9hX5dq0BnEsYnNWQxDzc%2Fa5pBMN0QZn1yHb%2F3e2iXC9kPn%2BUzeKl5Nm70PiwZIxIoyvWSy8njCfoJnWBjqkAWGe18gvZNTr%2BiU%2FZ0UNvzoGutx4A7RDzlO3JW0onUQbq2E6kLHiLXUyTxzdYjYjUClgpf%2BHQq9c6JkHM0z2xZRB3ljelUkll5HyZTSX2KZzIHX1WWyrH47T%2FF7FZDuZwvqmSKMlyzZgnEJOPBvSzZ6b7VfV3MIbxok5SM%2FFD%2BzQ3fEuS4v84%2B85LAItyPEYfuc2krdCQ01q8OT%2BYcdPSvk1xPn7&X-Amz-Signature=e4bf9b0581ff5b60d4318f7e498905116cf1827266005d2bca6e45d823b83d43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
