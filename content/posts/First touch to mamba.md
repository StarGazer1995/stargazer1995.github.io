---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIUIMO7W%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T012313Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCo9eCb2ATL3tG%2FUh7MGvULr9JkYNjpNMqSCn%2FGnis%2BaAIhAMjyWNE%2FcI47hppbWSq%2BDHrvNMni4XzzXWDssdmRVfH2KogECLD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGis33On7TVnkreCMq3APdmGR4QDjrFJboOpZZzoUhHBtleNB6IMS2zJC%2BO79fG%2Ftthh5q6hAottZW3uyzlAqOvKJDmsldFTm3o3vPdTsn%2BGzfdaNR3%2Fpl41G1io5GMaOtzzFtOJDclJaIqdg3brLQfKodEAdoxJ0QlIiv7tLAoREhr%2Bm2aU8gYRwNoZr5WHKebODFpCwZRoAcrbyxBn6lBAjjyKCNRHSOqcZMqHiQqUnJt9AhNmfkP%2BH%2BZBNZ79eJHzax9aGL8ziMqgZ9eTIzkjGexqaFEAF3uODrBfma9W2TVt7HlHOCi1DVbobPbCMMVBrV0OVd5GSsQNMS8PNncVUFsWVzUiR5QVWpQOJC6qc1xx1QIWAWQhYqKj26PLDMtiGo1iYgQOP%2FIJbBvJwbBzllgwoDbNTFVts405JqE%2F5Fj2h0KkkMKbbCfEz9EfXmTO%2B%2B3ljKkjfDR1%2FVZiFH%2B20%2F04NGXoweG6VArBy5xjEL68O9RgrSgVkeO9B8HPND21MZ1fk7Y00X4MeJpbJiK%2Fw9vjRPSjPyVka%2Fca%2FLQ24YKbB%2Ff7p%2BUx4lu0P3EM2VWrmu6XciLkg8a7A62n8JZSP%2F5Z9q%2BfRcfPfUROnTclOudQIY%2FsZ2J4VxBJ%2FT40m9oYiItFU2OGB9QjCjwvrSBjqkAbc2zSYQOih8bZWJlURwKVTnGxPkfFruo5X4krIo5jNs9r5zHmflxLTvPEwyxIm%2B4978UUKCsVfRCe431%2Fs5lozaHFbDp4cEP3XKaNsrr%2BMJH1RSgJtJzTyarbQyWeOJx9N9vdh1dgDR%2BNZ37lemTFLjbklvGFB6w1p%2Ff%2BSB0fI7rDQe%2FwYe4P%2FVm%2BNsZC8pXu9qxZPz1Fq8p4p4EePlYtrUtlkg&X-Amz-Signature=17d309dfa3f57f5de453fb50caaafdc30ee891f69d8f19555eff0ede6a6dd3ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
