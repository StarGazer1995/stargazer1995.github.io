---
created: 2024-07-04T01:57:00+00:00
updated: 2024-08-17T12:46:00+00:00
date: 2024-07-04T01:57:00+00:00
title: First touch to mamba
cover: https://app.notion.com/images/page-cover/rijksmuseum_jansz_1636.jpg
id: 16b485d2-90af-4103-816d-314870e04d6a
---

![](https://prod-files-secure.s3.us-west-2.amazonaws.com/9ae3228c-6982-46ec-8946-abb7d53f72af/f4425041-9cff-41b3-9da7-b628790af0b0/Untitled.jpeg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662B4G7BOG%2F20261004%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261004T133300Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD%2B1zNSuFuQY%2Fzept7wyXcNCj%2FXMvajTsjrwFaHV5xNaQIgAIuegHnv13xMddhlem8MVqWGUehbt8k2%2FyZfVU0A2cAqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAKxpqVaudZ4ZDsP4CrcA3YGx9jHO7UpqvvlnlqsacGTeI1hOtdWz8BfKwn9GlziwpxqmsNUFWPDqQOOfXwuPyaFfXG31j3rZMeDxVu1A%2FW82hSijaIIag%2FIINXZgg3cIS%2B83nR2MY6hRwgjp1E4QlTMTk0%2BR7kdp2lrw9Inwpz5xXDczr5udvNTdqPdriPv7vAUTg2l17vwNSwoHjumklPfYGYogm0kxKa6qy38zlCL6wGQ5N0zM30Ck98jqrJKVstufumdJG%2F21VE0ye%2BUBzvfjZbZPPU5Fl9vzrVK0LfXSUsT2qtmgGj7wwP3SgoU%2B7mKQslTNH%2FKxxeBvtvSD1jSoIO7CcbOJZVn8dDtLsreLtVr7LSmMYuNDnwbiCRa7gHrF2bhUtdAwUhTV%2BUw3r8iZ9ombVDA4Cbb9TP%2FD1AXV9IHFKV7JZze%2B4a0w7bt8BUfRpGM1egS2br4Kxnv8bjwt%2FfsTJVBJLb8QOYcBYaVWrj62p4FTl%2BKeyk0pyvXCHiBFtqhfXerU3yO4mDeEgWh%2FtP8eEzciRs1mUe6l6rxkSzLNwDGZ47YG7fYIYL3cILA7If9eGb6liavcypXLPTueE0Kwc5Oiv1SKDYHXssob2qlKWicd2T1KUDTp%2B0fvQ2SuVfogEWamh1RMICZiNYGOqUBAkyCtS398Jl%2FMNB7tMdbAjqcUiNpzJHYGltumbLmw9s9K167NQb04W9bk1E%2F4SAc%2BuCWYII5aaEoQnMb81sKkkuyu0H7KtXjiKLrzbvgdUDIemfedDUYgItRMRP7yXf6n%2BsDM6Kqo7yyaAV%2BNoqP6lJNEI8AMzvlzaymCdU37cpJi5eY1zajamvwDdeKTpBUjCGw%2FgpEFhmSHeDvcW8lZAyKqDsT&X-Amz-Signature=da38efce9970db1334acfa98f3b10b0777f556fe23970602dcc0c511119e2581&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

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
