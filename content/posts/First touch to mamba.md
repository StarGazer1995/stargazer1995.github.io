---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6VVZ3RO%2F20260716%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260716T204412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDZcZ%2B1eEXCQEz46oz3MlNlTbpJzTuON5GmGOg1PzHyOgIhAPc%2FM4uPVhRx%2BW3eKdSd2GWMrhjeCUgKLz4QXbaz9QFsKv8DCE0QABoMNjM3NDIzMTgzODA1IgxisS2gQ8iY6DwQd3Iq3ANOpGkmfLOmZtnWWiVu5XBVBF265fhKZkiLT7R52b6EAa5vjLhQ9EMqBnOUT7C1hSTMqMCNlCFmuezTW82fUvHaqCvL86KK5FPxlSD%2FdE%2BbNTDEnxRLXjaJyfPqW2%2Btz8dPtXWuQ1Q%2FHEGp33IU6Zga%2FKrwWeCaaawNG7VooT%2Fx2gy579b8BfRHzSMEHTucFZI0grkzIKaGci1ocvkkdY5Ep375mKumK4u2hWccbrdmrZ%2FpRKoTN6Zs4I6gbG4Fo16O22gHhEEOPb%2BwOK2wBcR57%2FsUBSo3F8ZuzPtHhK66WLAvmZSZrqmPfv7vysFJj6Bt2RwrHQVZXZ7FzDAqVuZsh4A2txTq8z9ginfMFoz3W2qRf9LNRHlDokFrUXKbFmZVtGppI4rgKvAozkdaQ8aKX2RYyN%2BrgQLK%2Bt6gl8jaVKR8NFVMtKfE8PV2QPDgZeohcOeaxlKiEpkouDtry4Jw6VRKmhXV11JLe4yzWUQOEY93fEuK7MPPe1huKQb0QS%2BT4guUTj9X3lVA2StI9tEHzUq5lujDk6s9aPN70SRzm2Cva70Mj08tKbwMYgCbUQYHk835BI8%2BujJwFUBnLYD9NI3982cXr319zj8IWnAv5W5lvt5Bm5%2BJIbrLqTCW5uTSBjqkAQH31lD6KDyJI47NM0jjdcDOjxffZTvebbOvkbDNl4vYX9BRSeIsVArYStMoQtmSuC7zWmkrp26MGFntpztkz2uxYgGNREfr0jrWFtSy5sodiv0EsywcKpcQ5IwHL502f32SbsBM3mhuPsEYPDHrxpfGPFB%2BDnF%2BECEghgMB0V9aI8W%2FEHTOCrH2PAceyYlHVRXhzrzBJurgAjtRKHJOYexbGNdl&X-Amz-Signature=85ac3fec88b882120af5214d1e0044025ae384bbf98ee2e75c66e7e365ed3a37&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
