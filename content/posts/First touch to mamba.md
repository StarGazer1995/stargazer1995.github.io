---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIMAEQ65%2F20260908%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260908T202520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFig56F01JkppYr6ZfwKEthggl4ZoBZ5QjtiFMLSSkE3AiAcx2oFTDz2feo3O9XwcrLOMNijTQQECdXMb3%2Btsdh3Yyr%2FAwhaEAAaDDYzNzQyMzE4MzgwNSIMaC4cmqIZLQEa39uOKtwD%2FbzMZf9kpvVcQSbbZyTINoo9UK2WYi2KB9DXO%2BItijYgAGh1Oq%2BKFtvjK1MOX5eJIw2IMMbmRRQb8taIWIKz%2FtkhtYjeZB%2FTyEHk%2FytcbtQ4UpYJ5jwhdiAQC%2BS9m3COoWc9RhPd%2B7ZWtrNSSrTDNgyqVGwfyQIBxZwxjzY1GBxgsLQ4qVxwkNxQ9jFaSJFtzr2cizO31s4nYmxKFImdTMpQ2xDCqWVlG4TbQYkDhc0by1GIF7EX2LoEzO4aiW%2BZ7utfVx9jULWrRz0attriHhaScjYMGM60eFokw%2Byzg6vXnc8pNkbJ2n91zPfLqQdhnByXeiVBMdPB8fxUxoP7vRzlJdzwe32%2F0yUPBTwzOoV%2FTcMWp4BniCQ9ws5PcvwLTK52PYj1X%2BevBtZnrDJUbbwKrKcZbILefytFSvI75rEHahXSsSI%2BHJLXYVCES1MAWqaKO4A%2BhJNNu3Db10qS6yD75%2B7ViIrpNkxWOKExLh72G3vZlu9cVmoAJ8TzVbXLI6C%2BAewzPC6MM2c6WT%2BLoVIeDao86878xuMWLyFfzf6%2FKfObVKrrFXvmnlx%2BTU941loK5HfEvhg1p88u%2FoagRsnqKW1DEUeUBUkz4WlHFQpikkQ4JyN0F3UaYcAw4IGB1QY6pgF%2Ba9Wl%2FGGmrYg5SK3wsib%2Fl82LvD0KPGLHeVKUhL3V4xXRhkO5xe3RidSFU9gFeI8Cra%2Bya2CkBzHGi5H0h2z9HvNxihUGbLs34Un5610E2UXuv4y4P3NluKil%2B2U2PxqormONj%2F%2F7frwJ0S0%2BJcmlQ6WC0ExJceWJPZbOmc4UIsRAx3%2Bihl9CCO9ZfiFDBYzl%2FslcSnRiPo0ZWMiM2r%2BPGRlHv6MD&X-Amz-Signature=e3534443649e507d51b5ccfbdd2da69b7a13dfbf4a34ee19ccf13b7dff70c9b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
