---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VJKS2BM%2F20260516%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260516T125540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCaTi05a1EE1f0bjisfnhHUt2KNHKDNb%2BkK7zy4nirZ7AIgfQVVddGw3OvvQojZ3K5uZplPbQdwqUMb1WrrMb80xIQqiAQIjP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOJeO9ch9b6aZJqpvyrcA0eOHGIhqsb6JwdVGuRJ3K2FivZ0no9FAwh8WSadPwM0WhUzpn4QNwh9WXZw%2F%2BUyJjNtVbZMsJHAUu1Vt%2BZGVHyk8BUVBFeJYB7VTuwANcEkAvpXMTMT6mf7kJI6NiXed9H%2F6V9XBugxQL%2Foc4EiyT5hxDmB51ZVNsrzLhMmZnQ%2FXo3F9AqPtvnAfk9RtSySCyN4tc1XQkE1mm%2BFm7eCE7dZwXxEifQH2DB%2FeMcd9S8wtUfp27%2BaELES8cco1bxaV5T6crknQ4D4%2BTec9JX7F6RbE%2FXO5dP9Uvy%2FFvwF37aC3fUftNWJZ%2BMR%2BWeg%2FRkbs8ZCLeN2MqfKrPDcupUm2ZjxBmMXdX65J96M0n35kabXWYTYMdadt4C3yiLnI1Y2djPGVzoZwPEUTNFWjt8t3LZ9TSAwF%2BwnZuyyF%2Fl3wdDjKDpLDi26I0OwralypPtfHtpfoTlldN7YdxY5ffNli40L5acPWAex5wAjbf7EFFBrLtNBw3LWrH55WiB19pkkHCTqywEKBfP6O3m0jJ2VhB83eCSrjDCX39eEukfEGqEYGgD26VI8X1vJIbgoSyJnFJ1LeQRjhdvFUEpBaWNkRY341ih9Mm23akhUq3EvFgx3UaMEO4ItFEu5vEfbMM6lodAGOqUBwPFLy0scPXsryfgBniIt%2Bo5zbRv134kxs02Z59vx0Gj%2BAakYHVI9OB%2Fcfs1gv8b51Z%2BVTju9dJFyqkwU%2FInIVAksTcvZo9B2ZQJQNsnqmxk6K5tTMf0Cvluz8u4%2Bd0D1JUtLIuRHOxfRc3URoT425F6IGPMWTDs5Wt0vME6ldPsm1gEco7et%2BtYJxN2KgiV3ypOpNBxvgTXakMvKEuoxgalM2cDH&X-Amz-Signature=0f78384d40e98f8bc3fae5133c3450dc89e97d277316bdb8101d9bd886ebdf5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
