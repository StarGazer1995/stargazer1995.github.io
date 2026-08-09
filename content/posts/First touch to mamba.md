---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673MIZ3TE%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T004613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBLCb80hjdTtxNustgXvkIsCePd8HZl3n61ZcYlUqbAVAiEA9UIAYuyfQf4rLCKi73we8P5mk4gQNVFBf%2FMu5uw2qcgq%2FwMIdxAAGgw2Mzc0MjMxODM4MDUiDAhsT2q97xRfHWRYESrcA445beJG4LR1RVJlFOGJTJ%2Bw4QEOvasW0C7rvJe3xZZY3F6yv2xHkc87kq0ZJZ%2BxcdDgdECWDa3neVF1MK3w7XhcugPzHeZ%2FOjUnJ4r7Zn4tLoAa2M493y4WY1NF3SD0IW%2FuEONhs1j7R0Srt7%2BxEcvwzUrSuW6vh7ILe3r2CAePE7Swt2Uzp3dQAoXs0%2FyQXx6EmTGa6ZsgYU76QKbUZDV%2F83iINZqtVD6Yt5TcmW7bgl3Az8XnK%2F88h24X%2Bbq6epbpeqDatVA23n0Cr5UGW6lizvXDG602zHZQOqiF%2Fl4MnrQl3wOdvu3YjelKDO4Pn93Sd%2FKaxSso0DEGgQdxpzgCZO6IW5HAZ2X%2B3TFT0UAyFcq%2F2qicv%2Fh%2FScPUECsER5twsyWrSkrY2QIUFFsrGhl%2BRMzb7IjRUQeojs7BlvVrjZPf2%2Buudred8x%2FpnVJGFlDPoXBxhTJKyHqbzfZxMjB3fouO4ADZpFIsCdEwUSxF3f8UiObgHGbnOejPdT66kcYi5mnrzQI4%2FY0Ibi8ZdwDF6kYXOhBFirwojMM2nZ%2B5yProIuSBIUTv%2FUDvH0TX9agHSTZts3ZDMumtHRZ%2FJdt9UvDBR%2Bq5r64eRBf8v%2BHEBT6gUWO2quF%2FD4jtMJDU3tMGOqUBXCgq34%2FWNvXRkOhIX1KuXp8vqQ4kORKPykZ2vmCRVFNbUB89sq7Rcn6VgXKQ8L3%2FSGOA%2Bp7mQMt%2FiULKZCojF7XQzeIcucdAsCgq%2BrMaaDYGV4G3OI5OWMSGUjXxV%2FZqh8mjouEqhfw7Mk2kVnyuZSJlIjW2Uj1QODUcTBv4qurcbMN11YDCJm2BOjY%2BEBoNJZvOX04OK1qi5Fdel%2FuLVRDwxTys&X-Amz-Signature=3b583124ed16e36b71d5e0f10e7205b44060039128c8fe6f8d6f91f058b14353&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
