---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XE5A7XEN%2F20260801%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260801T013007Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5vr6TOtdbCTXfQ%2B1mSXG3j3VTRMo%2B8B1Zeg5QVbia7AIhANj5e10WwiKpq3FUf8UQdYsE9JjqsA%2F2bUuga8QPUOdiKogECLr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxBj30mmwk0VYdLWEEq3ANXzLoq%2BMJvqYajaI4qo8PqlkENCLEVS0stZIg9%2FtxJ%2FOisywRRgwkYLR4T5bYWFBzJUlMomOEWCUt5LpNZZ4XdwuXfyHzvN2sXbhxXPM7qHkTE5nBpOCWat8DX9wztvjKSD3nhDR%2FAK4OultespwYFnFLK9fsn9NRWB0yxzjbCVfBQkbdjI0i5%2BwmUyK8i%2FwvZBE8rJsp%2BfmW6VTyEtcMEvCUUwOQV2FZZvW%2FCprhhyjF8c8T1J8IHwW1VjHMtFIdqaZWpfNQ6qmfS38pbtjVP8wozMBGMvXOvLUo1YL%2FHHiMrs8%2BkV0DSiiGJO14YijRUAbiJe2twTjrRDG4hgxhng1GessOkt83EZfAgsdo7Y4vKNPgDi2hdJ04bMWFNCgDyL2E9uBKyICsIO0y0P6rgkX0Uw57EH3FvpkMbLspNVBlRK0E3A5flbQd91w4IYwyS5CPDTMM4YTsPsiROjxFcl00CvwLyAP3R9Tg%2FCcv%2FMLsCRlSQWfgIvtR4UGd3Tnd1VUhqDsGFzGoBeC5KcWaI1eOzWoI%2BQDsAmQpxIznBqu8gP7vLQYqKld%2FoNtH1z0r2YQ05T5qHP0%2FtG1qXEuHgN5iqCr82OQWlu%2FsTpwarS7Q4v7TS3q%2B1FT5JWDDqjLXTBjqkAZZUXYZY997UbXDF88fi1zuIqawJlkCFbROjW6YvSp0zwJONBsZdnhMi9pTBJYWhpctg8vaFUNLXhiPS3nrHO0gMShEpmsTFLRJoIvJnwmaZkh4F4l44uzr0zip%2Bfe2jLRJnvyYJGkNhj8u6h3VlniDT2ZLZ%2B7khmonsx1vw4bcQHwmeX4S75FnD31GpDl3IF1Qti8L0FlhUKHcWuAq6bpybqNC4&X-Amz-Signature=749312a412dfff60554df88402df12c08995ce3a05658b3340825fe1e417e9ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
