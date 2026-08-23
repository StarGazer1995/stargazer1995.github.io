---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SR6JQ2QN%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T121601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJHMEUCIQDiRpVb4%2BksPVvsAC5eW2UwFTHjXsOjMd0qSoKi8pmwYQIgTajezKphZ%2BXQxFFe3%2BHFhsP9kw7jeuYJ4loUlrJ%2FmqkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK5BtryWWUf8ZzNmAyrcAwluZ90OKwBCFh%2Bxg87ygojoUg2no48bz3KGguqtW3MmHcieSWu%2Fg8bXbE%2FYdfR8ilM6lXahlQhgegYXJI7%2BTQWBsXxyaQhTsR6d7C777sth9s3XJxU0HFnr3C6NNrE%2FFsvXyTeI4ow5dWjoHBplceSSFXQVhBeHEolwsVD7N9ITVCJLwZUgBl%2BZ9V3snszOT%2Bke0YdVb8RXGvepgkDaaQTyAZRhIQd3ttkX6jsRblBKupDoYbzPu2tocg1brCnVvYnThGOzitu5FPGdnvJXIBv8oJ5cmCHjyBp8u%2BdV0WJqQ9ev5WSeSMIK4e6JIWuc9S8fxJIp4WlgxKVtuKqbne20bL9kp37f53kVWfHEnk%2FuTgoZi57fy7iNqoInZPBf483LoHSpSKmxHnbvG7O4qMa4wRnQetQVVDVNlrGBAGLShTbLvvEz3Nb%2B57WVV8b9gb%2FT03K%2Bbbti5MtNhvmbYFbnuad%2FwY6%2Ftrz6Do4SDzo%2Fk8TW3ysUN3MnbC2W1GyQTincS%2Bohz5P8q7WvIwJPf27XgC72QG9uT6EZqCNIdtBCXxVBWohswXK0Fleoz5gG7AP%2BM3t6MLF4I%2BtySX5whUVal6zoLaZWrczyzPKbSs9%2BMgjghN4LL0JgWwbOMIDRqtQGOqUBr23pxdNSST1yu%2FXnJjtxPY88RdUy6S9FIJ9YQ%2FNYmuwXS6kSdwIqku%2Fn%2FmADRGsljgkPNbdcwFUMZan5ilJ6rhJYkic94ncMEaanG7KZ%2Fi9rPpxU6KOtnGFiV7kIZBSXRVdzvzJDuqFTG9%2FpIP2SQLLueTRcMw0EPIT2ahi4iDLiRmJL3RCuRMblSA45vPFmVASJ4C974mgQtLsPOWtoIv68A%2FA3&X-Amz-Signature=2a4ea3e0b22c0accc0dcc2b0f481d87595be8703580f7211e41bf086f7693c0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
