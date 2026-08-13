---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQXDWLQY%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T005708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIQCt%2BSYzY0KBomU18LrEdc3jisrCWuGZlvDL1DXd%2F267zwIgJkd3j9D8UxOuLEUvvHxnjRbJfnAXnvZxvQWzLDEG258qiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDbRXAVgOok%2FcLOrLCrcA2%2FzH9Z8bbu7tfaIHJSd86odTAq%2FS9NK3LZslU%2Fgsf%2FEMckxKLlL52cgaBhv8FNT8P0VVDKSJSBkd%2FUCZwf8huI7Wa6XuHg%2BDat3kfP%2Bb7vVDIu2Ur9ZGlURqJRD5g8nf9rb20fDSFHsvLd0KV0wIuuLaA86jO%2BAPFbO7ouXGqjTKeyrR8%2F%2BbO9UKZyEDnUMGKwm8aOkeeQXzfqojKFt%2FalgLeTXyqkNHyDsAuCR3aES%2BA6powzbltsFeE4pPP%2FCofrTQdhjVRIdQ0ziyApNZAneNk9ynFCvek6ATidXvrOURpYrZe4jHWg50RBYpNf9YSc%2FxtkGoiZQ2nnyjlSEElhWtqsMBxG10HIbCfaI6IyIa2j9xVzADYKkA0UMuDlsVC4OTulxnyzDoBWhOiV4ZJjJhdEGN7b1ujlE06VMKqF%2BzvJ7E9olCcV35dV3AWaDVh7kBbzs7mFK9u%2FC9ZZxIfbN%2BNmNxe5eWEu0U4FRgLc26fmFtvQ0zJJzWFLZ0SZfu7Bj53Ph2aoIc6W1IvI5IjgXguEFb5oxDDtrj9A%2FJ83tg%2B9n77f7557l5V4%2BLnTjXNvykfTLPjtMeYedCWl%2F%2But7VuCvc6PVPgm56MfT5L4%2F%2F8gw8vOGMmryV8yMMOfO89MGOqUBk70nwwCecOWn1OfRR5HfGNllvozy2NSki%2B%2BPhR7Arqvuzcl3BOltjzzZwUUxkBn%2Bl3QG3XS6dqsPxfXMQuWtuvGS8JyDkpq8hJiVMEq%2BUEynjKisonmyHzA4OoPruUVzgERFaqyvsfu0ABHoAoM0IE%2F1UoqQPsOAoG7DSJ4DsN2433iqHvoxqedYazSzF3c8PyJ44bvbtEl2SMhzOeD9dWOFVl%2FR&X-Amz-Signature=9aa06edf77399194df58554d49a2e1db6e2c53fb1336770dd0d462062ca206e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
