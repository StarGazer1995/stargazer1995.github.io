---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://www.notion.so/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDRGJBRO%2F20250427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250427T065448Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC7UzzBWg59JbTrpKrByavsYphxppHGo6F0KYsWiPOhsAIgcMyaFTDSdkyt8uxJiVqIAULlUg%2FUFz62AkVH1zjaOxAq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDFVoexgnQN1AoNUjtyrcA7GbecvrOkktPR7wPrfYWWzwiG4SKi%2BFzg%2B3YbkYRdL9fJ%2BR4g6Bhsi6Rt%2BXAGfFPolzEAntdvOhuI1nhZYqO%2B3c%2F%2BIIB%2B5JHsrRxNxft1rYcSDYxkXCWt8XewVi7iD7j0UWM1a0K%2FqSaSoNqwo0cl4EfTEOuVLOqeQdiiQXxhbUtx0nUyCAnBkj2TqJo6E32%2FHnyKCSScutw6QGGZKAJ3Y5uyuLCcDpOqbu%2FX8oPrLlXEoifP262NKluP0FMFo1ni2DcPe8Yqg9k8jREoo8m4EO2QQ61NzToSHItUX9jI%2FB8F%2FbyZtouSMgcadpN8WbbEtHMOsVccRVbURbrRwh2T%2BHZoAUL7uS6BIb49F5dUFo2SFYlbitaty%2FXgZQNn1aY9jN7ym7dppzpHHip649j31j43OTxi5EPQOqnE5CEZT8%2BLowVSWC%2BIOwMFpbuc0RVnYBb%2FTHZD46nGmXvGytTOWw5qLAdvKdb8lDCVnwQmt9Na8fjtQXC%2BpminmOD0wvS%2FADxRls7Ajbwvyifl3XcGBtRuIbBlCMT1RHy6%2FlReOf5%2ByziBQElGO6WTHsYVl4igwfmhXYUdR5%2For%2BFkDstaKSiWVbZ%2B61MNWf1Rcy7FoUEHKIaP7XoSlv7AEnMKHttsAGOqUBZ5ebuNlkX0c08IriUGidU6cfyyHG3LcyF5FHgAe2FuvXKkS7f0mGJ0H5%2Bw%2B5V5qBMX1C3IHJ2CdT4YrJo7SXs8kFRYhQ%2Fio6LBba5r%2Bx%2F1JKMIT3qfkFsPE2ZP3IT9Q9pnxj1KTa9Je7Nrj1RSmZZ3nqYuPAXVrDTF%2FifTAHOENLyC9hqEzxwC8pqlNjc9KzgExU3YKmYbks3bnALJNyISqAchV1&X-Amz-Signature=c43135b2f062ccc32a2e30c99a85fde8d88f7aa3c9d7f3c72c56fe68bb2889e1&X-Amz-SignedHeaders=host&x-id=GetObject)

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
