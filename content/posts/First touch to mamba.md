---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDD7OTLY%2F20260916%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260916T020156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGqo2gNGlkvITAFonRw5ckE9wg0ut9Mc%2FfPXEwvO%2B9SCAiEA3gBgqNQYt3WynShcLMEtV14yXnvUd0Ck6qC4qkwi8Vcq%2FwMIChAAGgw2Mzc0MjMxODM4MDUiDDusnJFfvEttpGTIsyrcA9igZSdXqDdZJLG52v9E15IaJARniRkir95Kr1PS%2BZp%2BWGT3NA9UyqSWw2n%2Fz%2BeWulwwuzh1N11IdrhCb6LFW%2Byaol7pZ5S%2FvWrZsbt9FABQyxlGFMGnm2h%2Bdm8BUsdYv4v%2Bjb2o3UGeb6KR5tDvYVrwOHCmjAWs5Obbh8IQaGEyfvhlQP958IGjuilkc0Ng4aEuDgJSOl%2B1zB941i2OdlagUV0FCqmFUN16Q0BqHg4j%2F1h%2FLYxGWfLDPHsX2FN4SMKne9v2ZpyVsTtml1AV%2BdXZwqMS8xdsESSzhsyQN%2B%2Fk1tsMIyzvRGMvCzNzsBtXVcykBP8fEupgqt9rVLgofcVeZdJD9gWPjcotmJ4eakniBuGVlQuzNwk7SRMCorMbXuj7fNKLzCRXbm4FqvzaL5HDhf68ZAwT4PjST7jt0kZgJh6vHnqt23sQ935P%2FRFUczQMeeweS2BukMU0PIJ8NVy3IGA%2B1tA00%2Fs9sL7lMZc9UOy3HhrHN6avEZbCV%2FNLI6rE%2BblfrezEPAJq9WUia17QIBcg1FhZ9eVwJt8Gum8sjrD2F7Dann%2B8fZ1MBiaGlyxoSr%2F8W7ykbCEFqOt7UPq4oE0GyQHqogG0qgkvcRBZxcqwIP71AeyqDzCYMLLLp9UGOqUBq7qO4Jf46zD9rdfzIRfN7dr%2BEG4FyJbOH4i2FcjuvCHjKynade4nmR4WElRjZKx%2FELzS2yIw32mmsZbdkWZEfmfZvgcryfGHMa%2ByZSBuiToRfuNteeg%2BlmKjjN08qgbQcFazqJULQg3cbzGHejBD9x%2FH421L9D5j74QsF1ED2Vqfgk0oGK5bAOzb25V4qV2AJee4nRCj3rUsAYr%2BIvpNXo62aePL&X-Amz-Signature=8ffe993d9e9d2013dba4e9162d03c505407dbbc015c2c418dd4b7d43722965c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
